#import discord, youtube_dl, os
#from discord.ext import commands
#from discord.ext.commands import bot


#@commands.command(name='play')

#async def play(ctx, url: str):
    #channel = ctx.author.voice.channel
    #voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)
    #if not voice.is_connected():
        #await channel.connect

#@commands.command(name='join')

#async def join(ctx, enter):
  #channel = ctx.author.voice.channel
  #await channel.connect()

#@commands.command(name='leave')

#async def leave(ctx):
    #voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)
    #if voice.is_connected():
        #await voice.disconnect()
    #else:
        #await ctx.send('E eu lá to conectado, porra?')

#@commands.command(name='pause')

#async def pause(ctx):
    #voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)
    #if voice.is_playing():
        #voice.pause()
        #await ctx.send('Pausei bro')
    #else:
        #await ctx.send('To tocando nada não, bro')

#@commands.command(name='resume')

#async def resume(ctx):
    #voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)
    #if voice.is_paused():
        #voice.resume()
    #else:
        #await ctx.send('Já to tocando, amigão')

#@commands.command(name='stop')

#async def stop(ctx):
    #voice = discord.utils.get(commands.voice_clients, guild=ctx.guild)
    #voice.stop()