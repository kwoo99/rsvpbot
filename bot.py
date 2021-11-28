# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("bot_token")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    channel = client.get_channel(914337815372910592)
    await channel.send("@everyone\nHello Everyone, I am your new RSVP Bot. I my job is to handle RSVP functions for server events.\nThank you for inviting me to your server!")

@client.event
async def on_reaction_add(reaction, user):
  channel = reaction.message.channel
  #print(reaction.message.reactions)
  if check_emoji(reaction.emoji, reaction.message.reactions, '👍'):
    #print("Detected")
    await channel.send('{} has confirmed that they will participate in this event'.format(user.name))
  elif check_emoji(reaction.emoji, reaction.message.reactions, '👎'):
    #print("Detected")
    await channel.send('{} has confirmed that they will not participate in this event'.format(user.name))
    

def check_emoji(emoji, message_reactions, desired_emoji):
  if any(reaction.emoji == desired_emoji for reaction in message_reactions):
    #print("Confirmed")
    return True

  else:
    #print("Denied")
    return False

client.run(TOKEN)
