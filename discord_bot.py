import discord
from discord.ext import commands
#import duke
import traceback
import sys

TOKEN = ('MTIzMjc2MTkxNzYyNjM4ODcyMg.G7BEBt.k4fjN3--Ho04RI7h-SRHVhplnego3tpb6OFFTk')
GUILD={'PRf0 Academy'}

intents = discord.Intents.default()
intents.message_content = True




#error-handling
async def on_command_error(ctx, error):
    # Handle your errors here
    if title(error):
        print ('error')
        return

    else:
        # All unhandled errors will print their original traceback
        print ('error')
        return





bot = commands.Bot(command_prefix='/', intents=intents)
bot.on_command_error = on_command_error

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
async def title(ctx, str, kd:str, x:int, y:int):
    if str=='duke':
        await ctx.send('Wait, we are checking the given position...')
        print (ctx.author.id)
        print (ctx.author.id)
        return
    
    elif str=='justice':
        await ctx.send('Wait, we are checking the given position...')
        return
    
    elif str=='architect':
        await ctx.send('Wait, we are checking the given position...')
        return
    
    elif str=='scientist':
        await ctx.send('Wait, we are checking the given position...')
        return
    
    else :
        await ctx.send('Please give a valid title. Type /help for mor information')
        return
    
@bot.command(name='hlp')
async def hlp(ctx):
    await ctx.send('To get a title, type the following command:\n /title (duke, justice, architect or scientist) (Lost Kingdom=lk, Home Kingdom=hk) x-coordinate, y-coordinate')
    return






bot.run(TOKEN)

