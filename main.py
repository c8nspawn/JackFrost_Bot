from twitchio.ext import commands
from os import getenv,listdir
from dotenv import load_dotenv

load_dotenv()
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
        token=getenv("TOKEN"), 
        prefix=getenv("PREFIX"), 
        initial_channels=[getenv("STREAMER1"), getenv("STREAMER2")]
        )
                
        for filename in listdir('./cogs'):
                if filename.endswith('.py'):
                    self.load_module(f'cogs.{filename[:-3]}')
        
    @commands.command()
    async def load(self, ctx, *, args):
        if not ctx.author.is_mod: return
        self.load_module(f"cogs.{args}")

    @commands.command()
    async def unload(self, ctx, *, args):
        if not ctx.author.is_mod: return
        self.unload_module(f"cogs.{args}")

    @commands.command()
    async def reload(self, ctx, *, args):
        if not ctx.author.is_mod: return
        self.reload_module(f"cogs.{args}")

    @commands.command()
    async def _showcommands(self, ctx):
        if not ctx.author.is_mod: return
        print(self.commands)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')


bot = Bot()
bot.run()
