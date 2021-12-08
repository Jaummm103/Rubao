from discord.ext import commands # teste para os broxa
# Comandos básicos pro bot, maioria só pra teste #

@commands.command(name='oi')

async def oi(ctx, arg):
  await ctx.send(arg)
	
@commands.command(name='teste')

async def teste(ctx):
	await ctx.send('Bip bop testando bip bop')

@commands.command(name='ping')
async def ping(ctx):
  latency = commands.latency
  await ctx.send(latency)

# commands.run('')
