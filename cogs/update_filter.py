from twitchio.ext import commands
from json import load,dump


class UpdateFilter(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot
        

    @commands.command()
    async def banword(self, ctx, *, word: str):
        if not ctx.author.is_mod: return
        self.__bot.unload_module('cogs.events')

        try:
            with open("./data/blacklist.json",'r') as blacklistfile:
                blacklist = load(blacklistfile)

            blacklist.append(word)

            with open("./data/blacklist.json",'w+') as blacklistfile:
                dump(blacklist, blacklistfile) 

            await ctx.channel.send(f"{word} has been banned")
        
        except: pass

        self.__bot.load_module('cogs.events')

def prepare(bot):
    bot.add_cog(UpdateFilter(bot))