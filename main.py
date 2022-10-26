from twitchio.ext import commands

import asyncio
import os
import sys

from dotenv import load_dotenv

load_dotenv()


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=os.getenv("TOKEN"), prefix='?', initial_channels=['lilc8n'])
                
        for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    self.load_module(f'cogs.{filename[:-3]}')
                

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')


bot = Bot()
bot.run()
