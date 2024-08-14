# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random
import yt_dlp as youtube_dl
import glob

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up the bot with a command prefix
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

# Brooklyn 99 Quote Command
@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(context):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    response = random.choice(brooklyn_99_quotes)
    await context.send(response)

# Roll Dice Command
@bot.command(name="roll_dice", help='Simulates rolling dice.')
async def roll_dice(context, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1))) 
        for _ in range(number_of_dice)
    ]
    await context.send(', '.join(dice))

# Join Voice Channel Command
@bot.command(name='join', help='The bot joins the voice channel')
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You're not connected to a voice channel.")

# Leave Voice Channel Command
@bot.command(name='leave', help='The bot leaves the voice channel')
async def leave(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("I'm not in a voice channel!")

# Play Local Audio File Command
@bot.command(name='play_local', help='Plays a local audio file')
async def play_local(ctx, filename: str):
    if not ctx.voice_client:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You're not connected to a voice channel.")
            return

    # Check if the file exists
    if os.path.isfile(filename):
        # Stop any current playing audio
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        # Play the audio file
        ctx.voice_client.play(discord.FFmpegPCMAudio(source=filename))

        await ctx.send(f'Now playing: {filename}')
    else:
        await ctx.send(f'File not found: {filename}')


@bot.command(name='play', help='Downloads and plays a song from YouTube')
async def play(ctx, *, url: str):
    if not ctx.voice_client:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("You're not connected to a voice channel.")
            return

    download_dir = 'downloads/'

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Save file to 'downloads' directory
        'playlist_items': '1',  # Only download the first video in a playlist
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        # Get the file path
        file_path = ydl.prepare_filename(info)
        
        # Check if 'Mix - ' exists in the filename and handle both cases
        directory, filename = os.path.split(file_path)
        base, ext = os.path.splitext(filename)
        base_without_mix = base.replace('Mix - ', '')
         # Find the actual file using glob within the specified directory
        print(base)
        matching_files = glob.glob(f"{base_without_mix}.*", root_dir=download_dir)
        if not matching_files:
            await ctx.send("Downloaded file not found.")
            return
        
        file_path = os.path.join(download_dir, matching_files[0])

    # Play the correct file
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()

    audio_source = discord.FFmpegPCMAudio(file_path)
    ctx.voice_client.play(audio_source)

    await ctx.send(f"Now playing: {info['title']}")

# Stop Music Command
@bot.command(name='stop', help='Stops the music')
async def stop(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()
    await ctx.send("Music stopped.")

bot.run(TOKEN)
