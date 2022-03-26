from ast import alias
from http import client
import discord
from discord.ext import commands
import random

TOKEN = 'OTUzNTI3MDQwMDcyNjM0MzY5.YjF3Qg.BS8SHiZiryl5F0LnOVWzYfLXi1I'

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

client = commands.Bot(command_prefix='.si ', help_command=CustomHelpCommand())

@client.event
async def on_ready():
    print('Bot is online.')

@client.command(aliases=['tess', 'less', 'bess'])
async def test(ctx):
    await ctx.send(embed=discord.Embed(
        description='this is a test command'
    ))

client.run(TOKEN)

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

