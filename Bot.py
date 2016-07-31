#Help from: Caleb, Dsylexic, TesseractCat, DiscordAPI

import discord      #Imports discords commands
from discord.ext import commands
import asyncio      #Imports asyncio's commands
import goslate
import urllib
import microsofttranslator
from microsofttranslator import Translator

bot = commands.Bot(command_prefix='&', description='Clubwho\'s dank bot')
gs = goslate.Goslate()
languages = gs.get_languages()
translator = Translator('WomBot', 'CQ9gw+TgF1ATumSQWp896QFM04DLZs9Hh0CI/WK9cBY=')

timeerror = 0

#Say who it is when logging in (not in discord)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def meme(ctx, message):
    message = ctx.message
    ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
    print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
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
    else:
        await bot.say('That isn\'t a meme I know!')

@bot.command(pass_context=True)
async def translate(ctx, message):
    message = ctx.message
    ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
    print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
    global timeerror
    try:
        
        curlanguage = translator.detect_language(ctx)
        translated = translator.translate(ctx, 'en')
        curlanguagefull = gs.get_languages()[curlanguage]
        await bot.say('Translated from **' + curlanguagefull + '**: ' + translated)
        timeerror = 0
    except microsofttranslator.TranslateApiException:
        timeerror = timeerror + 1
        if timeerror == 5:
            await bot.say("Please wait a bit longer.")
        elif timeerror == 10:
            await bot.say("Wait 1 minute before trying again")
        elif timeerror => 20:
            await bot.say("Contact @Clubwho, an issue might have occured")
        else:
            await bot.say("Timed out from server - please try again in a few seconds.")
    except microsofttranslator.ArgumentOutOfRangeException:
        await bot.say("Invalid language.")

#https://discordapp.com/oauth2/authorize?client_id=205653889624571905&scope=bot&permissions=0
bot.run('Token')
