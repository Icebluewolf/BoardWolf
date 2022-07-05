import os
import discord
from utils.bot import BoardWolf

COGS = ["utility"]

intents = discord.Intents.default()
bot = BoardWolf(description="Play Turn Based Strategy Games On Discord!",
                intents=intents,
                debug_guilds=[678359965081141286])

for cog in COGS:
    bot.load_extension(f"cogs.{cog}")


@bot.event
async def on_ready():
    print("Logged In")

bot.run(os.environ["bot_token"])
