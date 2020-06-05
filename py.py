import discord
import os
import datetime


client = discord.Client()


@client.event
async def on_ready():
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("------------------")
  await client.change_presence(game=discord.Game(name='=help / =options 사용해주세요.', type=1))

@client.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, name="welcome")
  await channel.send(f"[member.mention]님 환영합니다!")

@client.event
async def on_message(message):
  if
    if message.content.startswith("!help"):
      
