import os
import random
import discord
import json
import requests
from dotenv import load_dotenv

from discord.ext.commands import bot
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

@bot.command(name='staycool', help='Gives a helpful message')
async def cool(ctx):
    await ctx.send("Let's keep current events talk to a minimum")


bot.run(TOKEN)

client = discord.Client()

client.run(TOKEN)
