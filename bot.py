import discord
from discord.ext import commands
import RPi.GPIO as GPIO
import time


TOKEN = 'YOUR_TOKEN'

description = '''isOnline Bot'''
bot = commands.Bot(command_prefix='?', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    



    
@bot.command()
async def membercount(ctx):
    """Counts the members"""
    
    while True:
   
        member_count = len(ctx.guild.members) # includes bots
        true_member_count = len ([m for m in ctx.guild.members if not m.bot]) #doesn't include bots
        print(true_member_count)
        await ctx.send(true_member_count)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
    
   
        if true_member_count >= 1:
            GPIO.output(18, True)
            print("LED ON")
    
    
        if true_member_count < 1:
            GPIO.output(18, False)
            print("LED OFF")
        

    


bot.run(TOKEN)
