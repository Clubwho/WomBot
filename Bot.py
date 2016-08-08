#HUGE Help from Caleb <3
#Other help from: Dsylexic, TesseractCat, DiscordAPI

#TODO
#Restart cmd
import discord
from discord.ext import commands
import sys

#Set command prefix
bot = commands.Bot(command_prefix='&', description='Clubwho\'s dank bot')



print('------')
print('Loading')
print('------')

#Say who it is when logging in (not in discord)
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    #Load other files
    startup_extensions = ['Utilities', 'Memes', 'Math']
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            print('Loading: {}'.format(extension))
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))



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
