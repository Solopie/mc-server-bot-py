# MC Server Bot

Bot for discord to turn on minecraft server hosted on AWS EC2

## Setup

*Note these instruction have only been tested on Ubuntu 20.04, Python 3.8.5)*

**Install python (3) and virtualenv**

```
sudo apt install python-is-python3 -y
sudo apt install virtualenv -y
sudo apt install python3-venv -y
sudo apt install python3-pip -y
```

**Create virtual environment**

```
python -m venv venv
source venv/bin/activate
```

**Install required dependencies**

```
pip install requirements.txt
```

**Create .env file (use sample)**

*.env*

```
DISCORD_TOKEN=YOUR_BOT_TOKEN
DISCORD_GUILD_ID=YOUR_DISCORD_GUILD_ID
INSTANCE_ID=YOUR_EC2_INSTANCE_ID
AWS_DRY=False
PREFIX=#
```

*DISCORD_TOKEN* - Discord bot token retrieved from https://discord.com/developers/applications/UNIQUE_ID_HERE/bot

*DISCORD_GUILD_ID* - Right click the guild icon on discord and select "Copy ID"

*INSTANCE_ID* - Property of the AWS EC2 Instance

*AWS_DRY* - Used for testing. For production just leave as False for the commands to work.

*PREFIX* - Prefix for commands


**Setup AWS Credentials**

*~/.aws/credentials*

```
[default]
aws_access_key_id=YOUR_ACCESS_KEY
aws_secret_access_key=YOUR_SECRET_KEY
```

*~/.aws/config*

```
[default]
region=YOUR_REGION
```

**Run program**

```
python bot.py
```

## Commands

*start* - Start the AWS EC2 instance

*status* - Check the status of the AWS EC2 instance

*Note that I am only using the bot to start and stop the instance. Not the actual server as I have cronjob scripts to start and stop the server automatically*


## Technologies

*[discord.py](https://discordpy.readthedocs.io/en/stable/)* - Discord bot

*[boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)* - Interact with AWS EC2 server instance

Developed/Tested with Python 3.8.5 (Ubuntu 20.04)



## Start up guide I used for making discord bot in python

https://realpython.com/how-to-make-a-discord-bot-python/