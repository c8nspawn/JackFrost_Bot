from twitchio.ext import commands
from random import random
from asyncio import sleep

class Love(commands.Cog):
    def __init__(self,bot):
        self.__bot = bot
        self.__cooldown = False

    async def cooldown(self):
        await sleep(10)
        return False

    @commands.command()
    async def love(self, ctx, *, lover):
        self.__cooldown = True
        await ctx.channel.send(f"There is {round(random(),2) * 100:.0f}% love between {ctx.author.name} and {lover}!")
        self.__cooldown = await self.cooldown()

def prepare(bot):
    bot.add_cog(Love(bot))