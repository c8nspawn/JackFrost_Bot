from twitchio.ext import commands

class Setcommands(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

@commands.command()
async def bruh(self, ctx):
   ctx.channel.send('bruh')

def prepare(bot):
    bot.add_cog(Setcommands(bot))