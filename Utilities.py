#HUGE Help from Caleb <3

import goslate
import microsofttranslator
from microsofttranslator import Translator
from discord.ext import commands

# Setup translate commands
gs = goslate.Goslate()
translator = Translator('WomBot', 'Token')


class Utilities():
    def __init__(self, bot):
        self.bot = bot

    # Translates a language into english
    @commands.command(pass_context=True)
    async def translate(self, ctx):
        """Translates something into english"""

        message = ctx.message
        ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
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


def setup(bot):
    bot.add_cog(Utilities(bot))

