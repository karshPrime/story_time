#!/usr/bin/env python
import discord
from discord.ext import commands
from discord import Embed
from random import randint

# INITIALIZE
intents = discord.Intents.default()
intents.members=True
client = commands.Bot(command_prefix='?', case_insensitive=True, intents = intents)
client.remove_command("help")

# PRINT MESSAGE ON ACTIVATION
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('Story Time'))
  print("bot is online")

# COMMANDS
@client.event
async def on_message(message):
  prefix = "bot"
  story_channel = 123456789 # enter your channel id

  channel = message.channel
  content = str(message.content).lower()


  # will only store user message if the message is posted in story channel 
  if channel.id == story_channel:
    if content in [f"{prefix} story so far", f"{prefix} story"]:
        pass
    else:
        pass


client.run("token")
