import random
import disnake as discord
import asyncio
from io import BytesIO
from disnake.ext import commands


class miscellanious(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  

  #8ball command
  @commands.command(aliases=["8ball"])
  async def question(self, ctx, *, question):
	  randomresp = random.randint(0, 6)
	  resp = ['nah', 'hell no', 'yeah', 'probably', 'maybe', 'yes', 'probably no']
	  await ctx.send(f'Question: {question}\nAnswer: {resp[randomresp]}')



  #ping command
  @commands.command()
  async def ping(self, ctx):
	  pingtxt = ['to ping you', 'to contact you', 'to kidnap your grandma', 'to send you to the shadow realm']
	  pingresp = random.randint(0, 3)
	  await ctx.send(f" it takes me {round(self.bot. latency*1000)}ms {pingtxt[pingresp]}")
  

  @commands.command()
  async def AV(self, ctx):
    file = discord.File(BytesIO(await ctx.author.avatar_url.read(), filename = 'avatar.jpg'))
    await ctx.send(file = file)
  

  #purge command
  @commands.command(aliases=['purge', 'clean', 'delete'])
  @commands.has_permissions(manage_messages=True)
  async def clr(self, ctx, amount : int):
    amount = amount + 1
    await ctx.channel.purge(limit=amount)


  @commands.command()
  @commands.has_permissions(administrator = True)
  async def send(self, ctx, member: discord.Member, *, msg):
    await member.send(f"{msg} sent by {ctx.author} from {ctx.guild.name}")


  #error handling
  #purge error handling
  @clr.error
  async def purge_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send('Please check if you have proper permissions')
      elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please state the number of messasges to be deleted')
      elif isinstance(error, commands.MissingPermissions & commands.MissingRequiredArgument):
        await ctx.send('missing permissions and arguments')
  

  #question error hamdling
  @question.error
  async def question_error(self, ctx, error):
      if isinstance(error, commands.MissingRequiredArgument):
          await ctx.send("No question was inputted")


  #question error hamdling
  @send.error
  async def send_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
          await ctx.send("You need administrator privelages to use this")





def setup(bot):
	bot.add_cog(miscellanious(bot))