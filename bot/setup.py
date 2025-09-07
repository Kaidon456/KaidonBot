import json
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!', intents=discord.Intents.all())

# Importacion del token
with open("./tokens.json") as file:
    data = json.load(file)

# Importacion de ID de canales
with open("./bot/channel.json") as file:
    ids = json.load(file)

# Creacion del Prefijo
client = commands.Bot(command_prefix = 'ENTER YOUR PREFIX', intents=discord.Intents.all())

# Eventos Discord
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='Kaidon456', url='https://www.twitch.tv/kaidon456'))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.')


# <---------------------------------------COMANDOS--------------------------------------->


# Inicializacion del Bot
client.run(data.get('BOT_ID'))