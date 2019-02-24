import discord
from discord.ext import commands
import asyncio
import random
import requests
import os

client = discord.Client()
bot = commands.Bot(command_prefix="Crot.")

async def status_task():
    while True:
        dnd = discord.Status.dnd
        await bot.change_presence(activity=discord.Game(name='LAGI NGEUE |Try Crot.commands'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='AGI NGEUE |Try Crot.commands '), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='GI NGEUE |Try Crot.commands  '), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='I NGEUE |Try Crot.commands   '), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name=' NGEUE |Try Crot.commands   L'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='NGEUE |Try Crot.commands   LA'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='GEUE |Try Crot.commands   LAG'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='EUE |Try Crot.commands   LAGI'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='UE |Try Crot.commands   LAGI '), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='E |Try Crot.commands   LAGI N'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name=' |Try Crot.commands   LAGI NG'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='|Try Crot.commands   LAGI NGE'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='Try Crot.commands   LAGI NGEU'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='ry Crot.commands   LAGI NGEUE'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='y Crot.commands   LAGI NGEUE '), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name=' Crot.commands   LAGI NGEUE |'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='Crot.commands   LAGI NGEUE |T'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='rot.commands   LAGI NGEUE |Tr'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='ot.commands   LAGI NGEUE |Try'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='t.commands   LAGI NGEUE |Try '), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='.commands   LAGI NGEUE |Try Cr'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='commands   LAGI NGEUE |Try Cro'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='ommands   LAGI NGEUE |Try Crot'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='mmands   LAGI NGEUE |Try Crot.c'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='mands   LAGI NGEUE |Try Crot.co'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='ands   LAGI NGEUE |Try Crot.com'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='nds   LAGI NGEUE |Try Crot.comm'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='ds   LAGI NGEUE |Try Crot.comma'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='s   LAGI NGEUE |Try Crot.comman'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='   LAGI NGEUE |Try Crot.command'), status=discord.Status.dnd)
        await asyncio.sleep(2)
        await bot.change_presence(activity=discord.Game(name='  LAGI NGEUE |Try Crot.commands'), status=discord.Status.dnd)
        await asyncio.sleep(2)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready for ngebacod!")
    bot.loop.create_task(status_task())

@bot.command()
async def hey(ctx):
    await ctx.send("APA LU KONTOL! "+str(ctx.message.author.mention))

@bot.command()
async def commands(ctx):
    await ctx.send("BARU ADA .help ,.hey & .invite DOANG NGENTOD! ")

@bot.command()
async def invite(ctx):
    await ctx.send("NIH LINKNYA BABI @here https://discordapp.com/api/oauth2/authorize?client_id=548945449344696331&permissions=0&scope=bot ")

bot.run(str(os.environ.get('BOT_TOKEN')))
