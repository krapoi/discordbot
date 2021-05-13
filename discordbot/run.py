from collections import UserString
import urllib
import random
from weakref import WeakKeyDictionary
import bs4
from discord import colour
from discord.embeds import Embed
import requests
import discord
import asyncio
import corona
from bs4 import BeautifulSoup
from discord.ext import commands, tasks
from requests.sessions import Request
token = ""
client = discord.Client()
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='help;'))
    print("시작!")

@client.event
async def on_message(msg):
    author = msg.author
    send = msg.channel.send
    content = msg.content

    if (author == client.user):
        pass

    if (content.startswith("help;")):
        embed = discord.Embed(
            title="봇 사용법",
            colour=0x62c1cc
        )
        embed.add_field(name="help;", value="도움말을 표시합니다", inline=False)
        embed.add_field(name="corona;", value="누적 확진자 수, 일일확진자 수를 확인합니다.", inline=False)
        embed.add_field(name="dice;", value="주사위를 굴립니다.", inline=False)
        embed.add_field(name="lolrd;", value="포지션에 상관없이 롤 랜덤 캐릭터를 추천 해줍니다.", inline=False)
        embed.add_field(name="rainrd;", value="레인보우식스시즈 랜덤 캐릭터를 추천 해줍니다.", inline=False)
        embed.add_field(name="bsrd;", value="블랙서바이벌 랜덤 캐릭터를 추천 해줍니다.", inline=False)
        await send(embed=embed)
    
    #코로나 확진자 크롤링
    if(content.startswith("corona;")):
        crawler = corona.krapoi()
        crawler.requestRun()
        r = crawler.requestReturn()
        embed = discord.Embed(
            title="확진자수",
            colour=0x62c1cc
            )
        embed.add_field(name="총 확진자수",value=r['today_domestic']+r['today_overseas'],inline=False)
        embed.add_field(name="국내 확진자수",value=r['today_domestic'],inline=False)  
        embed.add_field(name="해외유입 확진자수",value=r['today_overseas'],inline=False)  
        embed.add_field(name="누적 확진자수",value=r['accumulate_confirmed'],inline=False)  
        await send(embed=embed)

    #주사위 굴리기
    if(content.startswith("dice;")):
        randnum = random.randint(1, 6)  # 1이상 6이하 랜덤 숫자를 뽑음
        embed = discord.Embed(
            title="주사위",
            colour=0x62c1cc
        )
        embed.add_field(name=f'주사위 결과 입니다.',value=f'{randnum}',  inline=False)
        await send(embed=embed)
    

    #롤 랜덤캐 노가다.
    if (content.startswith('lolrd;')):
        rd = random.randint(1,155)
        if(rd == 1):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="가렌")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Garen_0.jpg")
            await send(embed=embed)
        elif(rd == 2): 
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="갈리오")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Galio_0.jpg")
            await send(embed=embed)
        elif(rd == 3):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="갱플랭크")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Gangplank_0.jpg")
            await send(embed=embed)
        elif(rd == 4):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="그라가스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Gragas_0.jpg")
            await send(embed=embed)
        elif(rd == 5):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="그레이브즈")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Graves_0.jpg")
            await send(embed=embed)
        elif(rd == 6):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="그웬")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Gwen_0.jpg")
            await send(embed=embed)
        elif(rd == 7):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="나르")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Gnar_0.jpg")
            await send(embed=embed)
        elif(rd == 8):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="나미")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nami_0.jpg")
            await send(embed=embed)
        elif(rd == 9):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="나서스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nasus_0.jpg")
            await send(embed=embed)
        elif(rd == 10):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="노틸러스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nautilus_0.jpg")
            await send(embed=embed)
        elif(rd == 11):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="녹턴")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nocturne_0.jpg")
            await send(embed=embed)
        elif(rd == 12):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="누누와 윌럼프")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nunu_0.jpg")
            await send(embed=embed)
        elif(rd == 13):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="니달리")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nidalee_0.jpg")
            await send(embed=embed)
        elif(rd == 14):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="니코")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Neeko_0.jpg")
            await send(embed=embed)
        elif(rd == 15):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="다리우스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Darius_0.jpg")
            await send(embed=embed)
        elif(rd == 16):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="다이애나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Diana_0.jpg")
            await send(embed=embed)
        elif(rd == 17):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="드레이븐")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Draven_0.jpg")
            await send(embed=embed)
        elif(rd == 18):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="라이즈")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ryze_0.jpg")
            await send(embed=embed)
        elif(rd == 19):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="라칸")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Rakan_0.jpg")
            await send(embed=embed)
        elif(rd == 20):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="람머스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Rammus_0.jpg")
            await send(embed=embed)
        elif(rd == 21):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="럭스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lux_0.jpg")
            await send(embed=embed)
        elif(rd == 22):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="럼블")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Rumble_0.jpg")
            await send(embed=embed)
        elif(rd == 23):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="레넥톤")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Renekton_0.jpg")
            await send(embed=embed)
        elif(rd == 24):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="레오나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Leona_0.jpg")
            await send(embed=embed)
        elif(rd == 25):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="렉사이")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/RekSai_0.jpg")
            await send(embed=embed)
        elif(rd == 26):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="렐")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Rell_0.jpg")
            await send(embed=embed)    
        elif(rd == 27):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="렝가")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Rengar_0.jpg")
            await send(embed=embed)
        elif(rd == 28):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="루시안")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lucian_0.jpg")
            await send(embed=embed)
        elif(rd == 29):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="룰루")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lulu_0.jpg")
            await send(embed=embed)
        elif(rd == 30):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="르블랑")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Leblanc_0.jpg")
            await send(embed=embed)
        elif(rd == 31):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="리신")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/LeeSin_0.jpg")
            await send(embed=embed)
        elif(rd == 32):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="리븐")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Riven_0.jpg")
            await send(embed=embed)
        elif(rd == 33):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="리산드라")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lissandra_0.jpg")
            await send(embed=embed)
        elif(rd == 34):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="릴리아")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lillia_0.jpg")
            await send(embed=embed)
        elif(rd == 35):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="마스터 이")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MasterYi_0.jpg")
            await send(embed=embed)
        elif(rd == 36):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="마오카이")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Maokai_0.jpg")
            await send(embed=embed)
        elif(rd == 37):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="말자하")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Malzahar_0.jpg")
            await send(embed=embed)
        elif(rd == 38):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="말파이트")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Malphite_0.jpg")
            await send(embed=embed)
        elif(rd == 39):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="모데카이저")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Mordekaiser_0.jpg")
            await send(embed=embed)
        elif(rd == 40):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="모르가나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Morgana_0.jpg")
            await send(embed=embed)
        elif(rd == 41):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="문도 박사")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/DrMundo_0.jpg")
            await send(embed=embed)
        elif(rd == 42):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="미스 포츈")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MissFortune_0.jpg")
            await send(embed=embed)
        elif(rd == 43):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="바드")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Bard_0.jpg")
            await send(embed=embed)
        elif(rd == 44):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="바루스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Varus_0.jpg")
            await send(embed=embed)
        elif(rd == 45):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="바이")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Vi_0.jpg")
            await send(embed=embed)
        elif(rd == 46):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="베이가")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Veigar_0.jpg")
            await send(embed=embed)
        elif(rd == 47):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="베인")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Vayne_0.jpg")
            await send(embed=embed)
        elif(rd == 48):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="벨코즈")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Velkoz_0.jpg")
            await send(embed=embed)
        elif(rd == 49):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="볼리베어")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Volibear_0.jpg")
            await send(embed=embed)
        elif(rd == 50):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="브라움")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Braum_0.jpg")
            await send(embed=embed)
        elif(rd == 51):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="브랜드")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Brand_0.jpg")
            await send(embed=embed)
        elif(rd == 52):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="블라디미르")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Vladimir_0.jpg")
            await send(embed=embed)
        elif(rd == 53):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="블리츠크랭크")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Blitzcrank_0.jpg")
            await send(embed=embed)
        elif(rd == 54):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="비에고")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Viego_0.jpg")
            await send(embed=embed)
        elif(rd == 55):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="빅토르")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Viktor_0.jpg")
            await send(embed=embed)
        elif(rd == 56):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="뽀삐")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Poppy_0.jpg")
            await send(embed=embed)
        elif(rd == 57):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="사미라")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Samira_0.jpg")
            await send(embed=embed)
        elif(rd == 58):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="사이온")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sion_0.jpg")
            await send(embed=embed)
        elif(rd == 59):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="사일러스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sylas_0.jpg")
            await send(embed=embed)
        elif(rd == 60):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="샤코")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Shaco_0.jpg")
            await send(embed=embed)
        elif(rd == 61):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="세나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Senna_0.jpg")
            await send(embed=embed)
        elif(rd == 62):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="세라핀")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Seraphine_0.jpg")
            await send(embed=embed)
        elif(rd == 63):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="세주아니")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sejuani_0.jpg")
            await send(embed=embed)
        elif(rd == 64):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="세트")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sett_0.jpg")
            await send(embed=embed)
        elif(rd == 65):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="소나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sona_0.jpg")
            await send(embed=embed)
        elif(rd == 66):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="소라카")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Soraka_0.jpg")
            await send(embed=embed)
        elif(rd == 67):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="쉔")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Shen_0.jpg")
            await send(embed=embed)
        elif(rd == 68):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="쉬바나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Shyvana_0.jpg")
            await send(embed=embed)
        elif(rd == 69):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="스웨인")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Swain_0.jpg")
            await send(embed=embed)
        elif(rd == 70):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="스카너")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Skarner_0.jpg")
            await send(embed=embed)
        elif(rd == 71):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="시비르")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sivir_0.jpg")
            await send(embed=embed)
        elif(rd == 72):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="신 짜오")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/XinZhao_0.jpg")
            await send(embed=embed)
        elif(rd == 73):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="신드라")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Syndra_0.jpg")
            await send(embed=embed)
        elif(rd == 74):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="신지드")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Singed_0.jpg")
            await send(embed=embed)
        elif(rd == 75):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="쓰레쉬")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Thresh_0.jpg")
            await send(embed=embed)
        elif(rd == 76):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아리")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_0.jpg")
            await send(embed=embed)
        elif(rd ==77):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아무무")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Amumu_0.jpg")
            await send(embed=embed)
        elif(rd == 78):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아우렐리온 솔")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/AurelionSol_0.jpg")
            await send(embed=embed)
        elif(rd == 79):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아이번")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ivern_0.jpg")
            await send(embed=embed)
        elif(rd == 80):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아지르")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Azir_0.jpg")
            await send(embed=embed)
        elif(rd == 81):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아칼리")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Akali_0.jpg")
            await send(embed=embed)
        elif(rd == 82):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아트록스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aatrox_0.jpg")
            await send(embed=embed)
        elif(rd == 83):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아펠리오스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Aphelios_0.jpg")
            await send(embed=embed)
        elif(rd == 84):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="알리스타")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Alistar_0.jpg")
            await send(embed=embed)
        elif(rd == 85):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="애니")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Annie_0.jpg")
            await send(embed=embed)
        elif(rd == 86):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="애니비아")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Anivia_0.jpg")
            await send(embed=embed)
        elif(rd == 87):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="애쉬")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ashe_0.jpg")
            await send(embed=embed)
        elif(rd == 88):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="야스오")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yasuo_0.jpg")
            await send(embed=embed)
        elif(rd == 89):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="에코")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ekko_0.jpg")
            await send(embed=embed)
        elif(rd == 90):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="엘리스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Elise_0.jpg")
            await send(embed=embed)
        elif(rd == 91):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="오공")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MonkeyKing_0.jpg")
            await send(embed=embed)
        elif(rd == 92):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="오른")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ornn_0.jpg")
            await send(embed=embed)
        elif(rd == 93):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="오리아나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Orianna_0.jpg")
            await send(embed=embed)
        elif(rd == 94):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="올라프")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Olaf_0.jpg")
            await send(embed=embed)
        elif(rd == 95):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="요네")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yone_0.jpg")
            await send(embed=embed)
        elif(rd == 96):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="요릭")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yorick_0.jpg")
            await send(embed=embed)
        elif(rd == 97):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="우디르")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Udyr_0.jpg")
            await send(embed=embed)
        elif(rd == 98):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="우르곳")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Urgot_0.jpg")
            await send(embed=embed)
        elif(rd == 99):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="워윅")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Warwick_0.jpg")
            await send(embed=embed)
        elif(rd == 100):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="유미")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yuumi_0.jpg")
            await send(embed=embed)
        elif(rd == 101):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="이렐리아")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Irelia_0.jpg")
            await send(embed=embed)
        elif(rd == 102):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="이블린")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Evelynn_0.jpg")
            await send(embed=embed)
        elif(rd == 103):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="이즈리얼")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ezreal_0.jpg")
            await send(embed=embed)
        elif(rd == 104):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="일라오이")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Illaoi_0.jpg")
            await send(embed=embed)
        elif(rd == 105):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="자르반 4세")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/JarvanIV_0.jpg")
            await send(embed=embed)
        elif(rd == 106):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="자야")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Xayah_0.jpg")
            await send(embed=embed)
        elif(rd == 107):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="자이라")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zyra_0.jpg")
            await send(embed=embed)
        elif(rd == 108):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="자크")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zac_0.jpg")
            await send(embed=embed)
        elif(rd == 109):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="잔나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Janna_0.jpg")
            await send(embed=embed)
        elif(rd == 110):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="잭스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jax_0.jpg")
            await send(embed=embed)
        elif(rd == 111):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="제드")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zed_0.jpg")
            await send(embed=embed)
        elif(rd == 112):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="제라스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Xerath_0.jpg")
            await send(embed=embed)
        elif(rd == 113):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="제이스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jayce_0.jpg")
            await send(embed=embed)
        elif(rd == 114):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="조이")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zoe_0.jpg")
            await send(embed=embed)
        elif(rd == 115):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="직스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ziggs_0.jpg")
            await send(embed=embed)
        elif(rd == 116):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="진")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jhin_0.jpg")
            await send(embed=embed)
        elif(rd == 117):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="질리언")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zilean_0.jpg")
            await send(embed=embed)
        elif(rd == 118):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="징크스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jinx_0.jpg")
            await send(embed=embed)
        elif(rd == 119):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="초가스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Chogath_0.jpg")
            await send(embed=embed)
        elif(rd == 120):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카르마")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Karma_0.jpg")
            await send(embed=embed)
        elif(rd == 121):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카밀")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Camille_0.jpg")
            await send(embed=embed)
        elif(rd == 122):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카사딘")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kassadin_0.jpg")
            await send(embed=embed)
        elif(rd == 123):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카서스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Karthus_0.jpg")
            await send(embed=embed)
        elif(rd == 124):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카시오페아")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Cassiopeia_0.jpg")
            await send(embed=embed)
        elif(rd == 125):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카이사")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kaisa_0.jpg")
            await send(embed=embed)
        elif(rd == 126):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카직스")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Khazix_0.jpg")
            await send(embed=embed)
        elif(rd == 127):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카타리나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Katarina_0.jpg")
            await send(embed=embed)
        elif(rd == 128):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="칼리스타")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kalista_0.jpg")
            await send(embed=embed)
        elif(rd == 129):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="케넨")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kennen_0.jpg")
            await send(embed=embed)
        elif(rd == 130):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="케이틀린")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Caitlyn_0.jpg")
            await send(embed=embed)
        elif(rd == 131):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="케인")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kayn_0.jpg")
            await send(embed=embed)
        elif(rd == 132):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="케일")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kayle_0.jpg")
            await send(embed=embed)
        elif(rd == 133):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="코그모")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/KogMaw_0.jpg")
            await send(embed=embed)
        elif(rd == 134):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="코르키")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Corki_0.jpg")
            await send(embed=embed)
        elif(rd == 135):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="퀸")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Quinn_0.jpg")
            await send(embed=embed)
        elif(rd == 136):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="클레드")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kled_0.jpg")
            await send(embed=embed)
        elif(rd == 137):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="키아나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Qiyana_0.jpg")
            await send(embed=embed)
        elif(rd == 138):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="킨드레드")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kindred_0.jpg")
            await send(embed=embed)
        elif(rd == 139):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="타릭")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Taric_0.jpg")
            await send(embed=embed)
        elif(rd == 140):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="탈론")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Talon_0.jpg")
            await send(embed=embed)
        elif(rd == 141):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="탈리야")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Taliyah_0.jpg")
            await send(embed=embed)
        elif(rd == 142):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="탐 켄치")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/TahmKench_0.jpg")
            await send(embed=embed)
        elif(rd == 143):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="트런들")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Trundle_0.jpg")
            await send(embed=embed)
        elif(rd == 144):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="트리스타나")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Tristana_0.jpg")
            await send(embed=embed)
        elif(rd == 145):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="트린다미어(손잡이)")
            embed.set_image(url= "https://cdn.discordapp.com/attachments/842219802096697347/842219866622001172/hand.PNG")
            await send(embed=embed)
        elif(rd == 146):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="트위스티드 페이트")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/TwistedFate_0.jpg")
            await send(embed=embed)
        elif(rd == 147):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="트위치")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Twitch_0.jpg")
            await send(embed=embed)
        elif(rd == 148):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="티모")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Teemo_0.jpg")
            await send(embed=embed)
        elif(rd == 149):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="파이크")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Pyke_0.jpg")
            await send(embed=embed)
        elif(rd == 150):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="판테온")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Pantheon_0.jpg")
            await send(embed=embed)
        elif(rd == 151):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="피들스틱")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fiddlesticks_0.jpg")
            await send(embed=embed)
        elif(rd == 152):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="피오라")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fiora_0.jpg")
            await send(embed=embed)
        elif(rd == 153):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="피즈")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fizz_0.jpg")
            await send(embed=embed)
        elif(rd == 154):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="하이머딩거")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Heimerdinger_0.jpg")
            await send(embed=embed)
        elif(rd == 155):
            embed = discord.Embed(
                title="롤 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="헤카림")
            embed.set_image(url= "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Hecarim_0.jpg")
            await send(embed=embed)
    
    if (content.startswith("rainrd")):
            embed = discord.Embed(title="레인보우식스 랜덤캐", color=0xc1cc)
            embed.add_field(name="⚔️", value="공격팀", inline=False)
            embed.add_field(name="🛑", value="수비팀", inline=False)
            rainbow = await msg.channel.send(embed=embed)
            await rainbow.add_reaction("⚔️") #stun
            await rainbow.add_reaction("🛑") #step
    
    if(content.startswith("bsrd;")):
        randbs = random.randint(1,28)
        if(randbs == 1):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="재키")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270497035255808/jack.png")
            await send(embed=embed)
        elif(randbs == 2):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아야")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270392251973692/aya.png")
            await send(embed=embed)
        elif(randbs == 3):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="현우")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270479733751818/hyun.png")
            await send(embed=embed)
        elif(randbs == 4):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="매그너스")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270530588377108/mag.png")
            await send(embed=embed)
        elif(randbs == 5):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="피오라")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270546640371742/piora.png")
            await send(embed=embed)
        elif(randbs == 6):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="나딘")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270536919023626/nadin.png")
            await send(embed=embed)
        elif(randbs == 7):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="자히르")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270506019454986/jahir.png")
            await send(embed=embed)
        elif(randbs == 8):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="하트")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270463303483392/heart.png")
            await send(embed=embed)
        elif(randbs == 9):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아이솔")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270487387439104/isol.png")
            await send(embed=embed)
        elif(randbs == 10):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="리다이린")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270553599377418/redirin.png")
            await send(embed=embed)
        elif(randbs == 11):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="유키")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270376733835264/yuki.png")
            await send(embed=embed)
        elif(randbs == 12):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="혜진")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270472112701491/hyeajin.png")
            await send(embed=embed)
        elif(randbs == 13):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="쇼우")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270579985350656/shou.png")
            await send(embed=embed)
        elif(randbs == 14):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="시셀라")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270599556497419/sisella.png")
            await send(embed=embed)
        elif(randbs == 15):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="키아라")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270515334086736/kiara.png")
            await send(embed=embed)
        elif(randbs == 16):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아드리아나")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270443062034432/driana.png")
            await send(embed=embed)
        elif(randbs == 17):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="쇼이치")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270586255179807/showich.png")
            await send(embed=embed)
        elif(randbs == 18):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="실비아")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270593663762442/silvia.png")
            await send(embed=embed)
        elif(randbs == 19):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="엠마")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270453199274004/emma.png")
            await send(embed=embed)
        elif(randbs == 20):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="레녹스")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270523555577866/lenox.png")
            await send(embed=embed)
        elif(randbs == 21):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="로지")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270561190150144/rogi.png")
            await send(embed=embed)
        elif(randbs == 22):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="루크")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270572247646248/ruke.png")
            await send(embed=embed)
        elif(randbs == 23):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="캐시")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270421231206420/cash.png")
            await send(embed=embed)
        elif(randbs == 24):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아델라")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270432810893362/della.png")
            await send(embed=embed)
        elif(randbs == 25):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="버니스")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270411298439168/burnis.png")
            await send(embed=embed)
        elif(randbs == 26):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="바바라")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270401128300594/babara.png")
            await send(embed=embed)
        elif(randbs == 27):
            embed = discord.Embed(
            title="블서 랜덤캐",
            colour=0xc1cc
            )
            embed.add_field(name="추천",value="알렉스")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270383401861190/Alex.png")
            await send(embed=embed)
        elif(randbs == 28):
            embed = discord.Embed(
                title="블서 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="수아")
            embed.set_image(url="https://cdn.discordapp.com/attachments/842270328717574144/842270606158463016/sua.png")
            await send(embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    rdnum2 = random.randint(1, 30)
    rdnum = random.randint(1, 29)
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "⚔️":
        if(rdnum2 == 1):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="슬레지")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-sledge.00141f92.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 2):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="대처")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-thatcher.b1cac8e7.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 3):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="애쉬")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-ash.16913d82.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 4):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="써마이트")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-thermite.9010fa33.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 5):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="트위치")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-twitch.83cbfa97.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 6):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="몽타뉴")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-montagne.2078ee84.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 7):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="글라즈")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-glaz.43dd3bdf.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 8):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="퓨즈")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-fuze.9e7e9222.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 9):
            embed = discord.Embed(
            title="레식 랜덤캐",
            colour=0xc1cc
        )
            embed.add_field(name="추천",value="블리츠")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-blitz.cd45df08.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 10):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아이큐")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-iq.b1acee1a.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 11):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="벅")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-buck.2fc3e097.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 12):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="블랙비어드")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-blackbeard.fccd7e2c.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 13):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카피탕")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-capitao.6603e417.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 14):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="히바나")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-hibana.c2a8477d.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 15):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="자칼")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-jackal.0326ca29.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 16):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="잉")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-ying.b88be612.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 17):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="조피아")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-zofia.2a892bf5.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 18):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="도깨비")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-dokkaebi.2f83a34f.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 19):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="라이온")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-lion.69637075.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 20):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="핀카")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-finka.71d3a243.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 21):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="매버릭")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-maverick.7eab7c75.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 22):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="노매드")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-nomad.dbd9a315.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 23):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="그리드락")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-gridlock.6b572bdc.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 24):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="뇌크")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-nakk.d3b4f1af.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 25):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아마루")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-amaru.24a70133.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 26):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="칼리")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-kali.ff0fee46.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 27):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="야나")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-iana.6fa68bc8.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 28):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="에이스")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-ace.f898bd77.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 29):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="제로")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-zero.050263d1.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum2 == 30):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="플로레스")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/842219802096697347/842224030941708338/flores.png")
            await reaction.message.channel.send(embed=embed)
    if str(reaction.emoji) == "🛑":
        if(rdnum == 1):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="스모크")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-smoke.874e9888.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 2):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="뮤트")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-mute.3e4f2b01.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 3):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="캐슬")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-castle.378f8f4e.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 4):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="펄스")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-pulse.9de627c5.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 5):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="닥")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-doc.29fe751b.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 6):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="룩")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-rook.eb954a4e.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 7):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="캅칸")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-kapkan.562d0701.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 8):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="타찬카")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-tachanka.ae7943f0.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 9):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="예거")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-jager.600b2773.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 10):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="밴딧")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-bandit.385144d9.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 11):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="프로스트")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-frost.e5362220.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 12):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="발키리")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-valkyrie.f87cb6bd.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 13):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카베이라")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-caveira.757e9259.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 14):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="에코")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-echo.a77c7d7e.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 15):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="미라")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-mira.22fb72a5.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 16):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="리전")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-lesion.07c3d352.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 17):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="엘라")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-ela.63ec2d26.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 18):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="비질")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-vigil.4db5385b.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 19):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="마에스트로")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-maestro.b6cf7905.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 20):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="알리바이")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-alibi.7fba8d33.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 21):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="클래시")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-clash.133f243d.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 22):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="카이드")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-kaid.ae2bfa7a.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 23):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="모찌")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-mozzie.adeac188.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 24):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="워든")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-warden.fd12fbd9.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 25):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="고요")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-goyo.3e765688.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 26):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="와마이")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-wamai.4e4bf506.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 27):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="오릭스")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-oryx.6472c8ee.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 28):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="멜루시")
            embed.set_thumbnail(url="https://r6.op.gg/images/operators/badges/badge-melusi.f93b3d64.png")
            await reaction.message.channel.send(embed=embed)
        elif(rdnum == 29):
            embed = discord.Embed(
                title="레식 랜덤캐",
                colour=0xc1cc
            )
            embed.add_field(name="추천",value="아루니")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/842219802096697347/842227716166254662/aruni.png")
            await reaction.message.channel.send(embed=embed)

    

        



client.run(token)