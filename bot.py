import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID"))

# client = discord.Client()

bot = commands.Bot(command_prefix="#")


@bot.event
async def on_ready():
    target_guild = discord.utils.find(
        lambda g: g.id == GUILD_ID, bot.guilds)
    if not target_guild:
        print("[ERR] Target guild not connected")
        exit("Target guild not connected")
    print(
        f"[INFO] Connected to target guild: {target_guild.name} (id: {target_guild.id})")
    print(f"[INFO] {bot.user} is ready!")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You do not have the correct role for this command")


@bot.command(name="start", help="Start the minecraft server")
@commands.has_role("server")
async def start(ctx):
    await ctx.send("Starting the server")


bot.run(TOKEN)
