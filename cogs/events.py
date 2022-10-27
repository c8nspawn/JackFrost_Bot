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

        offense_score = {
            1:["this", "is", "a", "one"],
            2:["a", "two"]
        }

        def score_assigner(message):
            if any(map(lambda x: message in x, [e for e in offense_score.values()])):
                print('yeah')
        
        score_assigner("this")



def prepare(bot):
    bot.add_cog(Events(bot))