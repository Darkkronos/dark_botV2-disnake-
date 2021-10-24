import os
import disnake as discord
from disnake.ext import commands


class mod(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.owner = os.environ['owner']
    self.tufftobeat = os.environ['tufftobeat']


  @commands.command(name="kick")
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason="none"):
    self.member = member
    await member.kick(reason=reason)
    ctx.send(f'kicked {member}')


  @commands.command(name="ban")
  @commands.has_permissions(ban_members=True) 
  async def ban(self, ctx, member: discord.Member, *, reason="none"):
    await member.ban(reason=reason)


  @commands.command(name = "cs-ban")
  async def cs_ban(self, ctx, uid, *, reason ="none"):
    if ctx.author.id == int(self.owner) or int(self.tufftobeat):

      with open('blocked_names.txt', 'a') as f:
        try:
          uid1 = int(uid)
        except ValueError:
          await ctx.send('discord ids can only contain integer numbers and no strings or floats.')
        if len(str(uid1)) <= 16:
          await ctx.send("too short to be a an id")
          return
        f.write(f"{uid1} ")

        await self.bot.get_user(588050532434968591).send(f"{ctx.author.name}: {uid} [AT_ID: {ctx.author.id}]")

        await self.bot.get_user(uid).send(f"you were banned  from using dark cross-chat by a member of The Authority. Reason: {reason}")


  #error handling
  #kick error handling
  @kick.error
  async def kick_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send('you dont have permission to use that command')
    elif isinstance(error, commands.CommandInvokeError):
      await ctx.send('user has higher permissions')
    elif isinstance(error, commands.MissingReqquiredArgument):
      await ctx.send('please specify a user')
    else:
      print(error)
      print(type(error))
  

  #ban error handling
  @ban.error
  async def ban_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send('you dont have permission to use that command')
    elif isinstance(error, commands.CommandInvokeError):
      await ctx.send('user has higher permissions')
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('please specify a user')
    else:
      print(error)
      print(type(error))





def setup(bot):
	bot.add_cog(mod(bot))