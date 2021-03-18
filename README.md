# How to use Raspberry Pi with Discord to check if friends are online

I want to share my experience in working and testing a small discord bot with discord.py and my rapsberry pi. It is for simple things like showing if someone is only etc.

The main idea is building a Discord bot which shows to Raspberry Pi number of online Members and passes it then to an LED light or a display

### Disclaimer
I don't take any responsability for  damage on your Raspbarry Pi or any hardware. I just want to know you what worked for me :)


## Add Bot to Discord Server

1. Go to Discord Developer Console
![Picture example](https://i2.wp.com/joel.business/wp-content/uploads/2021/01/Go-to-Discord-Developer-Console.png?resize=768%2C122&ssl=1)

2. Click on “New Application”
![Picture example](https://i1.wp.com/joel.business/wp-content/uploads/2021/01/Click-on-New-Application.png?resize=768%2C73&ssl=1)

3. Type in a name and click “Create”
![Picture example](https://i2.wp.com/joel.business/wp-content/uploads/2021/01/Type-in-a-name-and-click-Create.png?w=430&ssl=1)

4. Click “Bot” on the left side and then “Add Bot”
![Picture example](https://i2.wp.com/joel.business/wp-content/uploads/2021/01/Click-Bot-on-the-left-side-and-then-Add-Bot.png?resize=768%2C186&ssl=1)

5. Write your Bot Token down, because you’ll need it later
![Picture example](https://i2.wp.com/joel.business/wp-content/uploads/2021/01/Write-your-Bot-Token-down-because-youll-need-it-later.png?resize=768%2C175&ssl=1)

6. Go to "OAuth2" in the navigation, select "bot" in scopes and "Administrator" at bot permissions. Then you should open the link.
![Picture example](https://i2.wp.com/joel.business/wp-content/uploads/2021/01/Go-to-OAuth2-in-the-navigation-select-bot-in-scopes-and-Administrator-at-bot.png?resize=768%2C439&ssl=1)

7. Add the bot to your server and confirm it

=> Your bot should be now in your server but offline

## Update your Raspberry Pi

1. You need to update package lists
  ```sudo apt-get update```
  
2. Then you should upgrade it to
  ```sudo apt-get upgrade```
  
3. Now we should clean things up a bit
```sudo apt-get dist-upgrade```

4. Reboot your Raspberry Pi



## Check which version of Raspbian your Pi is running on

```cat /etc/os-release```

Raspian Buster (Version 10.x)  ships with Python 3.7.x and should work great with discord.py. You can click here if you want to upgrade your OS to Buster.

If your Raspberry Pi is not running on Buster or Stretch you have to install Python manually, but if not you can skip this part.

1. Install libssl-dev (to ensure we can use pip when we install the newest version of Python)
  ```sudo apt-get install libssl-dev```
  
2. Install libffi-dev (to ensure audio works with the Discord bot)
  ```sudo apt-get install libffi-dev```
  
3. Install libsqlite3-dev (this will be handy, as it installs libraries needed to install sqlite3 support)
  ```sudo apt-get install libsqlite3-dev```
  
4. Grab the latest version of Python 3.x from [python](https://www.python.org/downloads/)
  ```wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz```
  
5. Extract the files, and enter the directory
  ```tar xzvf Python-3.6.0.tgz```
  
6. Then run cd Python-3.6.0/ to navigate to the folder
  ```cd Python-3.6.0/```

7. Run configure to check for dependencies, and get ready to build the Python installation (This will take 2-5 minutes)
  ```./configure```

8.Run make to start compiling the software (This will take 15-30 minutes)
  ```make```

9. Install Python 3.6.x (This will take 10-15 minutes)
  ```sudo make install```
  
10. Reboot your Pi!



## Install Discord.py

You may need to install the following, if you have installed Buster a short time ago

```sudo apt install python3-pip```
```sudo apt install python3-cffi```
```sudo pip3 install discord.py[voice]```

Install latest version of the Discord library for Python (Discord.Py)

```sudo python3 -m pip install -U discord.py[voice]```

## Run the bot

1. Move to folder
  ```cd ~/isOnline_bot```

2. Run python script
   ```python3 bot.py```
  
2. Go to your Discord Channel and type in “?membercount” and if someone is in a channel it will glow up 🙂

Side note: Make shure you use a text channel which is empty or not used, because thebot will spam it

3. Have some fun with this bot and be updated everytime someone is online!



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* My main inspiration was this arcle from [gngrninja.com](https://www.gngrninja.com/code/2017/3/24/python-create-discord-bot-on-raspberry-pi#idiscordpy)
* etc
