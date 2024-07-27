import os
from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
from dateutil import parser as dateparser
from datetime import datetime, timedelta
import yt_dlp
import asyncio

# Load environment variables
load_dotenv()

# Retrieve Discord token from environment
TOKEN = os.getenv('DISCORD_TOKEN')

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.typing = False
intents.presences = True
intents.message_content = True
intents.voice_states = True

# Initialize bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Example scheduled events database (for demonstration)
scheduled_events = {}

# FFMPEG and YDL options
FFMPEG_OPTIONS = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
}
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}

class MusicBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.queue = []

    @commands.command()
    async def play(self, ctx, *, search):
        print("Received play command")
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
            print("User not in a voice channel")
            return await ctx.send("You're not in a voice channel!")
        if not ctx.voice_client:
            print("Connecting to voice channel")
            await voice_channel.connect()

        async with ctx.typing():
            print(f"Searching for: {search}")
            try:
                with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(f"ytsearch:{search}", download=False)
                    if 'entries' in info:
                        info = info['entries'][0]
                    url = info['url']
                    title = info['title']
                    self.queue.append((url, title))
                    print(f"Added to queue: {title}")
                    await ctx.send(f'Added to queue: **{title}**')
            except Exception as e:
                print(f"Error during yt_dlp search: {e}")
                await ctx.send(f"Error during search: {e}")
                
        if not ctx.voice_client.is_playing():
            await self.play_next(ctx)

    async def play_next(self, ctx):
        print("Attempting to play next song in queue")
        try:
            if self.queue:
                url, title = self.queue.pop(0)
                print(f"Now playing: {title}")
                source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)
                ctx.voice_client.play(source, after=lambda _: self.bot.loop.create_task(self.play_next(ctx)))
                await ctx.send(f'Now playing **{title}**')
            elif not ctx.voice_client.is_playing():
                print("Queue is empty")
                await ctx.send("Queue is empty!")
        except Exception as e:
            print(f"Error occurred while playing next song: {e}")
            await ctx.send(f"Error occurred: {e}")
            await ctx.voice_client.disconnect()

    @commands.command()
    async def skip(self, ctx):
        print("Received skip command")
        if ctx.voice_client and ctx.voice_client.is_playing():
            print("Skipping current song")
            ctx.voice_client.stop()
            await ctx.send("Skipped")
        else:
            print("No song is playing to skip")
            await ctx.send("No song is playing to skip")

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
        'organizer': ctx.author.name,
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
                        else:
                            print(f"User with ID {participant_id} not found.")
                else:
                    print(f"Message with ID {message_id} not found in channel {channel_id}.")

# Error handling for reminder loop
@reminder_loop.error
async def remind_loop_error(error):
    print(f"Error in the reminder loop: {error}")

# Command: List
@bot.command()
async def list(ctx):
    """List all scheduled games."""
    if scheduled_events:
        games_list = []
        for game, details in scheduled_events.items():
            print(f"Processing game: {game}, details: {details}")  # Debug message for game and details
            try:
                participants = ', '.join([f"{(await bot.fetch_user(pid)).name}" for pid in details['participants']]) if details['participants'] else 'None'
                organizer = await bot.fetch_user(details['organizer'])
                games_list.append(f"{game}: {details['datetime'].strftime('%Y-%m-%d %H:%M')} by {organizer.name} - {details['players_needed']} players, Participants: {participants}")
            except Exception as e:
                print(f"Error fetching user info for game: {game}, error: {e}")  # Debug message for errors
        
        await ctx.send(f"**Scheduled Games:**\n" + "\n".join(games_list))
    else:
        await ctx.send("No games scheduled.")

# Command: Remove
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

# Command: Delete All
@bot.command()
async def delete_all(ctx):
    """Deletes all messages in the channel (bot needs manage messages permission)."""
    if ctx.channel.permissions_for(ctx.author).manage_messages:
        await ctx.send('Deleting all messages in this channel...')
        try:
            await ctx.channel.purge(limit=None)
            await ctx.send('All messages deleted :sunglasses:')
        except discord.Forbidden:
            print("Bot does not have permission to delete messages.")
            await ctx.send("I don't have permission to delete messages.")
    else:
        print("User does not have permission to delete messages.")
        await ctx.send("You don't have permission to delete messages in this channel.")

# Setup hook to add MusicBot cog
async def setup_hook():
    await bot.add_cog(MusicBot(bot))

# Set the setup_hook method
bot.setup_hook = setup_hook

# Run the bot
bot.run(TOKEN)
