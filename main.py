import discord
import func
import musica
from discord.ext import commands

cogs = [musica]

client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)

# Curar as mensagens pra não responder bots e etc #
@client.event

async def on_message(message):
  message.content = message.content.lower()
  await client.process_commands(message)
  if message.author == client.user:
    return

# Funções abaixo executam as funções dos outros arquivos #
@client.command(name='oi')

async def oi(ctx, arg):
  await ctx.send(func.oi(ctx, arg))

@client.command(name='teste')

async def teste(ctx):
  await ctx.send(func.teste(ctx))

@client.command(name='ping')

async def ping(ctx):
  await ctx.send(func.ping(ctx))

# @client.command(name='join')

# async def join(ctx):
# await(msc.join(ctx))

# @client.command(name='play')

# async def play(ctx, url: str):
#   await (msc.play(ctx, url))

client.run('')