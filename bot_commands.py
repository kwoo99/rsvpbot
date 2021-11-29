# bot_commands
import discord
from discord.ext import commands

# All bot commands will start with the prefix (!)
global bot
bot = commands.Bot(command_prefix = '(!)')

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
  msg_event_final = await ctx.send("{} has created the event: {}\nEvent Date:\n{}\nEvent Details:\n{}".format
  (ctx.author.name, msg_event_name.content, msg_event_date.content, msg_event_details.content))
  
  await msg_event_final.edit(type = 'event')

  print(msg_event_final.type)
  print(msg_event_final.id)
  print(ctx.type)
  #----------------------------------------------------------------------------------------------------------------------