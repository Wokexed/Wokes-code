import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from dateutil import parser as dateparser
import youtube_dl
import yt_dlp
import asyncio

# Load environment variables
load_dotenv()

# Retrieve Discord token from environment
TOKEN = os.getenv('DISCORD_TOKEN')

# Define intents
intents = discord.Intents.default()
intents.messages = True  # Enable message intent
intents.typing = True
intents.presences = True
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.voice_states = True
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

# !add 
@bot.command()
async def add(ctx, time=None, players: int=None, *, game=None):
    """Add a game to the schedule."""
    if time is None or players is None or game is None:
        await ctx.send("No arguments stated, command failed. Please provide all arguments: `!add <time> <players> <game>`")
        return
    
    try:
        scheduled_time = dateparser.parse(time).time()
    except ValueError:
        await ctx.send("Invalid time format. Please use a valid time format, e.g., 'HH:MM', for example 08:39PM ")
        return

    # Create a message for scheduling the game
    schedule_message = await ctx.send(f"React to this message to join the game: {game} at {time} with {players} players needed!")
    
    # Store the scheduled game details including the message object
    scheduled_events[game.lower()] = {
        'time': scheduled_time,
        'organizer': ctx.author.name,
        'players_needed': players,
        'participants': [],  # Initialize empty list for participants
        'message': schedule_message  # Store the message object
    }

    # Add reactions to the scheduling message for user interaction
    await schedule_message.add_reaction('✅')  # You can add more reactions as needed

    await ctx.send(f"Added {game} to the schedule at {time} with {players} players needed!")

# Reaction Added
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
            if details['message'].id == message.id:
                game_name = game
                break
        
        if game_name:
            # Add participant to the list
            member = payload.member
            if member:
                username = member.display_name  # Change this to member's username or identifier as needed
                if username not in scheduled_events[game_name]['participants']:
                    scheduled_events[game_name]['participants'].append(username)

            # Update the message content with current participants
            participants = ', '.join(scheduled_events[game_name]['participants'])
            await message.edit(content=f"React to this message to join the game: {game_name} at {details['time']} with {details['players_needed']} players needed!\nParticipants: {participants}")

            print(f"{payload.member.name} joined {game_name}!")

# reaction removed

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
            if details['message'].id == message.id:
                game_name = game
                break
        
        if game_name:
            guild = bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            
            if member:
                username = member.display_name  # Change this to member's username or identifier as needed
                if username in scheduled_events[game_name]['participants']:
                    scheduled_events[game_name]['participants'].remove(username)

            # Update the message content with current participants
            participants = ', '.join(scheduled_events[game_name]['participants']) if scheduled_events[game_name]['participants'] else 'None'
            await message.edit(content=f"React to this message to join the game: {game_name} at {details['time']} with {details['players_needed']} players needed!\nParticipants: {participants}")

# !list
@bot.command()
async def list(ctx):
    """List all scheduled games."""
    if scheduled_events:
        games_list = []
        for game, details in scheduled_events.items():
            participants = ', '.join(details['participants']) if details['participants'] else 'None'
            games_list.append(f"{game}: {details['time']} by {details['organizer']} - {details['players_needed']} players, Participants: {participants}")
        
        await ctx.send(f"**Scheduled Games:**\n" + "\n".join(games_list))
    else:
        await ctx.send("No games scheduled.")

# !remove
@bot.command()
async def remove(ctx, *, game=None):
    """Remove a game from the schedule."""
    if game is None or game == "":
        await ctx.send("Please specify which game to remove.")
    elif game.lower() in scheduled_events:
        del scheduled_events[game.lower()]
        await ctx.send(f"Removed {game} from the schedule.")
    else:
        await ctx.send(f"{game} is not scheduled.")

# music player 

FFMPEG_OPTIONS = {'options' : 'vn'}
YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : True}

class MusicBot(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue = []

        @commands.command()
        async def play(self, ctx, *, search):
            voice_channel = ctx.author.voice.channel if ctx.author.voice else None
            if not voice_channel:
                return await ctx.send("You're not in a voice channel!")
            if not ctx.voice_client:
                await voice_channel.connect()

            async with ctx.typing():
                with yt_dlp.YoutubeDl(YDL_OPTIONS) as ydl:
                    info = ydl.extract_info(f"ytsearch:{search}", download=False)
                    if 'entries' in info:
                        info = info['entries'][0]
                    url = info['url']
                    title = info['title']
                    self.queue.append((url, title))
                    await ctx.send(f'Added to queue: **{title}**')
            if not ctx.voice_client.is_playing():
                await self.play_next(ctx)
    async def play_next(self, ctx):
        if self.queue:
            url, title = self.queue.pop(0)
            source = await discord.FFmpeg0pusAudio.from_probe(url, **FFMPEG_OPTIONS)  
            ctx.voice_client.play(source, after=lambda _:self.client.loop.create_task(self.play_next(ctx)))
            await ctx.send(f'Now playing **{title}**')
        elif not ctx.voice_client.is_playing():
            await ctx.send("queue is empty!")

    @commands.command()
    async def skip(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("Skipped")

client = commands.Bot(command_prefix="!", intents=intents)

async def main():
    await client.add_cog(MusicBot(client))
    await client.start('TOKEN')

# Run the bot with the specified token
bot.run(TOKEN)
