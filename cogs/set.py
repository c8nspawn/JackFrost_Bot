from twitchio.ext import commands
from json import load,dump

# purpose of this command is to create commands on the fly that are simple and only repeat what they were initialized to say. save these in a json maybe a dictionary
# until they are explicitily removed

class Set(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def set(self, ctx, *, string):
        if not ctx.author.is_mod: return
        self.__bot.unload_module('cogs.events')

        try:
            with open('./data/setcommands.json', 'r') as setfile:
                setcommands = load(setfile)
                
            splitstring = string.split(' ')
            setcommands[splitstring[0]] = ' '.join(splitstring[1:])

            with open('./data/setcommands.json', 'w+') as setfile:
                dump(setcommands, setfile, indent = 4)

        except:...
        
        self.__bot.load_module('cogs.events')



def prepare(bot):
    bot.add_cog(Set(bot))