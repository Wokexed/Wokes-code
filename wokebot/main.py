import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.messages = True  # Enable message content intent
intents.typing = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = 1258684017943777330  # Replace with your channel ID

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Send message to specified channel
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("*All systems online*")
    else:
        print("Failed to find channel :<")
    
    print(f'{bot.user} has connected to the server!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!'):
        command = message.content[1:].lower()
        
        if command == 'hello':
            response = "Hiiiiii!"
            await send_message(message, response, is_private=False)  # Send in the channel
        elif command == 'roll':
            response = str(random.randint(1, 6))
            await send_message(message, response, is_private=False)  # Send in the channel
        elif command == 'help':
            response = "`This is a help message that you can modify`"
            await send_message(message, response, is_private=False)  # Send in the channel
            response = handle_response(message)
            await send_message(message, response, is_private=False)  # Send in the channel

async def send_message(message, response, is_private=False):
    try:
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except discord.Forbidden:
        await message.channel.send("I don't have permission to send messages privately to you.")

def handle_response(message) -> str:
    p_message = message.content.lower()

    if p_message == 'hello':
        return "Hi!"
    
    if p_message == '!help':
        return "`This is a help message that you can modify`"
    
    return "Sorry, I didn't understand that."

bot.run(TOKEN)
