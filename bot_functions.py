# bot_functions
import discord
import bot

#----------------------------------------------------------------------------------------------------------------------
# Function that checks if a used emoji matches a desired emoji.
def check_emoji(emoji, message_reactions, desired_emoji):
  if any(reaction.emoji == desired_emoji for reaction in message_reactions):
    return True

  else:
    return False
#----------------------------------------------------------------------------------------------------------------------
