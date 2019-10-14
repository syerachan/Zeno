import discord
from discord.ext import commands
import asyncio
import os


#GIVE YOUR BOT A PREFIX; mine is a.
bot = commands.Bot(command_prefix="s.")



#PRINT THE DISCORD BOT'S NAME WHEN IT'S READY
@bot.event
async def on_ready():
    print(f"{bot.user.name} is now running!")



	
#A SIMPLE TEST COMMAND
@bot.command(pass_context=True)
async def hi(ctx):
	"""
	Sends Hi with the user of the user that used the command
	"""
	await bot.say(f"Hello there{ctx.message.author.display_name}")
  


@bot.command(pass_context=True,name='copy')
async def _copy(ctx,*,msg):
	"""
	Repearts what ever the user tpyes after s.copy
	"""
	await bot.say(msg) #Send the messages



bot.run(os.environ['BOT_TOKEN'])
