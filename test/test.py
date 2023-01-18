fname = 'generated.py'
command = "bruh"

with open(fname, 'r') as f:
    bruh = f.readlines()

bruh.insert(-3, f"\n@commands.command()\nasync def {command}(self, ctx):\n   ctx.channel.send('bruh')\n")
bruh = ''.join(bruh)

with open(fname, 'w') as f:
    f.write(bruh)



# print(bruh)
