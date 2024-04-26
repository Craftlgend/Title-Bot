import discord 
TOKEN = "MTIzMjc2MTkxNzYyNjM4ODcyMg.G7BEBt.k4fjN3--Ho04RI7h-SRHVhplnego3tpb6OFFTk"
client = discord.Client(intents=discord.Intents.default())
@client.event
async def on_ready():
    print(f'{client.user} ist mit folgenden Servern verbunden:\n')
    for server in client.guilds:
        print(f'{server.name}(id: {server.id})')