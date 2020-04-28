import os
import discord
from dotenv import load_dotenv
import discord.ext.commands
from discord.ext.commands import bot
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
client = discord.Client()

# https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='staycool', help='Gives a helpful message')
async def cool(ctx):

    await ctx.send("Let's keep current events talk to a minimum")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    delibird_says = "https://tenor.com/SDYj.gif"

    if message.content == 'bird' or message.content == 'birb':
        response = delibird_says
        await message.channel.send(response)
    await bot.process_commands(message)

bot.run(TOKEN)
#client.run(TOKEN)
