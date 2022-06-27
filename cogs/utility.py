import discord
from discord import slash_command


class Utility(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def ping(self, ctx):
        await ctx.respond(str(self.bot.latency * 1000))


def setup(bot):
    bot.add_cog(Utility(bot))
