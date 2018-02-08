import discord
from discord.ext import commands

class invite:
    """Invite Rory to your discord!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self):
        """Invite Rory to your discord!"""

        #Output Message
        await self.bot.say("Bot Invite Link: https://discordapp.com/oauth2/authorize?client_id=405191776127811604&scope=bot&permissions=-1 ")

def setup(bot):
    bot.add_cog(invite(bot))
