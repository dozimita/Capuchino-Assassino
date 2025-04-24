# main.py
import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True  # Enable if your bot needs to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(activity=discord.Game("with SWORDS"))
@bot.command()
async def status(ctx):
    """Command to check the bot's status."""
    activity = bot.activity if bot.activity else "onnumilla , verte irikennu ,same as you"
    status_message = f"ivda undee!\nCurrent activity: {activity}"
    await ctx.send(status_message)
import random

@bot.command()
async def whatis(ctx, member: discord.Member = None):
    """Gives a fun nickname to a user."""
    if not member:
        member = ctx.author  # if no user is mentioned, use the one who sent the command

    fun_names = [
        "potato", "spicy cucumber", "coding ninja", "lazy panda",
        "banana overlord", "meme master", "glitch in the matrix",
        "daydreamer deluxe", "sleepy wizard", "pixel pirate"
    ]

    nickname = random.choice(fun_names)
    await ctx.send(f"{member.display_name} is \"{nickname}\" 😄")

keep_alive()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # Set your token as an environment variable
bot.run(TOKEN)
