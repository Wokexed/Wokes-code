import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

AUDIO_FOLDER = "sounds"  # Folder that stores all your sound files (e.g., .mp3, .wav)

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
    vc.play(discord.FFmpegPCMAudio(path))
    await ctx.send(f"🎶 Now playing: **{chosen}**")

@bot.command()
async def leave(ctx):
    """Disconnect from voice channel."""
    vc = ctx.voice_client
    if vc:
        await vc.disconnect()
        await ctx.send("👋 Left the voice channel.")
    else:
        await ctx.send("I'm not connected to a voice channel.")

bot.run("YOUR_BOT_TOKEN")
