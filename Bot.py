#Help from: Caleb, Dsylexic, TesseractCat, DiscordAPI

#TODO
#Restart cmd

import discord      #Imports discords commands
from discord.ext import commands
import random
import sys

#Set command prefix
bot = commands.Bot(command_prefix='&', description='Clubwho\'s dank bot')

#Videos for bork command
borkoptions = ["https://www.youtube.com/watch?v=vwGnXKNGjT0", "https://www.youtube.com/watch?v=5i2brBA_dl8",
               "https://www.youtube.com/watch?v=b2p8Zxmuq4g", "https://www.youtube.com/watch?v=AeEH5ugJrUU",
               "https://www.youtube.com/watch?v=i1H0leZhXcY", "https://www.youtube.com/watch?v=gIx6_Srsrog",
               "https://www.youtube.com/watch?v=5dbG4wqN0rQ"]

print('Loading')
print('------')

#Say who it is when logging in (not in discord)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    startup_extensions = ['Utilities']
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Loading ' + extension)
            print('------')
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

#Posts a meme
@bot.command(pass_context=True)
async def meme(ctx):
    """Posts a meme, Use &meme help to see them all"""

    message = ctx.message
    ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
    print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
    try:
        if ctx == 'yee':
            await bot.say('http://i.imgur.com/SdM4EME.png')
        elif ctx == 'wow' or ctx == 'wew':
            await bot.say('http://i.imgur.com/Mj2iT9d.gif')
        elif ctx == 'lenny':
            await bot.say('( ͡° ͜ʖ ͡° )')
        elif ctx == 'keem':
            await bot.say('https://www.youtube.com/watch?v=tuCi9_dfntg&index=34&list=WL')
        elif ctx == 'straya':
            await bot.say('https://www.youtube.com/watch?v=mZ3Ihas3ouw')
        elif ctx == 'attackheli':
            await bot.say('https://www.youtube.com/watch?v=WPMDCJrRpT8')
        elif ctx == 'song':
            await bot.say('https://www.youtube.com/watch?v=4kOX-qE6Ka4')
        elif ctx == 'wtf finland':
            await bot.say('https://www.youtube.com/watch?v=4om1rQKPijI')
        elif ctx == 'tunak':
            await bot.say('https://www.youtube.com/watch?v=vTIIMJ9tUc8')
        elif ctx == 'help':
            await bot.say('https://github.com/Clubwho/WomBot#meme-commands')
        else:
            await bot.say('That isn\'t a meme I know! Use **&meme help** to see all the memes I can say.')
    except:
        return

#Posts a random bork video from borkoptions
@bot.command()
async def bork():
    """Posts a random bork video"""

    randbork = (random.choice(borkoptions))
    await bot.say(randbork)

#Shutdown command, only done by Clubwho
@bot.command(pass_context=True, hidden=True)
async def shutdown(ctx):
    """Clubwho only"""

    message = ctx.message
    if message.author.id == '132111332752359424' or message.author.id == bot.user.id:
        await bot.say('Shutting down')
        sys.exit('Shutting down')
    else:
        await bot.say('You aren\'t Clubwho!')

#https://discordapp.com/oauth2/authorize?client_id=205653889624571905&scope=bot&permissions=0
bot.run('Token')
