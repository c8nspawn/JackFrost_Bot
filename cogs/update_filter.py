from twitchio.ext import commands


class UpdateFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def prepare(bot):
    bot.add_cog(UpdateFilter(bot))