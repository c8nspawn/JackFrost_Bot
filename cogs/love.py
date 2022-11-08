from twitchio import commands
import random

class Love(commands.Cog):
    def __init__(self,bot):
        self.__bot = bot

    @commands.command()
    async def love(self, ctx, *, lover):
        await ctx.channel.send(f"There is {random.radnom():.2f}% love between {ctx.author.name} and {lover}")


def prepare(bot):
    bot.add_cog(Love(bot))