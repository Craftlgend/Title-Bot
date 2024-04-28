import discord
from discord.ext import commands
from database import Player, session

import traceback
import sys

TOKEN = 'MTIzMjc2MTkxNzYyNjM4ODcyMg.G7BEBt.k4fjN3--Ho04RI7h-SRHVhplnego3tpb6OFFTk'
GUILD = 'PRf0 Academy'



# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True




#error-handling
async def on_command_error(ctx, error):
    # Handle your errors here
    if title(error):
        await ctx.send('Please type the command correctly. Type /help for more information.')
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

@bot.command(name='title')
async def title(ctx, title_str: str, kingdom_type: str, x: int, y: int):
    valid_titles = ['duke', 'justice', 'architect', 'scientist']
    if title_str.lower() not in valid_titles:
        await ctx.send('Please provide a valid title. Type /hlp for more information.')
        return

    # Check if the player exists in the database
    player = session.query(Player).filter_by(discord_id=str(ctx.author.id)).first()
    if player:
        # If the player exists, update their data
        player.discord_name = str(ctx.author)
        player.x_coord = x
        player.y_coord = y
        player.kingdom_type = kingdom_type
        player.title = title_str.title()  # Capitalize the first letter
    else:
        # If the player doesn't exist, create a new record
        new_player = Player(
            discord_id=str(ctx.author.id),
            discord_name=str(ctx.author),
            x_coord=x,
            y_coord=y,
            kingdom_type=kingdom_type,
            title=title_str.title()
        )
        session.add(new_player)
    
    # Commit changes to the database
    session.commit()

    await ctx.send(f"Title '{title_str.title()}' assigned to {ctx.author.display_name} at coordinates ({x}, {y}) in the {kingdom_type} kingdom.")




bot.run(TOKEN)
