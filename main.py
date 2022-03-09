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
  prefix = "spcc"
  story_channel = 123456789    ## replace with your story channel's id
  bot_id = 123456789           ## replace with your bot's user id

  channel = message.channel
  content = str(message.content).lower()


  # will only store user message if the message is posted in story channel 
  if channel.id == story_channel:
    if content in [f"{prefix} story so far", f"{prefix} story"]:
      with open ("messages.txt", "r") as story:
        story_text = story.read()
        story.close()

        await channel.send("**Story So far:**")

        # divide story in different messages to overcome message size limit
        while len(story_text) > 2000:
          i = 1999
          while story_text[i] != " ":
            i -= 1
          await channel.send(f"> {story_text[0:i]}")
          story_text = story_text[i:]
        await channel.send(f"> {story_text}")
  
    else:
      if message.author.id != bot_id:
        with open ("messages.txt", "a") as story:
          story.write(f"{content} ")
          story.close()
          print(content)
    

  else: 
    pass

client.run("token")
 