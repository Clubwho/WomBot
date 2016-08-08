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

with open('MemeList.json') as json_data:
    memelist = json.load(json_data)

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
            await self.bot.say(memelist['MemeList'][ctx])
        except:
            await self.bot.say("That isn't a meme I know! **Use &meme help** to see all the memes I can say.")

    # Posts a random bork video from borkoptions
    @commands.command()
    async def bork(self):
        """Posts a random bork video"""

        randbork = (random.choice(borkoptions))
        await self.bot.say(randbork)

    #Meme testing
    @commands.command(pass_context=True, hidden=True)
    async def addmeme(self, ctx, memename : str, memeurl : str):
        message = ctx.message
        ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
        print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
        try:
            if message.author.id == '132111332752359424':
                if memename in memelist['MemeList']:
                    await self.bot.say('**{}** already exists!'.format(ctx))
                else:
                    memelist['MemeList'][memename] = memeurl
                    with open('MemeList.json', 'w') as a:
                        a.write(json.dumps(memelist))
                    await self.bot.say('Added **{}**'.format(memename))
            else:
                await self.bot.say('Only @Clubwho can add memes')
        except Exception as e:
            print (e)

    @commands.command(pass_context=True, hidden=True)
    async def removememe(self, ctx, memename : str):
        message = ctx.message
        ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
        print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
        try:
            if message.author.id == '132111332752359424':
                if memename in memelist['MemeList']:
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
