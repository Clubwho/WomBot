#HUGE Help from Caleb <3

import configparser
import wolframalpha
import goslate
import microsofttranslator
from microsofttranslator import Translator
from discord.ext import commands

config = configparser.ConfigParser()
config.read('Settings.ini')
MSTranslateApiToken = config['Settings']['MSTranslateApiToken'].replace(' ','')

# Setup translate commands
gs = goslate.Goslate()
translator = Translator('WomBot', MSTranslateApiToken)

#WolframAlpha API Token
config = configparser.ConfigParser()
config.read('Settings.ini')
WolframAlphaToken = config['Settings']['WolframAlphaToken'].replace(' ','')
waClient = wolframalpha.Client(WolframAlphaToken)

class Utilities():
    def __init__(self, bot):
        self.bot = bot

    # Translates a language into english
    @commands.command(pass_context=True)
    async def translate(self, ctx):
        """Translates something into english"""

        await self.bot.send_typing(ctx.message.channel)
        message = ctx.message
        ctx = ctx.message.content.split(' ', 1)[1]
        print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
        try:
            curlanguage = translator.detect_language(ctx)
            translated = translator.translate(ctx, 'en')
            curlanguagefull = gs.get_languages()[curlanguage]
            await self.bot.say('Translated from **{}**: {}'.format(curlanguagefull, translated))
        except microsofttranslator.TranslateApiException:
            await self.bot.say("Timed out from server - please try again in a few seconds.")
        except microsofttranslator.ArgumentOutOfRangeException:
            await self.bot.say("Invalid language.")

    @commands.command(pass_context=True)
    async def wolfalpha(self, ctx, search: str):
        """Gets Wolfram Alpha result for [search] put a 'true' at the beginning of your search to enable images."""

        waText = ""
        waText += "**--- Wolfram Alpha result for: " + search + " ---**\n"
        await self.bot.send_typing(ctx.message.channel)

        if search.split(" ")[0].lower() == "true":
            waResult = waClient.query(search.split(" ", 1)[1])
        else:
            waResult = waClient.query(search)

        for pod in waResult.pods:
            waText += "**" + pod.title + "**\n"
            if pod.text == None and search.split(" ")[0].lower() == "true":
                waText += pod.img + "\n"
                await self.bot.say(waText)
                watext = ""
            elif pod.text != None:
                waText += pod.text.replace("\\:", "\\u") + "\n"
        if len(waResult.pods) < 1:
            waText += "*No results, please rephrase your query.*"
        await self.bot.say(waText)

    @commands.command(pass_context=True)
    async def cl(self, ctx):
        """Clears messages since last boot"""
        async for message in self.client.logs_from(ctx.message.channel):
            if message.author == self.client.user:
                await self.client.delete_message(message)

def setup(bot):
    bot.add_cog(Utilities(bot))
