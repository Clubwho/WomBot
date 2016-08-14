# HUGE Help from Caleb <3

import discord
import json
import random
import re
from discord.ext import commands

with open('Lists.json') as json_data:
    jsonlist = json.load(json_data)


class Memes():
    def __init__(self, bot):
        self.bot = bot

    # Posts a meme
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        """Posts a meme, Use &meme help to see them all"""

        message = ctx.message
        ctx = ctx.message.content.split(' ', 2)[1]
        print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
        if ctx == 'help':
            memelistsort = sorted(jsonlist['MemeList'].keys())
            memeliststring = str(memelistsort)
            memehelp = re.sub("[\[\]']", "", memeliststring)
            await self.bot.say("I know: **{}**.".format(memehelp))
        elif ctx =='nummemes':
            await self.bot.say('I know **{}** memes!'.format(len(jsonlist['MemeList'])))
        else:
            try:
                await self.bot.say(jsonlist['MemeList'][ctx])
            except:
                await self.bot.say("That isn't a meme I know! **Use &meme help** to see all the memes I can say.")

    # Add a meme
    @commands.command(pass_context=True, hidden=True)
    async def addmeme(self, ctx, memename: str, memeurl: str):
        message = ctx.message
        ctx = ctx.message.content.split(' ', 2)[1]
        print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
        try:
            if message.author.id == '132111332752359424':
                if memename in jsonlist['MemeList']:
                    await self.bot.say('**{}** already exists!'.format(ctx))
                else:
                    if memename in jsonlist['MemeSuggest']:
                        del jsonlist['MemeSuggest'][memename]
                    jsonlist['MemeList'][memename] = memeurl
                    with open('Lists.json', 'w') as a:
                        a.write(json.dumps(jsonlist, indent=4))
                    await self.bot.say('Added **{}**'.format(memename))
            else:
                if memename in jsonlist['MemeList']:
                    await self.bot.say('**{}** already exists!'.format(ctx))
                else:
                    jsonlist['MemeSuggest'][memename] = memeurl
                    with open('Lists.json', 'w') as a:
                        a.write(json.dumps(jsonlist, indent=4))
                    await self.bot.say('Suggested **{}**, you will have to wait for Clubwho to add it.'.format(memename))
        except:
            await self.bot.say('**Did you miss the name or url?**')


    @commands.command(pass_context=True, hidden=True)
    async def removememe(self, ctx, memename: str):
        message = ctx.message
        ctx = ctx.message.content.split(' ', 2)[1]
        print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
        try:
            if message.author.id == '132111332752359424':
                if memename in jsonlist['MemeList']:
                    del jsonlist['MemeList'][memename]
                    with open('Lists.json', 'w') as a:
                        a.write(json.dumps(jsonlist, indent=4))
                    await self.bot.say('Removed **{}**'.format(memename))
                else:
                    await self.bot.say('**{}** isn\'t a meme'.format(memename))
            else:
                await self.bot.say('Only Clubwho can remove memes')
        except:
            return

    # Posts a random bork video
    @commands.group(pass_context=True)
    async def bork(self, ctx):
        """Posts a random bork video"""
        if ctx.invoked_subcommand is None:
            randbork = (random.choice(jsonlist['BorkList']))
            await self.bot.say(randbork)

    @bork.command(pass_context=True)
    async def add(self, ctx):
        message = ctx.message
        ctx = ctx.message.content.split(' ', 2)[2]
        if message.author.id == '132111332752359424':
            if ctx in jsonlist['BorkList']:
                await self.bot.say('Tha\'s already been borked!')
            else:
                jsonlist['BorkList'].append(ctx)
                with open('Lists.json', 'w') as a:
                    a.write(json.dumps(jsonlist, indent=4))
                await self.bot.say('**bork** *bork* `bork` bork ***BORK***')
        else:
            await self.bot.say('Only Clubwho can add borks')

    @bork.command()
    async def num(self):
        await self.bot.say('There are **{}** borks!'.format(len(jsonlist['BorkList'])))

def setup(bot):
    bot.add_cog(Memes(bot))
