import discord, youtube_dl, os
from discord.ext import commands
from discord.ext.commands import bot


client = commands.Bot(command_prefix="$")

@client.command(name='play')

async def play(ctx, url: str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='STAFF CHAT')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await voiceChannel.connect()

@client.command()

async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send('E eu lá to conectado, porra?')

@client.command()

async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send('Pausei bro')
    else:
        await ctx.send('To tocando nada não, bro')

@client.command()

async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send('Já to tocando, amigão')

@client.command()

async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

client.run('ODk1NjQ4MTAzOTM4NTMxMzI4.YV7nTA.NhhqjdvYMqcY1XSWYj9QVKNBuJw')
