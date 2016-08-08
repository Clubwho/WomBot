#HUGE Help from Caleb <3

import sys
import json
import random
from discord.ext import commands

#Videos for bork command
borkoptions = ["https://www.youtube.com/watch?v=vwGnXKNGjT0", "https://www.youtube.com/watch?v=5i2brBA_dl8",
               "https://www.youtube.com/watch?v=b2p8Zxmuq4g", "https://www.youtube.com/watch?v=AeEH5ugJrUU",
               "https://www.youtube.com/watch?v=i1H0leZhXcY", "https://www.youtube.com/watch?v=gIx6_Srsrog",
               "https://www.youtube.com/watch?v=5dbG4wqN0rQ"]

#Meme help table
memehelp = """```Meme help

Memes:
  yee         Posts yee
  wow         Posts wow gif
  wew         See wow
  lenny       ( ͡° ͜ʖ ͡° )
  keem        Keemstar dancing
  straya      Go Aussie Go
  attackheliI sexually identify as an Attack Helicopter
  song        Hey baby
  wtf finland Loituma - "Ievan Polkka"
  tunak       TUNAK TUNAK TUNAKTUNAK TUNAK
  help        Posts this```
"""

#Meme2 list
memelist = ['http://i.imgur.com/SdM4EME.png', 'http://i.imgur.com/Mj2iT9d.gif',
            '( ͡° ͜ʖ ͡° )', 'https://www.youtube.com/watch?v=tuCi9_dfntg&index=34&list=WL',
            'https://www.youtube.com/watch?v=mZ3Ihas3ouw', 'https://www.youtube.com/watch?v=WPMDCJrRpT8',
            'https://www.youtube.com/watch?v=4kOX-qE6Ka4', 'https://www.youtube.com/watch?v=4om1rQKPijI',
            'https://www.youtube.com/watch?v=vTIIMJ9tUc8']

with open('MemeList.json') as json_data:
    memelistj = json.load(json_data)

class Memes():
    def __init__(self, bot):
        self.bot = bot

    # Posts a meme
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        """Posts a meme, Use &meme help to see them all"""

        message = ctx.message
        ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
        print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
        try:
            if ctx == 'yee':
                await self.bot.say(memelist[0])
            elif ctx == 'wow' or ctx == 'wew':
                await self.bot.say(memelist[1])
            elif ctx == 'lenny':
                await self.bot.say(memelist[2])
            elif ctx == 'keem':
                await self.bot.say(memelist[3])
            elif ctx == 'straya':
                await self.bot.say(memelist[4])
            elif ctx == 'attackheli':
                await self.bot.say(memelist[5])
            elif ctx == 'song':
                await self.bot.say(memelist[6])
            elif ctx == 'wtf finland':
                await self.bot.say(memelist[7])
            elif ctx == 'tunak':
                await self.bot.say(memelist[8])
            elif ctx == 'help':
                await self.bot.say(memehelp)
            elif ctx == 'test':
                await self.bot.say(memelistj['yee'])
            elif ctx == 'nummemes':
                await self.bot.say('There are **{}** memes I can say.'.format(len(memelist)))
            else:
                await self.bot.say('That isn\'t a meme I know! Use **&meme help** to see all the memes I can say.')
        except:
            print(sys.exc_info()[0])

    # Posts a random bork video from borkoptions
    @commands.command()
    async def bork(self):
        """Posts a random bork video"""

        randbork = (random.choice(borkoptions))
        await self.bot.say(randbork)

    #Meme testing
    @commands.command(pass_context=True, hidden=True)
    async def addmeme(self, ctx):
        message = ctx.message
        ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
        print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
        try:
            if message.author.id == '132111332752359424':
                if ctx in memelist:
                    await self.bot.say('**{}** already exists!'.format(ctx))
                else:
                    memelist.append(ctx)
                    await self.bot.say('Added **{}**'.format(ctx))
            else:
                await self.bot.say('Only @Clubwho can add memes')
        except:
            return

    @commands.command(pass_context=True, hidden=True)
    async def removememe(self, ctx):
        message = ctx.message
        ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
        print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
        try:
            if message.author.id == '132111332752359424':
                if ctx in memelist:
                    del memelist[ctx]
                    await self.bot.say('Removed **{}**'.format(ctx))
                else:
                    await self.bot.say('**{}** isn\'t a meme'.format(ctx))
            else:
                await self.bot.say('Only @Clubwho can remove memes')
        except:
            return

def setup(bot):
    bot.add_cog(Memes(bot))
