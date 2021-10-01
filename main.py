#beta
from discord.ext import commands
import discord


token = "token"
bot = commands.Bot(command_prefix="!")
@bot.event
async def on_ready():
    print("준비완료")
    print(bot.user)
    game = discord.Game("/도움말")
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
    if ctx.author.guild_permissions.manage_message: #관리자 권한이 있는가?
        try:
            number = int(ctx.message.content[3:])
            await ctx.channel.purge(limit=number)
        except:
            embed = discord.Embed(title="erro!", description="명령어 사용 예시:\n/청소 10", color=0xff0000)
            await ctx.send(embed=embed)
    else: #아니라면
        await ctx.send("권한이 없습니다.")
#내 디스코드 정보를 보는 명령어
@bot.command()
async def 정보(ctx):

    embed = discord.Embed(title="Your Profile!", description=f"name : {ctx.author.name} id : {ctx.author.id}", color=0x00ff00)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    print(ctx.guild.id)
#다른사람의 정보를 보는 명령어
@bot.command()
async def 유저정보(ctx, user: discord.Member = None):
    try:
        embed = discord.Embed(title=f"{user.name} Profile!", description=f"name : {user.name} id : {user.id}", color=0x00ff00)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    except:
            embed = discord.Embed(title="erro!", description="명령어 사용 예시:\n/유저정보 @정우", color=0xff0000)
            await ctx.send(embed=embed)
bot.run(token)
