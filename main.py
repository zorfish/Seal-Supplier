import discord
from discord.ext import commands
import logging
from  dotenv import load_dotenv
import os
import random
import Seal_List


#get token
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

#Prints when bot online
@bot.event
async def on_ready():
    print("Bot is online")
    await bot.tree.sync()

#List of seals to be used by / command
seal_list = Seal_List.seals
#command to send a random seal
@bot.hybrid_command()
async def seal(ctx: commands.Context):
    #generates a random index
    random_seal_index: int = random.randint(0, len(seal_list) - 1)
    #logs seal command
    print(ctx.author, "used /seal with seal index", random_seal_index)
    #Sends seal message
    await ctx.send(seal_list[random_seal_index])

#run bot
bot.run(token, log_handler=handler, log_level=logging.DEBUG)