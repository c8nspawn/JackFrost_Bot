from twitchio.ext import commands

class Set(commands.Cog):
    def __init__(self, bot):
        self.__bot = bot

    @commands.command()
    async def set(self, ctx, *, args):
        if not ctx.author.is_mod: return

        args = args.split(' ')

        self.__bot.unload_module('cogs.setcommands')
        try:
            with open('./cogs/setcommands.py', 'r') as commands:
                setcommands = commands.readlines()
            
            if args[0] in self.commands:
                print("this happened")
                raise ...
            
            setcommands.insert(-3, f"\n    #{args[0]}\n    @commands.command()\n    async def {args[0]}(self, ctx):\n        await ctx.channel.send('{' '.join(args[1:])}')\n")
            setcommands = ''.join(setcommands)

            with open('./cogs/setcommands.py', 'w') as commands:
                commands.write(setcommands)

        except:...

        self.__bot.load_module('cogs.setcommands')

def prepare(bot):
    bot.add_cog(Set(bot))