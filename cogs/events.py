from twitchio.ext import commands
from asyncio import sleep
from json import load


class Events(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot
        self.__blacklist = 0
        self.__setcommands = 0 
        self.__setcommands_cooldown = False
        with open("./data/blacklist.json",'r') as blacklistfile:
            self.__blacklist = load(blacklistfile)
    
    async def cooldown(self):
            await sleep(10)
            return False
        
    @commands.Cog.event()
    async def event_message(self, message):
        if message.echo:
           return 

        # filter
        if any(map(lambda x: x in self.__blacklist, message.content.split(" "))) and \
            not message.author.is_mod and not message.author.is_broadcaster:
                await message.channel.send(f"/timeout {message.author.name} 120 Said banned word")
            # await message.channel.send(f"/delete {message.tags['id']}")

def prepare(bot):
    bot.add_cog(Events(bot)) 