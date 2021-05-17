import discord
from discord.ext import commands

import random

from discord.ext.commands.core import command

client = commands.Bot(command_prefix='.')
token = "ODIzODIzMjc1MzUxOTk4NTI0.YFmbNg.pNTzTpOaCiJPtAjXP3VR8DNbBdA"

#유저 소지금 및 코인
userMoney = {}
userCoin = {}

#블랙잭
cardDeck = [1,2,3,4,5,6,7,8,9,10,11,12,13]
TableCard = {}
isBust = {}     #해당 유저가 버스트인지를 감지함
isStand = {}    #해당 유저가 스탠드인지를 감지함
isDouble = {}   #해당 유저가 더블인지를 감지함
blackJackUser = []  #플레이 유저를 넣는다.
blackJackCount = 0
DealerCard = []     #딜러(봇)의 패
blackJackGet = []   #돈 따는 사람 리스트

@client.event
async def on_ready():
    print("hello")

@client.command()
async def testImg(ctx):
    e = discord.Embed()
    e.set_image(url="https://www.codingfactory.net/wp-content/uploads/abc.jpg")
    await ctx.send(embed=e)
    
@client.command(pass_content=True)
async def blackJack(ctx, money, *userName: discord.Member):
    global blackJackCount
    if userName in TableCard:
        await ctx.send("아직 게임이 종료되지않았습니다!")
        return
    money = int(money)
    if (money < 100):
        await ctx.send("배팅금이 100이하입니다.")
        return
    blackJackCount = 0
    await ctx.send("배팅금은 " + str(money) + "입니다.")
    dr1 = random.choice(cardDeck)
    dr2 = random.choice(cardDeck)
    DealerCard.append(dr1)
    DealerCard.append(dr2)

    if dr1 == 1:
        dr1 = "A"
    if dr1 == 11:
        dr1 = "J"
    if dr1 == 12:
        dr1 = "Q"
    if dr1 == 13:
        dr1 = "K"

    await ctx.send("딜러의 보여진 카드는 " + str(dr1) + "입니다.")
    for i in userName:
        r1 = random.choice(cardDeck)
        r2 = random.choice(cardDeck)
        TableCard[i] = [r1, r2]

        if r1 == 1:
            r1 = "A"
        if r1 == 11:
            r1 = "J"
        if r1 == 12:
            r1 = "Q"
        if r1 == 13:
            r1 = "K"
        
        if r2 == 1:
            r2 = "A"
        if r2 == 11:
            r2 = "J"
        if r2 == 12:
            r2 = "Q"
        if r2 == 13:
            r2 = "K"

        await ctx.send(str(i) + "님의 카드는 " + str(r1) + ", " + str(r2))
        isBust[i] = False
        isStand[i] = False
        isDouble[i] = False
        blackJackUser.append(i)

@blackJack.error
async def blackJack_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("배팅금 혹은 플레이어가 미지정상태입니다!")
    if isinstance(error, commands.BadArgument):
        await ctx.send("배팅금 혹은 플레이어의 형태가 올바르지 못합니다!")

@client.command(pass_content=True)
async def hit(ctx, *, user: discord.Member):
    if user != ctx.author:
        await ctx.send("당신은 " + str(user) + "님이 아니십니다.")
        return
    global blackJackCount
    try:
        if isStand[user] or isDouble[user] == True:
            await ctx.send(str(user) + "님께서는 이미 선택을 마쳤습니다.")
            return
        elif isBust[user] == True:
            await ctx.send(str(user) + "님께서는 버스트 상태입니다.")
            return
        nextCard = random.choice(cardDeck)
        TableCard[user].append(nextCard)

        sum = 0
        for i in TableCard[user]:
            if i == 11:
                i = 10
            elif i == 12:
                i = 10
            elif i == 13:
                i = 10
            sum += i

        if nextCard == 1:
            nextCard = "A"
        if nextCard == 11:
            nextCard = "J"
        if nextCard == 12:
            nextCard = "Q"
        if nextCard == 13:
            nextCard = "K"
            
        await ctx.send(str(user) +"님이 히트를 요청하여 준 카드 :" + str(nextCard))
        
        if (sum > 21):
            await ctx.send(str(user) + "님께서 버스트 하셨습니다.")
            isBust[user] = True
            blackJackCount += 1
    except KeyError as e:
        await ctx.send("게임 참가자가 아닙니다.")

@hit.error
async def hit_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("게임 참가자가 아닙니다.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("배팅금 혹은 플레이어가 미지정상태입니다!")


@client.command()
async def stand(ctx, *, user: discord.Member):
    global blackJackCount
    try:
        if isStand[user] == True:
            await ctx.send(str(user) + "님께서는 이미 선택을 마쳤습니다.")
            return
        elif isBust[user] == True:
            await ctx.send(str(user) + "님께서는 버스트 상태입니다.")
            return
        await ctx.send(str(user) + "님이 스텐드를 하셨습니다.")
        isStand[user] = True
        blackJackCount += 1
    except KeyError:
        await ctx.send("게임 참가자가 아닙니다.")

@stand.error
async def stand_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("게임 참가자가 아닙니다.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("배팅금 혹은 플레이어가 미지정상태입니다!")

@client.command()
async def double(ctx, *, user: discord.Member):
    global blackJackCount
    try:
        if isStand[user] or isDouble[user] == True:
            await ctx.send(str(user) + "님께서는 이미 선택을 마쳤습니다.")
            return
        elif isBust[user] == True:
            await ctx.send(str(user) + "님께서는 버스트 상태입니다.")
            return
        nextCard = random.choice(cardDeck)
        TableCard[user].append(nextCard)

        sum = 0
        for i in TableCard[user]:
            if i == 11:
                i = 10
            elif i == 12:
                i = 10
            elif i == 13:
                i = 10
            sum += i

        if nextCard == 1:
            nextCard = "A"
        if nextCard == 11:
            nextCard = "J"
        if nextCard == 12:
            nextCard = "Q"
        if nextCard == 13:
            nextCard = "K"
            
        await ctx.send(str(user) +"님이 더블을 요청하여 준 카드 :" + str(nextCard))
        
        if (sum > 21):
            await ctx.send(str(user) + "님께서 버스트 하셨습니다.")
            isBust[user] = True
            blackJackCount += 1

        await ctx.send(str(user) + "님이 더블을 선택하셨습니다.")
        isDouble[user] = True
    except KeyError:
        await ctx.send("게임 참가자가 아닙니다.")

@double.error
async def double_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("게임 참가자가 아닙니다.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("배팅금 혹은 플레이어가 미지정상태입니다!")

@client.command()
async def blackJackEnd(ctx):
    global blackJackCount
    if blackJackCount < len(blackJackUser):
        await ctx.send("아직 모든 인원이 버스트 혹은 스탠드 상태가 아닙니다!")
        return
    sum = 0

    dGui1 = DealerCard[0]
    dGui2 = DealerCard[1]

    if dGui1 == 1:
        dGui1 = "A"
    if dGui1 == 11:
        dGui1 = "J"
    if dGui1 == 12:
        dGui1 = "Q"
    if dGui1 == 13:
        dGui1 = "K"

    if dGui2 == 1:
        dGui2 = "A"
    if dGui2 == 11:
        dGui2 = "J"
    if dGui2 == 12:
        dGui2 = "Q"
    if dGui2 == 13:
        dGui2 = "K"

    await ctx.send("딜러의 패는" + str(dGui1) + ", " + str(dGui2) + "입니다")
    if DealerCard[0] == 11:
        DealerCard[0] = 10
    if DealerCard[0] == 12:
        DealerCard[0] = 10
    if DealerCard[0] == 13:
        DealerCard[0] = 10

    if DealerCard[1] == 11:
        DealerCard[1] = 10
    if DealerCard[1] == 12:
        DealerCard[1] = 10
    if DealerCard[1] == 13:
        DealerCard[1] = 10
    sum = DealerCard[0] + DealerCard[1]

    while sum < 17 :
        dr1 = random.choice(cardDeck)

        dgui = dr1
        if dgui == 1:
            dgui = "A"
        if dgui == 11:
            dgui = "J"
        if dgui == 12:
            dgui = "Q"
        if dgui == 13:
            dgui = "K"

        await ctx.send("딜러의 총합이 17미만이기에 뽑은 카드 : " + str(dgui))
        if (dr1 == 11):
            dr1 = 10
        if (dr1 == 12):
            dr1 = 10
        if (dr1 == 13):
            dr1 = 10    
        sum += dr1

    player = 0
    for i in range(len(blackJackUser)):
        for j in TableCard[blackJackUser[i]]:
            player += j
        for j in TableCard[blackJackUser[i]]:
            if j == 1:
                if player >= 12:
                    player += 10
        if (sum < player and player <= 21):
            blackJackGet.append(blackJackUser[i].name)
        elif (sum > 21 and player <= 21):
            blackJackGet.append(blackJackUser[i].name)
        player = 0

    if (sum > 21):
        await ctx.send("딜러 버스트")
        await ctx.send("돈을 딴 플레이어" + str(blackJackGet))
    
    elif (sum == 21):
        await ctx.send("딜러 21!")
        await ctx.send("모든 돈은 딜러에게로 넘어갑니다.")

    else:
        await ctx.send("딜러 " + str(sum))
        await ctx.send("딜러보다 높고 버스트가 아닌 모든 사람에게 배팅금의 2배를 드립니다.")
        await ctx.send("돈을 딴 플레이어" + str(blackJackGet))
    
    blackJackUser.clear()
    isBust.clear()
    isStand.clear()
    isDouble.clear()
    TableCard.clear()
    blackJackGet.clear()
    blackJackCount = 0
    DealerCard.clear()

@client.event
async def on_command_error(ctx, error):
    await ctx.send("알 수 없는 명령어를 사용하셨습니다.")
    pass

client.run(token)