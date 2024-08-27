import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from dateutil import parser as dateparser
from datetime import datetime, timedelta

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

    # start reminder loop
    reminder_loop.start()

# Command: Add
@bot.command()
async def add(ctx, date=None, time=None, players: int=None, *, game=None):
    """Add a game to the schedule."""
    if date is None or time is None or players is None or game is None:
        await ctx.send("No arguments stated, command failed. Please provide all arguments: `!add <date> <time> <players> <game>`")
        return
    
    try:
        scheduled_datetime = dateparser.parse(f"{date} {time}")
    except ValueError:
        await ctx.send("Invalid time format. Please use a valid format, e.g., 'YYYY-MM-DD HH:MM' (2069-12-03 10:30PM)")
        return

    # Create a message for scheduling the game
    schedule_message = await ctx.send(f"React to this message to join the game: {game} at {date} {time} with {players} players needed!")

    # Store the scheduled game details
    scheduled_events[game.lower()] = {
        'datetime': scheduled_datetime,
        'players_needed': players,
        'participants': [],
        'message_id': schedule_message.id  # Store the message ID for future reference
    }

    # Add reactions to the scheduling message for user interaction
    await schedule_message.add_reaction('✅')  # You can add more reactions as needed

    await ctx.send(f"Added {game} to the schedule at {date} {time} with {players} players needed!")

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
            participant_id = payload.user_id
            if participant_id not in scheduled_events[game_name]['participants']:
                scheduled_events[game_name]['participants'].append(participant_id)
                print(f"{payload.member.name} joined {game_name}!")

# Event : Reaction Removed

@bot.event
async def on_raw_reaction_remove(payload):
    """Handle reaction removed event."""
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
            participant_id = payload.user_id
            if participant_id in scheduled_events[game_name]['participants']:
                scheduled_events[game_name]['participants'].remove(participant_id)
                print(f"User {payload.user_id} left {game_name}.")

# Reminder 

@tasks.loop(minutes=1)  # Adjust the interval as needed
async def reminder_loop():
    """Check for events starting within the next hour and send reminders."""
    now = datetime.now()
    for game, details in scheduled_events.items():
        if details['datetime'] > now and details['datetime'] <= now + timedelta(hours=1) and not details['reminder_sent']:
            message_id = details['message_id']
            channel_id = 1258684017943777330  # Replace with the appropriate channel ID where the message was sent
            channel = bot.get_channel(channel_id)
            if channel:
                try:
                    message = await channel.fetch_message(message_id)
                except discord.errors.NotFound:
                    # Handle case where message is not found (deleted)
                    print(f"Message for game {game} with ID {message_id} not found.")
                    continue
                
                if message:
                    participants = details['participants']
                    for participant_id in participants:
                        user = await bot.fetch_user(participant_id)  # Fetch the user object by ID
                        if user:
                            try:
                                await user.send(f"Reminder: Your game {game} is starting in 1 hour at {details['datetime'].strftime('%Y-%m-%d %H:%M')}")
                                details['reminder_sent'] = True  # Set reminder_sent flag to True after sending reminder
                            except discord.Forbidden:
                                print(f"Failed to send reminder to {user.name}: User has blocked DMs or bot cannot DM them.")

# Error handling for reminder loop

@reminder_loop.error
async def remind_loop_error(error):
    print(f"Error in the reminder loop: {error}")

# Command : list

@bot.command()
async def list(ctx):
    """List all scheduled games."""
    if scheduled_events:
        games_list = []
        for game, details in scheduled_events.items():
            print(f"Processing game: {game}, details: {details}")                     # Debug message for game and details
            try:
                participants = ', '.join([f"{(await bot.fetch_user(pid)).name}" for pid in details['participants']]) if details['participants'] else 'None'
                games_list.append(f"{game}: {details['datetime'].strftime('%Y-%m-%d %H:%M')} - {details['players_needed']} players, Participants: {participants}")
            except Exception as e:
                print(f"Error fetching user info for game: {game}, error: {e}")       # Debug message for errors
        
        await ctx.send(f"**Scheduled Games:**\n" + "\n".join(games_list))
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

# command : delete_all
@bot.command()
async def delete_all(ctx):
    """Deletes all messages in the channel (bot needs manage messages permission)."""
    if ctx.channel.permissions_for(ctx.author).manage_messages:
        await ctx.send('Deleting all messages in this channel...')
        try:
            await ctx.channel.purge(limit=None)
            await ctx.send('All messages deleted :sunglasses:')
        except discord.Forbidden:
            await ctx.send("I don't have permission to delete messages.")
    else:
        await ctx.send("You don't have permission to delete messages in this channel.")

# Run the bot with the specified token
bot.run(TOKEN)
