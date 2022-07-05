import discord
from discord.ext.pages import Paginator


class PrettyRespond:
    def __init__(self, ctx: discord.ApplicationContext):
        self.ctx = ctx

    @staticmethod
    async def _paginate(value: str) -> list[str]:
        pass

    async def error(self, traceback: str) -> discord.Interaction | discord.WebhookMessage:
        e = discord.Embed(color=0xff0000, title="Error")
        e.set_footer(text="Report This In The Support Server")
        e.add_field(inline=False, name="Error:", value=traceback)
        return await self.ctx.respond(embed=e)

    async def fail(self, message: str) -> discord.Interaction | discord.WebhookMessage:
        e = discord.Embed(color=0xd33033, title="You Can Not Do That", description=message)
        return await self.ctx.respond(embed=e)

    async def success(self, message: str = None) -> discord.Interaction | discord.WebhookMessage:
        e = discord.Embed(color=0x00ff00, title="Success!", description=message)
        return await self.ctx.respond(embed=e)

    async def general(self, title: str, message: str) -> discord.Interaction | discord.WebhookMessage:
        e = discord.Embed(color=0x30d3d0, title=title, description=message)
        return await self.ctx.respond(embed=e)
