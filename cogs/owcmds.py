import os
import disnake as discord
from disnake.ext import commands


class cmds(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.token = os.environ['token']
    self.owner = os.environ['owner']
    self.tuffo = os.environ['tufftobeat']


  @commands.command()
  async def shutdown(self, ctx):
    if ctx.author.id == int(self.owner):
      await ctx.message.delete()
      await self.bot.exit()    
    else:
      await ctx.send('failed')
      await ctx.message.delete()
  

  @commands.command()
  async def restart(self, ctx):
    if ctx.author.id == int(self.owner) or int(self.tuffo):
      await self.bot.exit()
      await self.bot.login(self.token, bot=True)
      await ctx.send("Dark restarted successfully")

    else:
      await ctx.send('failed')


  @commands.command()
  async def erase(self, ctx, amount : int):
    if ctx.author.id == int(self.owner):
      await ctx.channel.purge(limit=amount + 1)


  @commands.command(name="throw", pass_context=True)
  async def throw(self, ctx, member: discord.Member, *,reason="none"):
    if ctx.author.id == int(self.owner):
      await ctx.message.delete()
      await member.kick(reason=reason)


  @commands.command(name="snap", pass_context=True)
  async def snap(self, ctx, member: discord.Member, *, reason="none"):
    if ctx.author.id == int(self.owner):
      await ctx.message.delete()
      await member.ban(reason=reason)


  @commands.command()
  async def dm(self, ctx, member: discord.Member, *, msg):
    if ctx.author.id == int(self.owner):
      await ctx.message.delete()
      await member.send(f"{msg}")






def setup(bot):
	bot.add_cog(cmds(bot))