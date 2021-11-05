from discord.ext import commands

client = commands.Bot(command_prefix="$")

@client.command()

async def oi(ctx, arg):
    await ctx.send(arg)

client.run('ODk1NjQ4MTAzOTM4NTMxMzI4.YV7nTA.NhhqjdvYMqcY1XSWYj9QVKNBuJw')
