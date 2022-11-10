from twitchio.ext import commands
from json import load, dump


class RemoveFilter(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot


    @commands.command()
    async def removeban(self, ctx, *, word: str):
        if not ctx.author.is_mod: return
        self.__bot.unload_module('cogs.events')

        try:
            with open("./data/blacklist.json",'r') as blacklistfile:
                blacklist = load(blacklistfile)

            blacklist.remove(word)

            with open("./data/blacklist.json",'w+') as blacklistfile:
                dump(blacklist, blacklistfile) 

            await ctx.channel.send(f"{word} has been banned")
        
        except:...

        self.__bot.load_module('cogs.events')

def prepare(bot):
    bot.add_cog(RemoveFilter(bot))