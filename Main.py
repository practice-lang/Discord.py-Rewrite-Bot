import asyncio
import discord
import random
import os
from itertools import cycle
from discord.ext import commands
client = commands.Bot(command_prefix='>')



@client.event
async def on_ready():
    game = discord.Game("with the API")
    await client.change_presence(status=discord.Status.online, activity=game)
    print(f'Logged in as: {client.user.name} - {client.user.id} Version: {discord.__version__}\n')
    print( [f"{guild} {len(guild.members)}" for guild in app.guilds])

@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command(pass_context=True)
async def clear(ctx, amount=100):
   channel = ctx.message.channel
   messages = []
   async for message in client.logs_from(channel, limit=int(amount)):
       message.append(message)
   await client.delete_messages(messages)
   await client.say("delet")

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

for cog in os.listdir(".\\cogs"):
    if cog.endswith(".py") and not cog.startswith("_"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            client.load_extension(cog)
            print(f"{cog} load")
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e


client.run('토큰')
