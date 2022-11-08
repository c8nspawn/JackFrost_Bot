from twitchio.ext import commands

import os
import sys

from dotenv import load_dotenv

load_dotenv()
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
        token=os.getenv("TOKEN"), 
        prefix=os.getenv("PREFIX"), 
        initial_channels=[os.getenv("STREAMER")]
        )
                
        for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    self.load_module(f'cogs.{filename[:-3]}')
        
        
    @commands.command()
    async def load(self, ctx, *, args):
        if not ctx.author.is_mod: return
        print(args)
        self.load_module(f"cogs.{args}")
                
    @commands.command()
    async def unload(self, ctx, *, args):
        if not ctx.author.is_mod: return
        print(args)
        self.unload_module(f"cogs.{args}")

    @commands.command()
    async def reload(self, ctx, *, args):
        if not ctx.author.is_mod: return
        print(args)
        self.reload_module(f"cogs.{args}")

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')


bot = Bot()
bot.run()
