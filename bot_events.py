# bot_events
import discord
import bot
import check_emoji

#----------------------------------------------------------------------------------------------------------------------
# Detects if a member reacts to an event message with thumbs up or thumbs down and will prompt the bot to announce the user who reacted
@bot.event
async def on_reaction_add(reaction, user):
  channel = reaction.message.channel
  print(reaction.message.type)
  if(reaction.message.author == bot.user):
    print(reaction.message.id)
    if reaction.message.type == 'event':
      if check_emoji(reaction.emoji, reaction.message.reactions, '👍'):
        await channel.send(f'{user.name} has confirmed that they will participate in this event')
      elif check_emoji(reaction.emoji, reaction.message.reactions, '👎'):
        await channel.send(f'{user.name} has confirmed that they will not participate in this event')
    else:
      print("Failed")
      print(reaction.message.type)
#----------------------------------------------------------------------------------------------------------------------    