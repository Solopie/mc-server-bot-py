import discord
from discord.errors import DiscordException
from discord.ext import commands
from util.config import TOKEN, GUILD_ID, PREFIX
from util.aws import EC2_Client

bot = commands.Bot(command_prefix=PREFIX)

# Initialise boto3 client
ec2_client = EC2_Client()


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
    # TODO: ERROR LOGGING
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send("You do not have the correct role for this command")
    elif isinstance(error, discord.DiscordException):
        print(error)
        await ctx.send("Something went wrong. Please contact an admin!")


@bot.command(name="shutdown")
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Bye")
    exit()


@bot.command(name="ping", help="Should return pong")
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command(name="setup", help="Setup the bot on first startup")
@commands.has_role("admin")
async def setup(ctx):
    await bot.change_presence(activity=discord.Game(name="mc.solopie.com"))
    await ctx.send("Setup complete")


@bot.command(name="start", help="Start the minecraft server. May take a minute for the server to go online")
@commands.has_role("server")
async def start(ctx):
    await ctx.send("Starting the server")
    response, err = ec2_client.start()

    if err:
        await ctx.send("Command failed. Please contact an admin")
        raise discord.DiscordException
    else:
        await ctx.send("Server has successfully started! Please wait a moment for the server to startup.")


@bot.command(name="status", help="Check status of server")
@commands.has_role("server")
async def status(ctx):
    await ctx.send("Fetching the status")
    status, err = ec2_client.status()

    if err:
        await ctx.send("Command failed. Please contact an admin")
        # raise discord.DiscordException
    else:
        await ctx.send("Status: " + status)

bot.run(TOKEN)
