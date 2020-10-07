import os
import discord
import random
import csv
import json
from dotenv import load_dotenv
import discord.ext.commands
from discord.ext.commands import bot
from discord.ext import commands
from discord.utils import get

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
guild = os.getenv('DISCORD_GUILD')
secret_server_id = os.getenv('Secret_Server')
home_server_id = int(secret_server_id)
client = discord.Client()

def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild.id == guild_id
    return commands.check(predicate)
# https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='staycool', help='Gives a helpful message')
@is_in_guild(home_server_id)
async def cool(ctx):
    await ctx.send("Take current events talk to #current_events_lounge")

@bot.command(name='nicknames', help='Gives you a list of nicknames')
async def nicknames(ctx):
    with open('nickname.json') as f:
        nicknames = json.load(f)
    nicknamelist = []
    for i in nicknames:
        name = nicknames[i]["Nickname"]
        nicknamelist.append(name)
    await ctx.send(nicknamelist)

@bot.command(name='pogo', help='gives pogo friend codes in a copypaste friendly format')
async def pogo(ctx, arg1):
    with open('coolerlounge.json') as f:
        data = json.load(f)
    with open('nickname.json') as f:
        nicknames = json.load(f)
    if arg1 == "all":
        pogo = ""
        for i in data:
                name = data[i]["Nickname"]
                code = data[i]['Pogo']
                if code != "":
                    newentry = name + " : " + code + "\n"
                    pogo += newentry
                else:
                    pass 
    else: 
        try:
            name = nicknames[arg1]
            USERID=name.get('DiscordID')
            pogo = data[USERID]['Pogo']
            if pogo == "":
                pogo = "The user you chose does not have a friend code in the system"
        except KeyError:
            pogo = "This user does not seem to exist or you got the nickname wrong"
    await ctx.send(pogo)

@bot.command(name='switch', help='Get your switch codes here')
async def switch(ctx, arg1):
    with open('coolerlounge.json') as f:
        data = json.load(f)
    with open('nickname.json') as f:
        nicknames = json.load(f)
    if arg1 == "all":
        switch = ""
        for i in data:
                name = data[i]["Nickname"]
                code = data[i]['Switch']
                if code != "":
                    newentry = name + " : " + code + "\n"
                    switch += newentry
                else:
                    pass 
    else:         
        try:
            name = nicknames[arg1]
            USERID=name.get('DiscordID')
            switch = data[USERID]['Switch']
            if switch == "":
                switch = "The user you chose does not have a friend code in the system"
        except KeyError:
            switch = "This user does not seem to exist or you got the nickname wrong"
    await ctx.send(switch)

@bot.command(name='xbox', help='Get your Xbox Usernames here')
async def xbox(ctx, arg1):
    with open('coolerlounge.json') as f:
        data = json.load(f)
    with open('nickname.json') as f:
        nicknames = json.load(f)
    if arg1 == "all":
        xbox = ""
        for i in data:
                name = data[i]["Nickname"]
                code = data[i]['XBL']
                if code != "":
                    newentry = name + " : " + code + "\n"
                    xbox += newentry
                else:
                    pass 
    else:    
        try:
            name = nicknames[arg1]
            USERID=name.get('DiscordID')
            xbox = data[USERID]['XBL']
            if xbox == "":
                xbox = "The user you chose does not have a friend code in the system"
        except KeyError:
            xbox = "This user does not seem to exist or you got the nickname wrong"
    await ctx.send(xbox)

@bot.command(name='Playstation', help='Get your PSN names here')
async def playstation(ctx, arg1):
    with open('coolerlounge.json') as f:
        data = json.load(f)
    with open('nickname.json') as f:
        nicknames = json.load(f)
    if arg1 == "all":
        playstation = ""
        for i in data:
                name = data[i]["Nickname"]
                code = data[i]['PSN']
                if code != "":
                    newentry = name + " : " + code + "\n"
                    playstation += newentry
                else:
                    pass 
    else:    
        try:
            name = nicknames[arg1]
            USERID=name.get('DiscordID')
            playstation = data[USERID]['PSN']
            if playstation == "":
                playstation = "The user you chose does not have a friend code in the system"
        except KeyError:
            playstation = "This user does not seem to exist or you got the nickname wrong"
    await ctx.send(playstation)

@bot.command(name='AltOne', help='Get Pogo Alt codes here')
async def firstAlt(ctx, arg1):
    with open('coolerlounge.json') as f:
        data = json.load(f)
    with open('nickname.json') as f:
        nicknames = json.load(f)
    try:
        name = nicknames[arg1]
        USERID=name.get('DiscordID')
        Alt = data[USERID]['PogoAlt']
        if Alt == "":
            Alt = "The user you chose does not have a friend code in the system"
    except KeyError:
        Alt = "This user does not seem to exist or you got the nickname wrong"
    await ctx.send(Alt)

@bot.command(name='AltTwo', help='Get Secondary Alt codes here')
async def SecondAlt(ctx, arg1):
    with open('coolerlounge.json') as f:
        data = json.load(f)
    with open('nickname.json') as f:
        nicknames = json.load(f)
    try:
        name = nicknames[arg1]
        USERID=name.get('DiscordID')
        Alt = data[USERID]['PogoAlt2']
        if Alt == "":
            Alt = "The user you chose does not have a friend code in the system"
    except KeyError:
        Alt = "This user does not seem to exist or you got the nickname wrong"
    await ctx.send(Alt)

@bot.command(name='AltThree', help='Get your Xbox Usernames here')
async def ThirdAlt(ctx, arg1):
    with open('coolerlounge.json') as f:
        data = json.load(f)
    with open('nickname.json') as f:
        nicknames = json.load(f)
    try:
        name = nicknames[arg1]
        USERID=name.get('DiscordID')
        Alt = data[USERID]['PogoAlt3']
        if Alt == "":
            Alt = "The user you chose does not have a friend code in the system"
    except KeyError:
        Alt = "This user does not seem to exist or you got the nickname wrong"
    await ctx.send(Alt)

@bot.command(name='notsafe', help="reminds people to keept talk appropriate-ish")
@is_in_guild(home_server_id)
async def safe(ctx):

    await ctx.send("Let's take adult content elsewhere, like #freeza_lounge or DM's")

@bot.command(name='set', help='Enter switch, xbox, pogo, alt1, alt2, alt3, or playstation followed by your info')
async def set(ctx, arg1, arg2):
    ID=ctx.author.id
    USERID=str(ID)
    platform = arg1.lower()
    with open('coolerlounge.json') as f:
        data = json.load(f)
    if platform == 'switch':   
        data[USERID]['Switch'] = arg2
        info = 'Your Switch friendcode has been updated this is the new value ' + arg2
    elif platform == 'xbox':
        data[USERID]['XBL'] = arg2
        info = 'Your XBL profile has been updated this is the new value ' + arg2
    elif platform == 'pogo':
        data[USERID]['Pogo'] = arg2
        info = 'Pogo Info updated this is the new value ' + arg2
    elif platform == 'alt1':
        data[USERID]['PogoAlt'] = arg2
        info = 'Pogo Alt updated this is the new value ' + arg2
    elif platform == 'alt2':
        data[USERID]['PogoAlt2'] = arg2
        info = 'Your second Pogo Alt has been updated this is the new value ' + arg2
    elif arg1 == 'alt3':
        data[USERID]['PogoAlt3'] = arg2
        info = 'Your third pogo alt has been updated this is the new value ' + arg2
    elif arg1 == 'playstation':
        data[USERID]['PSN'] = arg2
        info = 'Your Playstation has been updated this is the new value ' + arg2
    else: 
        info = "We currently don't support that"
    with open('coolerlounge.json', 'w') as f:
        json.dump(data, f)
    await ctx.send(info)




@bot.command(name='json', help='creates a jsonfile from the last backup')
@commands.is_owner()
async def jsoncreator(ctx):
    file = 'data.csv'
    jsonfile='coolerlounge.json'
    data={}
    with open(file) as csvFile:
        rd = csv.DictReader(csvFile)
        for rows in rd:
            id = rows['DiscordID']
            data[id] = rows
    with open(jsonfile, 'w') as jsonFile:
        jsonFile.write(json.dumps(data,indent=4))
    successmessage="update successful"    
    await ctx.send(successmessage)

@bot.command(name='csv', help='backs up the current json to csv for backup')
@commands.is_owner()
async def csvmaker(ctx):
    hi = "Hello Wolf"
    await ctx.send(hi)

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
    with open('coolerlounge.json') as f:
        data = json.load(f)
    ID=ctx.author.id
    USERID=str(ID)
    name=data[USERID]["Nickname"]
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