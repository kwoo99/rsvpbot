import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
# Fetches token for the discord bot from env file 
load_dotenv()
TOKEN = os.getenv("bot_token")

# All bot commands will start with the prefix (!)
bot = commands.Bot(command_prefix = '(!)')

#----------------------------------------------------------------------------------------------------------------------
# Bot Commands
#----------------------------------------------------------------------------------------------------------------------
# Command for creating events in a discord server. Will prompt user to specify name of event, time of event, and details of event.
@bot.command()
async def create_event(ctx):
  await ctx.send("You have initiated an event creation.")

  await ctx.send("Please enter name of your event")
  msg_event_name = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
  
  await ctx.send("Please enter date and time your event")
  msg_event_date = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
  
  await ctx.send("Please list additional details for your event?")
  msg_event_details = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
  
  ctx.type = 'event'
  msg_event_final = await ctx.send("|EVENT|\n{} has created the event:\n{}\nEvent Date:\n{}\nEvent Details:\n{}".format
  (ctx.author.name, msg_event_name.content, msg_event_date.content, msg_event_details.content))
  
 # await msg_event_final.edit(type = 'event')

  print(msg_event_final.type)
  print(msg_event_final.id)
  print(ctx.type)
#----------------------------------------------------------------------------------------------------------------------
# Bot Events
#---------------------------------------------------------------------------------------------------------------------- 
# Detects if a member reacts to an event message with thumbs up or thumbs down and will prompt the bot to announce the user who reacted
@bot.event
async def on_reaction_add(reaction, user):
  channel = reaction.message.channel
  print(reaction.message.type)
  if(reaction.message.author == bot.user):
    print(reaction.message.id)
    if '|EVENT|' in reaction.message.content:
      if check_emoji(reaction.emoji, reaction.message.reactions, '👍'):
        await channel.send(f'{user.name} has confirmed that they will participate in this event')
      elif check_emoji(reaction.emoji, reaction.message.reactions, '👎'):
        await channel.send(f'{user.name} has confirmed that they will not participate in this event')
    else:
      print("Failed")
      print(reaction.message.type)
#---------------------------------------------------------------------------------------------------------------------- 
# Functions
#----------------------------------------------------------------------------------------------------------------------   
# Function that checks if a used emoji matches a desired emoji.
def check_emoji(emoji, message_reactions, desired_emoji):
  if any(reaction.emoji == desired_emoji for reaction in message_reactions):
    return True

  else:
    return False
#----------------------------------------------------------------------------------------------------------------------


# Runs the discord bot
bot.run(TOKEN)
