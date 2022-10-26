from twitchio.ext import commands

import asyncio
import os
import sys

from dotenv import load_dotenv

load_dotenv()

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        
        super().__init__(token=os.getenv("TOKEN"), prefix='?', initial_channels=['lilc8n'])
        

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()