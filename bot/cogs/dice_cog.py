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
    """ Random Engine: Fortuna """

    @commands.command()
    async def roll(self, ctx, *, dice_expression: str = 'd20'):
        """ Evaluates dice_expression: d6, 3d6 or 3d6+1
        Examples:
            /roll       -> rolls one twenty-sided die
            /roll d10   -> rolls one ten-sided die
            /roll 3d6   -> rolls three six-sided dice
            /roll 8d6+3 -> rolls eight six-sided dice, then adds three
            /roll XdY+Z -> rolls a Y-sided dice X times, then adds Z """
        await ctx.send(f"{ctx.author.name} rolls {parse_dice(dice_expression)}")


async def setup(bot):
    await bot.add_cog(Dice(bot))
    await bot.add_cog(DiceParser(bot))
    print("[•] Dice Cogs Loaded")
