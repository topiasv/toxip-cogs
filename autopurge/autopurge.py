from redbot.core import commands

class AutoPurge(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def autopurge(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I will purge!")