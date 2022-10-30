from twitchio.ext import commands
import json


class UpdateFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def banword(self, ctx, *, word: str):
        self.bot.unload_module('cogs.events')

        try:
            blacklistfile = open("./data/blacklist.json",'r')
            blacklist = json.load(blacklistfile)
            blacklistfile.close()

            blacklist.append(word)
            blacklistfile = open("./data/blacklist.json",'w+')
            json.dump(blacklist, blacklistfile) 
            blacklistfile.close()

            await ctx.channel.send(f"{word} has been banned")
        except: pass
        self.bot.load_module('cogs.events')

def prepare(bot):
    bot.add_cog(UpdateFilter(bot))