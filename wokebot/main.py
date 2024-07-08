import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import random

# Load environment variables
load_dotenv()

# Retrieve Discord token from environment
TOKEN = os.getenv('DISCORD_TOKEN')

# Define channel ID where bot will send messages
CHANNEL_ID = 1258684017943777330  # Replace with your channel ID

# Create intents
intents = discord.Intents.default()
intents.messages = True  # Enable message intent
intents.typing = False
intents.presences = True
intents.message_content = True

# Initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Send "All systems online" message to specified channel
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("*All systems online*")
    else:
        print("Failed to find channel :<")
    
    print(f'{bot.user} has connected to the server!')

# Event: Bot is disconnected
@bot.event
async def on_disconnect():
    print("Bot disconnected from Discord.")
    try:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send("*Powering off...*")
        else:
            print("Failed to find channel :<")
    except Exception as e:
        print(f"Error in on_disconnect: {e}")


# Event: Message received
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!'):
        command = message.content[1:].lower()
        
        if command == 'hello':
            response = "Hiiiiii!"
            await send_message(message, response)  # Send in the channel
        elif command == 'roll':
            response = str(random.randint(1, 6))
            await send_message(message, response)  # Send in the channel
        elif command == 'help':
            response = "`This is a help message that you can modify`"
            await send_message(message, response)  # Send in the channel
        else:
            response = handle_response(message)
            await send_message(message, response)  # Send in the channel

# Function to send messages (private or channel)
async def send_message(message, response):
    try:
        await message.channel.send(response)
    except discord.Forbidden:
        await message.channel.send("I don't have permission to send messages.")

# Function to handle responses based on message content
def handle_response(message) -> str:
    p_message = message.content.lower()

    if p_message == 'hello':
        return "Hi!"
    
    if p_message == '!help':
        return "`This is a help message that you can modify`"
    
    return "Sorry, I didn't understand that."

# Run the bot with the specified token
bot.run(TOKEN)
