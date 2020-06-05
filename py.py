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
  await client.change_presence(game=discord.Game(name='appealbot.xyz 하는 중', type=1))

@client.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, name="welcome")
  await channel.send(f"[member.mention]님 환영합니다!")

@client.event
async def on_message(message):
  if message.channel.is_private and message.author.id != "718421206059057234":
    if message.content == "!":
      await client.send_message(message.channel, "```올바르지 않는 명령어 형식입니다.```")
    else:
      if message.content[1:5] == "help":
        await client.send_message(message.channel, "Commands:\n```!help - Appeal Bot에 대한 명령어들을 확인합니다.\n!appeal (playerName) - 당신의 벤 또는 뮤트 항소를 합니다.\n!accept (discordID) - 해당 유저가 항소 한 것을 수락합니다. [관리자만]\n!deny (discordID) - 해당 유저가 항소 한 것을 거절합니다.```")
      if message.content[1:7] == "appeal":
        if message.content[8:]:
          await client.send_message(discord.utils.get(client.get_all_channels(), id="718434205448536066"), "@everyone\n[어필 정보]\n```유저 디스코드이름: " + message.author + "\n유저 디스코드아이디: " + message.author.id + "\n유저 마인크래프트닉네임: " + message.content[8:])
        else:
          await client.send_message(message.channel, "```해당 명령어는 해당 서버에서 사용이 불가능합니다.```")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
