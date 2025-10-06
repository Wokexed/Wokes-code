import asyncio
import sys
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve Discord token from environment
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

AUDIO_FOLDER = os.path.join(os.path.dirname(__file__), "sounds")


@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    print(f"🎵 Ready to play sounds from: {os.path.abspath(AUDIO_FOLDER)}")

@bot.command()
async def join(ctx):
    """Join the user's current voice channel."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Joined **{channel}** ✅")
    else:
        await ctx.send("You're not in a voice channel!")

@bot.command()
async def help(ctx):
    """Display a list of available commands."""
    help_text = """
**🎵 Soundboard Bot Commands**

`!join` - Bot joins your current voice channel  
`!playrandom` - Plays a random sound from the sounds folder  
`!leave` - Bot leaves the voice channel  
`!help` - Shows this help message
"""
    await ctx.send(help_text)

@bot.command()
async def list(ctx):
    """List all available sound files."""
    if not os.path.exists(AUDIO_FOLDER):
        await ctx.send("⚠️ No sounds folder found!")
        return

    files = [f for f in os.listdir(AUDIO_FOLDER) if f.lower().endswith(('.mp3', '.wav'))]
    if not files:
        await ctx.send("⚠️ No sound files found in the folder.")
        return

    file_list = "\n".join(files)
    await ctx.send(f"**Available sounds:**\n{file_list}")


@bot.command()
async def play(ctx, *, name: str):
    """Play a specific sound by name."""
    vc = ctx.voice_client
    if not vc:
        await ctx.send("Use !join first so I can join your voice channel.")
        return

    path = os.path.join(AUDIO_FOLDER, name)
    if not os.path.isfile(path):
        await ctx.send(f"⚠️ File not found: {name}")
        return

    vc.stop()  # Stop anything currently playing

    # Custom volume for each file
    volume_levels = {
        "dimwit.mp3": 1.0,
        "faku.wav": 1.5,
        "urnigger.mp3": 2.0,
        "wadafuq.mp3": 1.0
    }
    volume = volume_levels.get(name, 1.0)
    audio_source = discord.FFmpegPCMAudio(path, options=f"-af volume={volume}")
    vc.play(audio_source)

    await ctx.send(f"🎶 Now playing: **{name}** at volume {volume}x")


@bot.command()
async def playrandom(ctx):
    """Play a random sound from the sounds folder."""
    vc = ctx.voice_client
    if not vc:
        await ctx.send("Use !join first so I can join your voice channel.")
        return

    # Get all valid sound files
    if not os.path.exists(AUDIO_FOLDER):
        await ctx.send("⚠️ No sounds folder found!")
        return

    files = [f for f in os.listdir(AUDIO_FOLDER) if f.lower().endswith(('.mp3', '.wav'))]

    if not files:
        await ctx.send("⚠️ No sound files found in the folder.")
        return

    chosen = random.choice(files)
    path = os.path.join(AUDIO_FOLDER, chosen)

    vc.stop()  # Stop anything currently playing

    volume_levels = {
        "dimwit.mp3": 1.0,
        "faku.wav": 1.2,
        "urnigger.mp3": 2.0,
        "wadafuq.mp3": 1.0
    }

    # Default volume is 1.0 if file not listed
    volume = volume_levels.get(chosen, 1.0)
    audio_source = discord.FFmpegPCMAudio(path, options=f"-af volume={volume}")
    vc.play(audio_source)

    await ctx.send(f"🎶 Now playing: **{chosen}** at volume {volume}x")

@bot.command()
async def leave(ctx):
    """Disconnect from voice channel."""
    vc = ctx.voice_client
    if vc:
        await vc.disconnect()
        await ctx.send("👋 Left the voice channel.")
    else:
        await ctx.send("I'm not connected to a voice channel.")

bot.run(TOKEN)
