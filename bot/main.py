import os
import asyncio

import discord
from discord.ext import commands
from dotenv import load_dotenv


bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
bot.description = "DiceBot slash commands by category"


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Dice"))
    print("[•] Ready To Roll")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=999):
    """ Clears the last N messages, where N = amount + 1 """
    await ctx.channel.purge(limit=amount+1)


async def main():
    load_dotenv()
    await bot.load_extension("bot.cogs.dice_cog")
    await bot.start(os.getenv("TOKEN"))


if __name__ == '__main__':
    asyncio.run(main())
