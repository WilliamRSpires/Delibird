import os
import discord
import random
import csv
import json
import gspread
from dotenv import load_dotenv
import discord.ext.commands
from discord.ext.commands import bot
from discord.ext import commands
from discord.utils import get

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
guild = os.getenv('DISCORD_GUILD')
google_sheets = os.getenv('Google_Sheets_Key')
secret_server_id = os.getenv('Secret_Server')
home_server_id = int(secret_server_id)
client = discord.Client()
gc = gspread.service_account(filename='google_sheets_creds.json')
sh = gc.open_by_key(google_sheets)
worksheet = sh.sheet1

def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild.id == guild_id
    return commands.check(predicate)
# https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client

def find_code(name,platform):
    row_cell = worksheet.find(name)
    column_cell = worksheet.find(platform)
    row = row_cell.row
    column = column_cell.col
    if worksheet.cell(row,column).value is "":
        return "This user does not have a code in the system"
    else: 
        return worksheet.cell(row,column).value

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='staycool', help='Gives a helpful message')
@is_in_guild(home_server_id)
async def cool(ctx):
    await ctx.send("Take current events talk to #current_events_lounge")

@bot.command(name='newprofile', help="give me a nickname and I'll make you a new profile")
async def newprofile(ctx,arg1):
    id_list = worksheet.col_values(1)
    user_id = ctx.message.author.id
    id_string = str(user_id)
    lowercase_user = arg1.lower()
    if id_string in id_list:
       message = "You're already in the database. Please try a different command"
    else:     
        user = [id_string, arg1, lowercase_user]
        worksheet.append_row(user)
        message = "You've been added to the database, thank you {}".format(arg1)
    await ctx.send(message)

@bot.command(name='nicknames', help='Gives you a list of nicknames')
async def nicknames(ctx):
    nicknamelist = worksheet.col_values(2)[1:]
    await ctx.send(nicknamelist)

@bot.command(name='pogo', help='gives pogo friend codes in a copypaste friendly format')
async def pogo(ctx, arg1):
    friend_code = find_code(arg1.lower(),'pogo')   
    await ctx.send(friend_code)

@bot.command(name='switch', help='Get your switch codes here')
async def switch(ctx, arg1):
    switch = find_code(arg1.lower(),'switch')  
    await ctx.send(switch)

@bot.command(name='xbox', help='Get your Xbox Usernames here')
async def xbox(ctx, arg1):
    xbl = find_code(arg1.lower(),'xbox')  
    await ctx.send(xbl)

@bot.command(name='playstation', help='Get your PSN names here')
async def playstation(ctx, arg1):
    PSN = find_code(arg1.lower(),'playstation')  
    await ctx.send(PSN)

@bot.command(name='AltOne', help='Get Pogo Alt codes here')
async def firstAlt(ctx, arg1):
    friend_code = find_code(arg1.lower(),'alt1') 
    await ctx.send(friend_code)

@bot.command(name='AltTwo', help='Get Secondary Alt codes here')
async def SecondAlt(ctx, arg1):
    friend_code = find_code(arg1.lower(),'alt2') 
    await ctx.send(friend_code)

@bot.command(name='AltThree', help='Get your Third Alt Codes here')
async def ThirdAlt(ctx, arg1):
    friend_code = find_code(arg1.lower(),'alt3') 
    await ctx.send(friend_code)

@bot.command(name='notsafe', help="reminds people to keept talk appropriate-ish")
@is_in_guild(home_server_id)
async def safe(ctx):
    await ctx.send("Let's take adult content elsewhere, like #freeza_lounge or DM's")

@bot.command(name='set', help='Enter switch, xbox, pogo, alt1, alt2, alt3, or playstation followed by your info')
async def set(ctx, arg1, arg2):
    ID=ctx.author.id
    USERID=str(ID)
    platform = arg1.lower()
    cell = worksheet.find(USERID)
    row_number = cell.row
    if platform not in worksheet.row_values(1):
        info = "Currently this platform is not supported. Please check for spelling errors or use the help command to find your error."
    elif platform == 'nickname':
        nickname_cell = worksheet.find('nickname')
        nickname_lower_case = worksheet.find('nickname_lower')
        col_number = nickname_cell.col
        second_column = nickname_lower_case.col
        lower_case_name = arg2.lower()
        worksheet.update_cell(row_number,col_number,arg2)
        worksheet.update_cell(row_number,second_column,lower_case_name)
        info = 'Your {} information has been updated {} is the new value.'.format(platform,arg2)
    else:
        platform_cell = worksheet.find(platform)
        col_number = platform_cell.col
        worksheet.update_cell(row_number,col_number,arg2)
        info = 'Your {} information has been updated {} is the new value.'.format(platform,arg2)
    await ctx.send(info)

@bot.command(name='friendship', help='Make two things best friends')
async def args(ctx, arg1, arg2):
    if arg1.lower() == 'clemson' or arg2.lower() == 'clemson':
        statement='Clemson is Trash'
    else:
        statement='{} and {} are best friends'.format(arg1, arg2)
    await ctx.send(statement)

@bot.command(name='friendshipover', help='End your friendship')
async def friendshipover(ctx, arg1, arg2):
    statement='Friendship over with {}, {} is my new best friend'.format(arg1, arg2)
    await ctx.send(statement)

@bot.command(name='bird', help='Get wonderful gif of Delibird')
async def Delibird(ctx):
    delibird_gifs = ['https://31.media.tumblr.com/2453c1bcf3b7081c6e183441591560d1/tumblr_mre9ce7ILY1se9g54o1_500.gif',
    'https://31.media.tumblr.com/tumblr_ma7tfuO7Er1qike2eo1_500.gif',
    'https://66.media.tumblr.com/e42e5f24841422abd1672d1387e66e1b/tumblr_nssazjoJRx1ux6juuo6_400.gif',
    'https://66.media.tumblr.com/1513a8963e1a395bab6eae7dfdcecf40/tumblr_nsd701CkFe1rpq6b5o1_400.gif',
    'https://66.media.tumblr.com/0ca9bac2eb25a7977c7eae9dc27ec7b2/tumblr_mf321sKcZd1rv3hlso1_500.gif',
    'https://66.media.tumblr.com/282b967349293f7ca39779ea20b5c8fc/tumblr_nzvk2awlpm1sox2ufo1_250.gif',
    'https://66.media.tumblr.com/tumblr_m0w12eglVE1qd87hlo1_500.gif',
    'https://66.media.tumblr.com/4e0ff42b26c06bc06a6b30bc533ce24a/tumblr_nsvpclFYbA1ttdkobo2_400.gif']
    delibird = random.choice(delibird_gifs)
    await ctx.send(delibird)

@bot.command(name='hello', help='Get a friendly greeting')
async def hello(ctx):
    ID=ctx.author.id
    USERID=str(ID)
    cell = worksheet.find('nickname')
    row_cell = worksheet.find(USERID)
    row = row_cell.row
    column = cell.column
    name = worksheet.cell(row,column).value
    await ctx.send("hello "+ name)

@bot.command(pass_context=True, name='fight', help="show you're available to battle")
@is_in_guild(home_server_id)
async def fight(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="fight_me")
    await member.add_roles(role)

@bot.command(pass_context=True, name='notice', help="sign up to be notified when someone tags Senpai") 
@is_in_guild(home_server_id)
async def notice(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="SENPAI")
    await member.add_roles(role)

@bot.command(pass_context=True, name='hide', help="unsubscribe from the Senpai role") 
@is_in_guild(home_server_id)
async def hide(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="SENPAI")
    await member.remove_roles(role)

@bot.command(pass_context=True, name='noviolence', help="unsubscribe from the fight_me role") 
@is_in_guild(home_server_id)
async def noviolence(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="fight_me")
    await member.remove_roles(role)
bot.run(TOKEN)
client.run(TOKEN)