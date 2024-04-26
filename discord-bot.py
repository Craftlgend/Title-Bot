import discord
from discord.ext import commands

TOKEN = ('MTIzMjc2MTkxNzYyNjM4ODcyMg.G7BEBt.k4fjN3--Ho04RI7h-SRHVhplnego3tpb6OFFTk')
GUILD={'PRf0 Academy'}

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )




@bot.command(name= 'title')
async def title(ctx, str, kd:str, x:int, y:int)
    if str=='duke':
        await ctx.send('You were added  to the waitlist for Duke')
    
    elif str=='justice':
        await  ctx.send("You were added to the waitlist  for Justice")
    
    elif str=='architect':
        await  ctx.send("You were added to the waitlist  for Architect")
        return
    
    elif str=='scientist':
        await  ctx.send('You were added to the waitlist  for Scientist')
        return
    
    else :
        await ctx.send('Please give a valid title')

bot.run(TOKEN)

