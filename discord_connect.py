from interactions import Client, Intents, OptionType, SlashContext, SlashCommandChoice, slash_option, slash_command
from database import Player, session
from algorythm import main_algorythm
from threading import Thread
from os import path



TOKEN = 'MTIzMjc2MTkxNzYyNjM4ODcyMg.G7BEBt.k4fjN3--Ho04RI7h-SRHVhplnego3tpb6OFFTk'


bot = Client(intents=Intents.DEFAULT)
async def on_command_error(ctx, error):
    # Handle your errors here
    if title(error):
        await ctx.send('Please type the command correctly. Type /hlp for more information.')
        return

    else:
        # All unhandled errors will print their original traceback
        print ('error')
        return

bot.on_error = on_command_error


#command structure
@slash_command(name="title", description = "gives you the requested title")
@slash_option(
    name="title",
    description="The title to give",
    required=True,
    opt_type=OptionType.STRING,
    choices=[
        SlashCommandChoice(name="Duke", value='Duke'),
        SlashCommandChoice(name="Scientist", value='Scientist'),
        SlashCommandChoice(name="Architect", value="Architect"),
        SlashCommandChoice(name="Justice", value="Justice")
    ]
)
@slash_option(
    name="kingdom",
    description="the kingdom your in.",
    required= True,
    opt_type= OptionType.STRING,
    choices=[
        SlashCommandChoice(name="Home Kingdom", value="hk"),
        SlashCommandChoice(name="Lost Kingdom", value= "lk")
        ]
)
@slash_option(
    name="x_coordinate",
    description="The x_coordinate of the location.",
    required=True,
    opt_type=OptionType.INTEGER
)
@slash_option(
    name="y_coordinate",
    description="The y_coordinate of the location.",
    required=True,
    opt_type=OptionType.INTEGER
)


#acts when the command is run
async def title(ctx: SlashContext, title: str, kingdom: str, x_coordinate: int,  y_coordinate: int):


    # Check if the player exists in the database
    player = session.query(Player).filter_by(discord_id=str(ctx.author.mention)).first()
    if player:
        # If the player exists, update their data
        player.discord_name = str(ctx.author)
        player.x_coord = x_coordinate
        player.y_coord = y_coordinate
        player.kingdom_type = kingdom
        player.title = title.title()  # Capitalize the first letter
        
    else:
        # If the player doesn't exist, create a new record
        new_player = Player(
            discord_id=str(ctx.author.mention),
            discord_name=str(ctx.author),
            x_coord=x_coordinate,
            y_coord=y_coordinate,
            kingdom_type=kingdom,
            title=title.title()
        )
        session.add(new_player)
    
    # Commit changes to the database
    session.commit()
    print ('Successfully added to database')
    await ctx.send(f"Title '{title.title()}' assigned to {ctx.author.mention} at coordinates ({x_coordinate}, {y_coordinate}) in the {kingdom} kingdom.")
    if path.isfile("Running.pid") == False:
        Thread(target=main_algorythm).start() #start the algo that gives the titles


bot.start(TOKEN)


