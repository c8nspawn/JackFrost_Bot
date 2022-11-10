from twitchio.ext import commands
from json import load,dump

#remove component of set command

class Remove(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot
    
    @commands.command()
    async def remove(self, ctx, *, string):
        if not ctx.author.is_mod: return
        self.__bot.unload_module('cogs.events')

        try:
            with open('./data/setcommands.json', 'r') as setfile:
                setcommands = load(setfile)
                
            splitstring = string.split(' ')
            del setcommands[splitstring[0]]

            with open('./data/setcommands.json', 'w+') as setfile:
                dump(setcommands, setfile, indent = 4)
        
        except:...

        self.__bot.load_module('cogs.events')


def prepare(bot):
    bot.add_cog(Remove(bot))