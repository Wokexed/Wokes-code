import os

from dotenv import load_dotenv
from discord import Intents, Client, Message

import discord

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = 1258684017943777330

intents = discord.Intents.default()
intents.typing = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("*All systems online*")
    else:
        print("Failed to find channel :<")
    print(f'{client.user} has connected to the server!')

if TOKEN:
    client.run(TOKEN)
else:
    print("ERROR: Discord token not found in environment variables.")
