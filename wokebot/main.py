import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from dateutil import parser as dateparser

# Load environment variables
load_dotenv()

# Retrieve Discord token from environment
TOKEN = os.getenv('DISCORD_TOKEN')

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable message intent
intents.typing = False
intents.presences = True
intents.message_content = True

# Initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Example scheduled events database (for demonstration)
scheduled_events = {}

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    print('Bot is ready to handle commands!')

# Command: Add
@bot.command()
async def add(ctx, time=None, players: int=None, *, game=None):
    """Add a game to the schedule."""
    if time is None or players is None or game is None:
        await ctx.send("No arguments stated, command failed. Please provide all arguments: `!add <time> <players> <game>`")
        return
    
    try:
        scheduled_time = dateparser.parse(time).time()
    except ValueError:
        await ctx.send("Invalid time format. Please use a valid time format, e.g., 'HH:MM'.")
        return

    # Create a message for scheduling the game
    schedule_message = await ctx.send(f"React to this message to join the game: {game} at {time} with {players} players needed!")

    # Store the scheduled game details
    scheduled_events[game.lower()] = {
        'time': scheduled_time,
        'organizer': ctx.author.name,
        'players_needed': players,
        'participants': [],
        'message_id': schedule_message.id  # Store the message ID for future reference
    }

    # Add reactions to the scheduling message for user interaction
    await schedule_message.add_reaction('✅')  # You can add more reactions as needed

    await ctx.send(f"Added {game} to the schedule at {time} with {players} players needed!")

# Event: Reaction Added
@bot.event
async def on_raw_reaction_add(payload):
    """Handle reaction added event."""
    if payload.user_id == bot.user.id:
        return

    channel = await bot.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    if message.author == bot.user:
        game_name = None
        for game, details in scheduled_events.items():
            if details['message_id'] == message.id:
                game_name = game
                break
        
        if game_name:
            scheduled_events[game_name]['participants'].append(payload.member.name)
            print(f"{payload.member.name} joined {game_name}!")

# Command : list

@bot.command()
async def list(ctx):
    """List all scheduled games."""
    if scheduled_events:
        games_list = "\n".join([f"{game}: {details['time']} by {details['organizer']} - {details['players_needed']} players, Participants: {', '.join(details['participants'])}" for game, details in scheduled_events.items()])
        await ctx.send(f"**Scheduled Games:**\n{games_list}")
    else:
        await ctx.send("No games scheduled.")

# command : remove

@bot.command()
async def remove(ctx, *, game=None):
    """Remove a game from the schedule."""
    if game is None or game == "":
        await ctx.send("Please specify which game to remove.")
    elif game in scheduled_events:
        del scheduled_events[game.lower()]
        await ctx.send(f"Removed {game} from the schedule.")
    else:
        await ctx.send(f"{game} is not scheduled.")

# Run the bot with the specified token
bot.run(TOKEN)
