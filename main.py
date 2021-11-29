# main.py
import os
import bot
from dotenv import load_dotenv
# Fetches token for the discord bot from env file 
load_dotenv()
TOKEN = os.getenv("bot_token")

# Runs the discord bot
bot.run(TOKEN)