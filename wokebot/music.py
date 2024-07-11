import discord
from discord.ext import commands
import yt_dlp
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

FFMPEG_OPTIONS = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
}
YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : True}

class MusicBot(commands.Cog):
    def __init__(self, client):
        self.client = client
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
            with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(f"ytsearch:{search}", download=False)
                if 'entries' in info:
                    info = info['entries'][0]
                url = info['url']
                title = info['title']
                self.queue.append((url, title))
                print(f"Added to queue: {title}")
                await ctx.send(f'Added to queue: **{title}**')
        if not ctx.voice_client.is_playing():
            await self.play_next(ctx)
            
    async def play_next(self, ctx):
        print("Attempting to play next song in queue")
        try:
            if self.queue:
                url, title = self.queue.pop(0)
                print(f"Now playing: {title}")
                source = await discord.FFmpegOpusAudio.from_probe(url, **FFMPEG_OPTIONS)  
                ctx.voice_client.play(source, after=lambda _:self.client.loop.create_task(self.play_next(ctx)))
                await ctx.send(f'Now playing **{title}**')
            elif not ctx.voice_client.is_playing():
                print("Queue is empty")
                await ctx.send("queue is empty!")
        except Exception as e:
            print(f"Error occurred: {e}")
            await ctx.send(f'Error: {e}')
            await ctx.voice_client.disconnect()
        

    @commands.command()
    async def skip(self, ctx):
        print("Received skip command")
        if ctx.voice_client and ctx.voice_client.is_playing():
            print("Skipping current song")
            ctx.voice_client.stop()
            await ctx.send("Skipped")

client = commands.Bot(command_prefix="!", intents=intents)

async def music():
    print("Starting bot")
    await client.add_cog(MusicBot(client))
    await client.start('redacted')

asyncio.run(music())
