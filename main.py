import discord
from discord.ext import commands
import random

from dotenv import load_dotenv
from os import getenv

load_dotenv()
TOKEN = getenv("TOKEN")


class CustomHelpCommand(commands.HelpCommand):

    def __init__(self):
        super().__init__()
    
    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title='Help Page!',
            url='https://youtu.be/dQw4w9WgXcQ',
            description='Click here to access the stupid idiot bot help page!'
        )
        await self.get_destination().send(embed=embed)

bot = commands.Bot(command_prefix='.si ', help_command=CustomHelpCommand())

@bot.event
async def on_ready():
    print('Bot is online.')

@bot.command(aliases=['tess', 'less', 'bess'])
async def test(ctx):
    await ctx.send(embed=discord.Embed(
        description='this is a test command'
    ))

bot.load_extension("test")

bot.run(TOKEN)

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f'Logged in as {client.user}')

# @client.event
# async def on_message(message):
#     username = str(message.author).split('#')[0]
#     content = message.content
#     channel = message.channel.name

#     if message.author == client.user:
#         return
    
#     if channel == 'test-stupid-idiot':
#         if content[0:len(prefix)] == prefix:
#             command = content[len(prefix):]
#             if command == 'help':
#                 embed = discord.Embed(
#                     title='Help Page!',
#                     url='https://youtu.be/dQw4w9WgXcQ',
#                     description='Click here to access the stupid idiot bot help page!'
#                 )
#                 await message.channel.send(embed=embed)

            
#         else:
#             pass

# client.run(TOKEN)

