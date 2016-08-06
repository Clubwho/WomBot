import goslate
import microsofttranslator
from microsofttranslator import Translator

class Utilities():
    def __init__(self, bot):
        self.bot = bot

        # Setup translate commands
        gs = goslate.Goslate()
        translator = Translator('WomBot', 'CQ9gw+TgF1ATumSQWp896QFM04DLZs9Hh0CI/WK9cBY=')

        # Translates a language into english
        @bot.command(pass_context=True)
        async def translate(ctx):
            """Translates something into english"""

            message = ctx.message
            ctx = ctx.message.content[len(ctx.message.content.split(" ")[0]) + 1:]
            print(message.author.name + "@" + message.server.name + "~" + message.channel.name + ": " + message.content)
            try:
                curlanguage = translator.detect_language(ctx)
                translated = translator.translate(ctx, 'en')
                curlanguagefull = gs.get_languages()[curlanguage]
                await bot.say('Translated from **' + curlanguagefull + '**: ' + translated)
            except microsofttranslator.TranslateApiException:
                await bot.say("Timed out from server - please try again in a few seconds.")
            except microsofttranslator.ArgumentOutOfRangeException:
                await bot.say("Invalid language.")


def setup(bot):
    bot.add_cog(Utilities(bot))