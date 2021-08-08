import discord
from discord.ext import commands
import os
import random

client = commands.Bot(command_prefix = '-')


@client.event
async def on_message(message):
    # 받은 메시지의 author 가 bot 인 경우 return
    if message.author.user:
        channel = message.channel
        num=random.randint(1,4)
        if num==1:
            asw="어?"
            await channel.send(asw)
            asw="귀여워."
            await channel.send(asw)
            return None
        if num==2:
            asw="아, 미안해요. 내가 사랑 앞엔 저돌적이라."
            await channel.send(asw)
            return None
        if num==3:
            asw="꺼피 한잔 할래요옹~"
            await channel.send(asw)
            return None
        if num==4:
            asw="오늘밤 준며들고, 적셔들기로 나와 약속~"
            await channel.send(asw)
            return None
        if num==5:
            asw="별자리 뭐에요? 난 당신 옆자리."
            await channel.send(asw)
            return None
        if num==6:
            asw="당신 정말 이쁘다. 호호호호훟훟"
            await channel.send(asw)
            return None
        if num==7:
            asw="당신, 우유 좋아해요? 난 우유 좋아하는데.."
            await channel.send(asw)
            asw="아이럽우유"
            await channel.send(asw)
            return None
        if num==8:
            asw="부끄러워하지 말아요 바보."
            await channel.send(asw)
            asw="이 바보야!! 바!보!! 바!!!!보!!!!!"
            await channel.send(asw)
            return None
        if num==9:
            asw="안녕? 꼬마아가씨"
            await channel.send(asw)
            return None
        if num==10:
            asw="흫흐흫"
            await channel.send(asw)
            return None
        if num==11:
            asw="미안 내가 너무,,,매력적이지?"
            await channel.send(asw)
            sw="우리 꼬마아가씨,,"
            await channel.send(asw)
            asw="그래도 나 임자있으니까"
            await channel.send(asw)
            asw="넘보지 않기로? 약속~"
            await channel.send(asw)
            return None
        if num==12:
            asw="잘 부탁하 꼬마아가씨^^"
            await channel.send(asw)
            return None
        if num==13:
            asw="어? 더 이쁘다"
            await channel.send(asw)
            asw="귀여운 꼬마아가씨"
            await channel.send(asw)
            return None
        if num==14:
            asw="사랑은 공격적이니까, 표현을 아끼지 않아요^^"
            await channel.send(asw)
            asw="미안, 너무 공격적이었죠"
            await channel.send(asw)
            asw="부끄러워하지말아요"
            await channel.send(asw)
            return None
        if num==15:
            asw="당신, 왜 이렇게 안 착해?"
            await channel.send(asw)
            asw="내 마음 속에 안착"
            await channel.send(asw)
            return None
        if num==16:
            asw="잘 자요, 꼬마아가씨"
            await channel.send(asw)
            return None
        if num==17:
            asw="우리 집에서 고양이 보고 갈래?"
            await channel.send(asw)
            return None

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="유혹"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("귀엽네")
  client.run(os.environ['token'])