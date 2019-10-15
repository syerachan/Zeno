import discord
from discord.ext import commands
import asyncio
import time


client = commands.Bot(command_prefix = "+")


@client.event
async def on_ready():
    print(f'Logged on as {client.user}')




async def statuschange():
  await client.wait_until_ready()


  while True:
    await client.change_presence(activity=discord.Activity(name='+help', type=discord.ActivityType.streaming))

    await asyncio.sleep(10)



client.loop.create_task(statuschange())
client.run('NjMzNDIyNTA4MjQ2NDMzNzky.XaV1bQ.OnKFLqhSUzo19EM4jL91Eb8Qmd4')
