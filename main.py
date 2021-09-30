#beta
from discord.ext import commands
import discord

token = "token"
bot = commands.Bot(command_prefix="/")
@bot.event
async def on_ready():
    print("준비완료")
    print(bot.user)
    game = discord.Game("/도움말")
    await bot.change_presence(status=discord.Status.online, activity=game)



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
@bot.command()
async def 청소(ctx):
    if ctx.author.guild_permissions.manage_message:
        try:
            number = int(ctx.message.content[3:])
            await ctx.channel.purge(limit=number)
        except:
            embed = discord.Embed(title="erro!", description="명령어 사용 예시:\n/청소 10", color=0xff0000)
            await ctx.send(embed=embed)
    else:
        await ctx.send("권한이 없습니다.")
@bot.command()
async def 내정보(ctx):
    embed = discord.Embed(title="Your profile!", description=f"name : {ctx.author.name} id : {ctx.author.id}", color=0x00ff00)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

bot.run(token)
