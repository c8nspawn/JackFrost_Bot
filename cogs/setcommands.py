from twitchio.ext import commands

class Setcommands(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    #test
    @commands.command()
    async def test(self, ctx):
        await ctx.channel.send('this is a test')

def prepare(bot):
    bot.add_cog(Setcommands(bot))