import discord
from utils.pretty_respond import PrettyRespond
from utils.database import Database
from discord import Interaction, WebhookMessage


class AdvContext(discord.ApplicationContext):
    # For attributes of ctx
    # @property
    # def name(self):
    #     return "object"

    @property
    def prespond(self, *args, **kwargs):
        return PrettyRespond(self)

    @property
    def db(self):
        return Database()

    # async def respond(self, *args, **kwargs) -> Interaction | WebhookMessage:
    #     return await super().respond(*args, **kwargs)


class BoardWolf(discord.Bot):
    # def __init__(self, description=None, *args, **options):
    #     super().__init__(self, *args, **options)

    async def get_application_context(self, interaction: Interaction, cls=None) -> discord.ApplicationContext:
        return await super().get_application_context(interaction, cls=cls or AdvContext)
