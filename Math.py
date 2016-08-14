import math
import wolframalpha
import configparser
import os
from discord.ext import commands
from time import sleep

wDir = os.path.dirname(os.path.realpath(__file__))

#WolframAlpha API Token
config = configparser.ConfigParser()
config.read('Settings.ini')
WolframAlphaToken = config['Settings']['WolframAlphaToken'].replace(' ','')
waClient = wolframalpha.Client(WolframAlphaToken)

class Maths():
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def math(self, ctx):
        """Math parent command"""

        if ctx.invoked_subcommand is None:
            await self.client.say('Math is only the parent command.')

    @math.command()
    async def add(self, left : float, right : float):
        """Adds two numbers"""
        try:
            await self.bot.say('{} + {} = **{}**'.format(left, right,left + right))
        except:
            return

    @math.command()
    async def sub(self, left : float, right : float):
        """Subtracts two numbers"""
        try:
            await self.bot.say('{} - {} = **{}**'.format(left, right,left - right))
        except:
            return

    @math.command()
    async def multi(self, left : float, right : float):
        """Multiply's two numbers"""
        try:
            await self.bot.say('{} * {} = **{}**'.format(left, right, left * right))
        except:
            return

    @math.command()
    async def div(self, left : float, right : float):
        """Divides two numbers"""
        try:
            await self.bot.say('{} ÷ {} = **{}**'.format(left, right, left / right))
        except:
            return

    @math.command(pass_context=True)
    async def paras(self, ctx, a: float, b: float, c: float):
        """Show a parabola using perfect square, ax^2 + bx + c, NOTE: YOU MUST HAVE A B and C like: &math para 1 0 1"""

        d = (b ** 2) - (4 * a * c)

        if d < 0:
            print
            xintcheck = 0
        elif d == 0:
            xint1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            xintcheck = 1
        else:
            xint1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            xint2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            xintcheck = 2

        axisofsym = b /(2 * a)
        vertex = a * axisofsym ** 2 + (b * axisofsym) + c

        watext = ""
        await self.bot.send_typing(ctx.message.channel)

        waResult = waClient.query('{} * x ** 2 + {}x + {}'.format(a, b, c))
        for pod in waResult.pods[0:3]:
            watext += "**" + pod.title + "**\n"
            watext += pod.img + "\n"
            await self.bot.say(watext)
            watext = ""

        await self.bot.say('**Axis of symmetry = x = -{}**'.format(axisofsym))
        await self.bot.say('**Vertex = ({}, {})**'.format(axisofsym, vertex))
        await self.bot.say('**Y-int = (0,{})**'.format(c))
        if xintcheck == 1:
            await self.bot.say('**X-int = ({}, 0)**'.format(xint1))
        elif xintcheck == 2:
            await self.bot.say('**X-int = ({}, 0) and ({}, 0)**'.format(xint1, xint2))
        else:
            await self.bot.say('**No X-int**')

    @math.command(pass_context=True)
    async def parav(self, ctx, a: float, b: float, c: float):

        watext = ""
        await self.bot.send_typing(ctx.message.channel)

        waResult = waClient.query('{} * (x - {}) ** 2 + {}'.format(a, b, c))
        for pod in waResult.pods[0:3]:
            watext += "**" + pod.title + "**\n"
            watext += pod.img + "\n"
            await self.bot.say(watext)
            watext = ""

        yint = (b ** 2) * a + c

        if a < 0 :
            if c > 0:
                xintcheck = 1
                xint1 = b + math.sqrt(-c / a)
                xint2 = b - math.sqrt(-c / a)
            else:
                xintcheck = 0
        else:
            if c < 0:
                xintcheck = 1
                xint1 = b + math.sqrt(-c / a)
                xint2 = b - math.sqrt(-c / a)
            else:
                xintcheck = 0

        await self.bot.say('**Vertex = ({}, {})\nAxis of symmetry: x = {}\nY-int = (0, {})**'.format(b, c, b , yint))
        if xintcheck == 1:
            await self.bot.say('**X-int = ({}, 0) and ({}, 0)**'.format(xint1, xint2))
        else:
            await self.bot.say('**No X-int**')

def setup(bot):
    bot.add_cog(Maths(bot))
