import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))
INSTANCE_ID = os.getenv("INSTANCE_ID")
AWS_DRY = True if os.getenv("AWS_DRY") == "True" else False
PREFIX = os.getenv("PREFIX")
