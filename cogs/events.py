from twitchio.ext import commands
import json


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.blacklist = json.load(open("./data/blacklist.json",'r'))

    @commands.Cog.event()
    async def event_message(self, message):
        if not message.echo:
            pass
            # filter goes here, use 

        if any(map(lambda x: x in self.blacklist, message.content.split(" "))):
            await message.channel.send(f"/delete {message.tags['id']}")



def prepare(bot):
    bot.add_cog(Events(bot))