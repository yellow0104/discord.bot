#beta
from discord.ext import commands
import discord



token = ""
intents = discord.Intents.all() 


bot = commands.Bot(command_prefix="?", intents=intents)
@bot.event
async def on_ready():
    print("준비완료")
    print(bot.user)
    game = discord.Game("?도움말")
    await bot.change_presence(status=discord.Status.online, activity=game)



#공지를 보내는 명령어
@bot.command()
async def 공지(ctx):
    if ctx.author.guild_permissions.manage_messages:

        content = ctx.message.content[3:]
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(title="공지📢", description=content, color=0x00ff00)
        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
    else:
        await ctx.send("권한이 없습니다.")
#채팅 청소 명령어
@bot.command()
async def 청소(ctx):
    if ctx.author.guild_permissions.manage_messages: #관리자 권한이 있는가?
        try:
            number = int(ctx.message.content[3:])
            await ctx.channel.purge(limit=number)
        except:
            embed = discord.Embed(title="erro!", description="명령어 사용 예시:\n?청소 10", color=0xff0000)
            await ctx.send(embed=embed)
    else: #아니라면
        await ctx.send(f"<@!{ctx.author.id}>님은 권한이 없습니다.")

    
#다른사람의 정보를 보는 명령어
@bot.command()
async def 유저정보(ctx, user: discord.Member = None):
    user_a = str(user.activity)
    
    if user_a == "None":
        user_activity = "None"
    else:
        user_activity = user.activity.name
    try:
        embed = discord.Embed(title=f"{user.name} Profile!", color=0x00ff00)
        embed.add_field(name="name", value=user.name, inline=True)
        embed.add_field(name="id", value=user.id, inline=True)
        embed.add_field(name="status", value=user.status, inline=True)
        embed.add_field(name="activity", value=user_activity, inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    except:
            embed = discord.Embed(title="erro!", description="명령어 사용 예시:\n?유저정보 @정우", color=0xff0000)
            await ctx.send(embed=embed)
@bot.command()
async def 도움말():
    embed = discord.Embed(title="도움말", color=0x00ffff)
    embed.add_field(name="접두사", value="?")
    embed.add_field(name="공지", value="공지를 띄어줍니다.")
    embed.add_field(name="청소", value="청소 (수) 채팅청소를 해줍니다")
    embed.add_field(name="유저정보", value="유저정보를 띄어줍니다.")
    embed.set_footer(text="이 봇은 discord 모듈 공부용입니다.")

bot.run(token)
