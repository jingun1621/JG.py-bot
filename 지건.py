import discord
import asyncio
import datetime

client = discord.Client()

token = "ODI1MzI3NzMzMTg1MzE0ODQ3.YF8UWQ.tzRx7g4EkNe4nes1jV3mDqpTfg4"

@client.event
async def on_ready():

    print(client.user.name)
    print('bot online')
    game = discord.Game('지건 도움말')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "지건 도배":
        await message.channel.send(":x:이 명령어는 이 방에서 사용 불가인 명령어입니다!")  
     
    if message.content == "지건 도움말":
        embed = discord.Embed(colour=discord.Colour.red(), title="지건.py 봇 도움말", description="--------------------------")
        embed.add_field(name="지건 기능", value="을 입력시 기능 목록을 엽니다.", inline=False)
        embed.set_footer(text="by 최진건#4327")
        await message.channel.send(embed=embed)
    
    if message.content == "지건 기능":
        embed = discord.Embed(colour=discord.Colour.red(), title="지건.py 봇 기능 목록", description="--------------------------")
        embed.add_field(name="지건 프로필", value="을 입력시 사용자 프로필을 보여줍니다.", inline=False)
        embed.add_field(name="지건 도배", value="을 입력시 도배를 시작합니다", inline=False)
        embed.set_footer(text="by 최진건#4327")
        await message.channel.send(embed=embed)

    if message.content.startswith("지건 프로필"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed= discord.Embed(color=0x00ff00)
        embed.add_field(name="닉네임", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일",  inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "지건 제작자":
        embed = discord.Embed(colour=discord.Colour.red(), title="지건.py 봇 제작자", description="--------------------------")
        embed.add_field(name="제작", value="최진건#4327", inline=False)
        embed.set_footer(text="by 최진건#4327")
        await message.channel.send(embed=embed)
    if message.content == "ㅋㅋ":
        await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋ")  
    
    if message.content == "ㅋㅋㅋ":
        await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")  

    if message.content == "ㅋㅋㅋㅋ":
        await message.channel.send("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")  

    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(message)








client.run('ODI1MzI3NzMzMTg1MzE0ODQ3.YF8UWQ.tzRx7g4EkNe4nes1jV3mDqpTfg4')