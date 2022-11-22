from Fortuna import d
from discord.ext import commands

from bot.cogs.dice_parser import parse_dice


class Dice(commands.Cog):
    """ Random Engine: Fortuna """

    @commands.command()
    async def d20(self, ctx):
        """ Rolls d20 - flat uniform distribution """
        await ctx.send(f"{ctx.author.name} rolls `d20` => {d(20)}")


class DiceParser(commands.Cog):

    @commands.command()
    async def roll(self, ctx, dice_expr):
        await ctx.send(f"{ctx.author.name} rolls `{dice_expr}` => {parse_dice(dice_expr)}")


async def setup(bot):
    await bot.add_cog(Dice(bot))
    await bot.add_cog(DiceParser(bot))
    print("[•] Dice Cogs Loaded")
