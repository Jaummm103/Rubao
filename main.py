import discord
import func, msc, youtube_dl, os
from discord.ext import commands
from discord.ext.commands import bot

client = discord.Client()
client1 = commands.Bot(command_prefix="$")


@client.event

async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

@client1.command()

async def oi(ctx, arg):
    await ctx.send(func.oi(ctx, arg))

@client1.command(name='play')

async def play(ctx, url):
    await (msc.play(ctx, url))

client.run('ODk1NjQ4MTAzOTM4NTMxMzI4.YV7nTA.NhhqjdvYMqcY1XSWYj9QVKNBuJw')

client1.run('ODk1NjQ4MTAzOTM4NTMxMzI4.YV7nTA.NhhqjdvYMqcY1XSWYj9QVKNBuJw')
