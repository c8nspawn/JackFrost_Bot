from twitchio.ext import commands
from random import random
from asyncio import sleep

class Love(commands.Cog):
    def __init__(self,bot):
        self.__bot = bot
        self.__cooldown = False
        self.__cooldown_enabler = False

    async def cooldown(self):
        await sleep(5)
        return False

    @commands.command()
    async def love(self, ctx, *, lover):
        if ctx.author.is_mod and "cooldownoff" in lover.lower():
            match self.__cooldown_enabler:
                case True:
                    self.__cooldown_enabler = False
                case False:
                    self.__cooldown_enabler = True
        elif not self.__cooldown or self.__cooldown_enabler:
            self.__cooldown = True
            if "roppusuke" in lover.lower().strip():
                match ctx.author.name.lower():
                    case "rinnekanzaki":
                        await ctx.channel.send(f"There is 100% <3 between {ctx.author.name} and {lover}!")
                    case _:
                        await ctx.channel.send(f"There is {round(random(),2) * 100:.0f}% <3 between {ctx.author.name} and {lover}!")
            else:
                await ctx.channel.send(f"There is {round(random(),2) * 100:.0f}% <3 between {ctx.author.name} and {lover}!")
            self.__cooldown = await self.cooldown()

def prepare(bot):
    bot.add_cog(Love(bot))