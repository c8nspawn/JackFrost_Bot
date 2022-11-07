from twitchio.ext import commands
import json


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.blacklist = 0
        self.setcommands = 0 
        with open("./data/blacklist.json",'r') as blacklistfile:
            self.blacklist = json.load(blacklistfile)
        with open("./data/setcommands.json",'r') as setcommandsfile:    
            self.setcommands = json.load(setcommandsfile)

    @commands.Cog.event()
    async def event_message(self, message):
        if message.echo:
           return 

            # filter
        if any(map(lambda x: x in self.blacklist, message.content.split(" "))):
            if not message.author.is_mod and not message.author.is_broadcaster:
                await message.channel.send(f"/timeout {message.author.name} 120 Said banned word")
            # await message.channel.send(f"/delete {message.tags['id']}")
        
        #setcommand checker
        # add a cooldown here
        if message.content.startswith("?") and message.content[1:] in self.setcommands:
            await message.channel.send(self.setcommands[message.content[1:]])

def prepare(bot):
    bot.add_cog(Events(bot))