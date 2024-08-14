# bot.py
import os
import discord
from dotenv import load_dotenv

from discord.ext import commands

import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
print(TOKEN)
print(GUILD)

client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discoooooooooo!')


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


@bot.command(name="roll_dice", help='Simulates rolling dice.')
async def roll_dice(context, number_of_dice:int, number_of_sides:int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1))) 
        for _ in range (number_of_dice)
    ]
    await context.send(', '.join(dice))


bot.run(TOKEN)



# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#     print(f'here are the guilds that i\'m connected to {client.guilds}')
#     guild = discord.utils.get(client.guilds, name=GUILD)
#     print(
#         f'{client.user} is connected to the following guild: \n',
#         f'{guild.name}(id: {guild.id})'
#     )

#     print('guild members : ')
#     for member in guild.members:
#         print(f'{member}')


# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]
#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)
#     elif 'happy birthday' in message.content.lower():
#         await message.channel.send('Happy Birthday! 🎈🎉')
#     elif message.content == 'raise-exception':
#         raise discord.DiscordException
    

# @client.event
# async def on_error(event, *args, **kwargs):
#     with open('err.log', 'a') as f:
#         if event == 'on_message':
#             f.write(f'Unhandled message: {args[0]}\n')
#         else:
#             raise


# client.run(TOKEN)
