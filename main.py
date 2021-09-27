import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import discord
import random

token = "토큰"
bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print("준비완료")
    print(bot.user)
    game = discord.Game("테스트")
    await bot.change_presence(status=discord.Status.online, activity=game)
@bot.command()
async def 주사위(ctx, number):
    try:
        await ctx.send(f"{number}면이있는 주사위를 돌려{random.randint(1, int(number))}가 나왔어요!")
    except:
        await ctx.send("명령어를 잘못 입력하셨어요")
@bot.command()
async def 공지(ctx):
    msg = ctx.message.content[3:]         
    embed = discord.Embed(title="공지🔈", description = msg, color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def 뉴스(ctx):
    inp = ctx.message.content[3:]
    url = f"https://search.naver.com/search.naver?query={inp}&where=news&ie=utf8&sm=nws_hty"
    res = requests.get(url)
    res.raise_for_status
    soup = BeautifulSoup(res.text, "lxml")
    titles = soup.find_all("a", attrs={"class":"news_tit"})

    for title in titles:
        t = title.get_text()
    link = title["href"]
    await ctx.send("===================")
    await ctx.send(f"{t, link}")
    await ctx.send("===================")
    


bot.run(token)
