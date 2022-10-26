from twitchio.ext import commands

@commands.cog()
class UpdateFilter:
    def __init__(self, bot):
        self.bot = bot

def prepare(bot):
    bot.add_cog(UpdateFilter(bot))