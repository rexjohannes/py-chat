import discord
import asyncio
import os
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='!')
status = cycle(["My", "Cool", "Presence.", "Here", "you", "can", "add", "more!"])

@bot.event
async def on_ready():
    change_status.start()
#    await bot.change_presence(activity=discord.Game("GAME"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.utils.oauth_url(bot.user.id))

@tasks.loop(seconds=120)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing Argument!")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not Found!")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don´t have Permssions to do that!")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("The Bot hasn`t the missing Permission!")
    if isinstance(error, commands.NotOwner):
        await ctx.send("This Command is only for my Lord!")

        
bot.remove_command('help')

@bot.command()
async def help(ctx):
  await ctx.send("Commands: \nhelp - View this message.")
  
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")  
bot.run(token)
