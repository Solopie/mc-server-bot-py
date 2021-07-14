# MC Server Bot

Bot for discord to turn on minecraft server hosted on AWS EC2

## Setup

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
```

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

## Technologies

[discord.py](https://discordpy.readthedocs.io/en/stable/) - Discord bot

[boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Interact with AWS EC2 server instance

Developed/Tested with Python 3.8.5

## Start up guide I used for making discord bot in python

https://realpython.com/how-to-make-a-discord-bot-python/