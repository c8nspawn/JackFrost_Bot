from twitchio.ext import commands
import json

#remove component of set command

class Remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def prepare(bot):
    bot.add_cog(Remove(bot))