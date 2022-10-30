from twitchio.ext import commands
import json


class RemoveFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def prepare(bot):
    bot.add_cog(RemoveFilter(bot))