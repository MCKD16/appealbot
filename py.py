import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print("login")
  print("------------------")
  await client.change_presence(game=discord.Game(name='안녕하세요.', type=1))

@client.event
async def on_message(message):
  if message.channel.is_private and message.author.id != "733310767973138553":
    if message.content == "!":
      await client.send_message(message.channel, "```정확하지 않은 명령어입니다.```")
    else:
      if message.content[1:4] == "말하기":
        if message.author.id == "623502843558756394":
          if message.content[8:]:
            await client.send_message(discord.utils.get(client.get_all_channels(), id="713704015384543262"), "@everyone\n```" + message.content[8:] + "```")
          else:
            await client.send_message(message.channel, "```보낼 메세지를 적어주세요.```")
        else:
          await client.send_message(message.channel, "```당신은 이 명령어를 사용할 권한이 없습니다.```")


access_token = os.environ["TOKEN"]
client.run(access_token)
