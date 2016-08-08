import math
from discord.ext import commands

class Maths():
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def math(self, ctx):
        """Math parent command"""

        if ctx.invoked_subcommand is None:
            await self.client.say('Math is only the parent command.')

    @math.command()
    async def add(self, left : int, right : int):
        """Adds two numbers"""
        try:
            await self.bot.say('{} + {} = **{}**'.format(left, right,left + right))
        except:
            return

    @math.command()
    async def sub(self, left : int, right : int):
        """Subtracts two numbers"""
        try:
            await self.bot.say('{} - {} = **{}**'.format(left, right,left - right))
        except:
            return

    @math.command()
    async def multi(self, left: int, right: int):
        """Multiply's two numbers"""
        try:
            await self.bot.say('{} * {} = **{}**'.format(left, right, left * right))
        except:
            return

    @math.command()
    async def div(self, left: int, right: int):
        """Divides two numbers"""
        try:
            await self.bot.say('{} ÷ {} = **{}**'.format(left, right, left / right))
        except:
            return

    @math.command(pass_context=True)
    async def paraps(self, ctx):
        """Perfect Square ax^2 + bx + c"""

        ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
        try:
            return
        except:
            return

def setup(bot):
    bot.add_cog(Maths(bot))