import discord
from discord import slash_command, Option


class Utility(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def ping(self, ctx):
        await ctx.prespond.error(str(self.bot.latency * 1000))

    @slash_command()
    async def test(self, ctx):
        await ctx.prespond.general(title="respond", message="1")


def setup(bot):
    bot.add_cog(Utility(bot))
