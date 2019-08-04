import discord
from discord.ext import commands
import asyncio
import os


#GIVE YOUR BOT A PREFIX; mine is a.
bot = commands.Bot(command_prefix="$")



#PRINT THE DISCORD BOT'S NAME WHEN IT'S READY
@bot.event
async def on_ready():
    print(f"{bot.user.name} is now running!")


@bot.command()
async def greet(msg,*users:discord.Member):
    #Can mention more than 1 user
    await msg.send(f"Hi there {" ".join[user.name for user in users]}")



@bot.command(aliases=['echo','copy','say'])
async def repeat(msg,*,message=None):
    if message == None:
        await msg.send("Please enter a message to repeat")

    else:
        await msg.send(f"{msg.author.name}: {message}")
  
#IF YOU WISH TO HOST YOUR CODE PUBLICALLY HIDE YOUR TOKEN VIA METHOD BELOW
#YOU CAN USE os.environ TO HIDE YOUR BOT TOKEN: SAVE YOUR BOT TOKEN AS THE NAME YOU GAVE IN os.environ['name'] ON HEROKU Config Vars
bot.run(os.environ['BOT_TOKEN'])
