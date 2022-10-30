from twitchio.ext import commands
import json

# purpose of this command is to create commands on the fly that are simple and only repeat what they were initialized to say. save these in a json maybe a dictionary
# until they are explicitily removed

class Set(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def set(self, ctx, *, string):
        self.bot.unload_module('cogs.events')
        try:
            setfile = open('./data/setcommands.json', 'r')
            setcommands = json.load(setfile)
            setfile.close()
            splitstring = string.split(' ')
            setcommands[splitstring[0]] = ' '.join(splitstring[1:])

            setfile = open('./data/setcommands.json', 'w+')
            json.dump(setcommands, setfile, indent = 4)
            setfile.close()
        except: pass
        self.bot.load_module('cogs.events')



def prepare(bot):
    bot.add_cog(Set(bot))