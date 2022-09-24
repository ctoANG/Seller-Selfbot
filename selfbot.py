from discord.ext import commands
from datetime import datetime
import json
from pystyle import Write, Colors, Add, Center, Box
import os
from os import system

system("title " + "By ANG Selfbot Started")
os.system('cls')
config = json.load(open("config.json"))
Write.Print(color=Colors.white_to_blue, text=Center.XCenter(text=config['client']['ascii']), interval=0)
client = commands.Bot(command_prefix='!', self_bot=True, help_command=None)


@client.command()
async def pay(ctx: commands.Context, type: str, amt: int):
    await ctx.message.delete()
    await ctx.send(f"""
```ini
[ {type} Invoice ]

Checkout: ${amt}
Method: {type}
Payment: {config['wallets'][f'{type}']}
```
""")


@client.command()
async def vouch(ctx: commands.Context, type: str):
    await ctx.message.delete()
    await ctx.send(f"""
```ini
[ Vouch ]

Thread: {config['vouch']['URL']}

How: Go the the URL then click the green vouch button on the right. Fill in all the fields and done!

Cost: ${type}
```
""")


@client.command()
async def sig(ctx: commands.Context):
    await ctx.message.delete()
    await ctx.send(f"""
```ini
[ Signature ]

[align=center][url={config['signature']['URL']}][img]{config['signature']["IMG"]}[/img][/url]
[color=#ffffff][size=x-large]Bought by @{config['signature']['USERNAME']} | On {datetime.today().strftime('%Y-%m-%d')}[/size][/color][/align]


How: 
1. Go to the change signature page 
2. Click the gear icon all the way on the right 
3. Paste the code above ^
4. Click the gear icon again you should now see the signature.
5. Click Enable my signature in all of my existing posts.
6. Done!
```
""")


client.run(config['client']['token'], bot=False)
