from twitchio.ext import commands

@commands.cog()
class Events:
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.event()
    async def event_message(self, message):
        if not message.echo:
            pass
            # filter goes here, use 

def prepare(bot):
    bot.add_cog(Events(bot))