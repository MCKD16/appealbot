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
  await client.change_presence(game=discord.Game(name='appealbot.xyz', type=1))

@client.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, name="welcome")
  await channel.send(f"[member.mention]님 환영합니다!")

@client.event
async def on_message(message):
  if message.content == "!":
    if message.channel.is_private and message.author.id != "718421206059057234":
      await client.send_message(message.channel, "```올바르지 않는 명령어 형식입니다.```")
  else:
    if message.content[1:5] == "help":
      if message.channel.is_private and message.author.id != "718421206059057234":
        await client.send_message(message.channel, "Commands:\n```!help - Appeal Bot에 대한 명령어들을 확인합니다.\n!appeal (playerName) - 당신의 벤 또는 뮤트 항소를 합니다.\n!accept (discordID) - 해당 유저가 항소 한 것을 수락합니다. [관리자만]\n!deny (discordID) - 해당 유저가 항소 한 것을 거절합니다.```")
    if message.content[1:7] == "appeal":
      if message.channel.is_private and message.author.id != "718421206059057234":
        if message.content[8:]:
          await client.send_message(discord.utils.get(client.get_all_channels(), id="718434205448536066"), "@everyone\n[ " + message.author + "님의 항소 정보 ]```디스코드 이름: " + message.author + "\n디스코드 아이디: " + message.author.id + "\n마인크래프트 닉네임: " + message.content[8:] + "```")
        else:
          await client.send_message(message.channel, "```마인크래프트 닉네임을 작성하여 주세요.```")
    if message.content[1:7] == "accept":
        if message.author.id == "623502843558756394":
          if message.content[8:24]:
            member = discord.utils.get(client.get_all_members(), id=message.content[8:24])
            await client.send_message(member, "[ 항소가 수락되셨습니다! ]\n```[ 수락자 디스코드 이름: " + message.author + "\n\n당신의 항소가 성공적으로 수락되었습니다.\n당신은 이제 서버에 접속이 가능하며, 서버의 규칙을 안지킬 시에 영구벤이 됩니다.\n그점 유의하여 주시길 바랍니다.```")
            await client.send_message(message.channel, "```성공적으로 해당 유저의 항소가 수락되었습니다.```")
          else:
           await client.send_message(message.channel, "```수락할 유저의 디스코드 아이디를 적어주세요.```")
    if message.author.id == "310659823211511809":
      if message.content[8:24]:
        member = discord.utils.get(client.get_all_members(), id=message.content[8:24])
        await client.send_message(member, "[ 항소가 수락되셨습니다! ]\n```[ 수락자 디스코드 이름: " + message.author + "\n\n당신의 항소가 성공적으로 수락되었습니다.\n당신은 이제 서버에 접속이 가능하며, 서버의 규칙을 안지킬 시에 영구벤이 됩니다.\n그점 유의하여 주시길 바랍니다.```")
        await client.send_message(message.channel, "```성공적으로 해당 유저의 항소가 수락되었습니다.```")
      else:
        await client.send_message(message.channel, "```수락할 유저의 디스코드 아이디를 적어주세요.```")
    if message.author.id == "584251780263575572":
      if message.content[8:24]:
        member = discord.utils.get(client.get_all_members(), id=message.content[8:24])
        await client.send_message(member, "[ 항소가 수락되셨습니다! ]\n```[ 수락자 디스코드 이름: " + message.author + "\n\n당신의 항소가 성공적으로 수락되었습니다.\n당신은 이제 서버에 접속이 가능하며, 서버의 규칙을 안지킬 시에 영구벤이 됩니다.\n그점 유의하여 주시길 바랍니다.```")
        await client.send_message(message.channel, "```성공적으로 해당 유저의 항소가 수락되었습니다.```")
      else:
        await client.send_message(message.channel, "```수락할 유저의 디스코드 아이디를 적어주세요.```")
    if message.author.id == "546583591056965634":
      if message.content[8:24]:
        member = discord.utils.get(client.get_all_members(), id=message.content[8:24])
        await client.send_message(member, "[ 항소가 수락되셨습니다! ]\n```[ 수락자 디스코드 이름: " + message.author + "\n\n당신의 항소가 성공적으로 수락되었습니다.\n당신은 이제 서버에 접속이 가능하며, 서버의 규칙을 안지킬 시에 영구벤이 됩니다.\n그점 유의하여 주시길 바랍니다.```")
        await client.send_message(message.channel, "```성공적으로 해당 유저의 항소가 수락되었습니다.```")
      else:
        await client.send_message(message.channel, "```수락할 유저의 디스코드 아이디를 적어주세요.```")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
