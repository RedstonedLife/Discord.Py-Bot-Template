import discord
from discord.ext import commands
import requests
import asyncio
import config

bot = commands.Bot(command_prefix='Bot Prefix (Example: b;)')

@bot.command(pass_context=True)
async def info(ctx):
  embed=discord.Embed(color=0xff7171)
  embed.add_field(name="Python", value="3.6.4", inline=True)
  embed.add_field(name="discord.py", value="1.0.0a", inline=True)
  embed.add_field(name="About BlueTemp", value="This is an instance of BlueTemp, an open sorce Discord Bot created by RedstonedLife", inline=False)
  embed.set_footer(text="A Template downloaded from Github")
  await ctx.send(embed=embed)

@bot.event
async def on_ready():
  print("Logged in as: " + bot.user.name + " " + "With the id: " + bot.user.id)
  print("---------------------------------------------------------------------")
  
bot.run(config.token) #This will run the bot with the token taken from config.py

