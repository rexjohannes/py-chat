import discord
import asyncio
import os
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import time 
import datetime as DT
import random
from discord import channel

bot = commands.Bot(command_prefix='!')
status = cycle(["py-chat", "Globalchat? | py-chat"])

@bot.event
async def on_ready():
    change_status.start()
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

        
@client.event
async def on_message(message):
    if message.author.bot: return
    member = message.author
    channel = message.channel
    if channel.name == "py-chat":
        msg = message.content
        print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
        embed = discord.Embed(color=discord.Color.blue(), title=f"{message.author} | {member.guild}", description=msg)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.set_footer(text=f"ist auf {len(bot.guilds)} Servern", icon_url=f"{member.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await message.delete()
        for guild in bot.guilds: 
                channel:discord.Channel = discord.utils.get(guild.channels, name="py-chat")
                await channel.send(embed=embed)
  
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")  
bot.run(token)
