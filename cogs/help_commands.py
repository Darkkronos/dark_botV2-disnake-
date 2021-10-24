import disnake as discord
from disnake.ext import commands


class help(commands.Cog):
  def __init_(self, bot):
    self.bot = bot


  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
    em = discord.Embed(title = '__Need help?__', description = "Use 'dark help <command>' for more info", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "Moderation", value = 'kick\nban\npurge\n', inline = True)
    em.add_field(name = "Misc", value = "8ball\nping\nsearch\nsend", inline= True)
    em.add_field(name = "Voice", value = "join\nplay\nleave\nnp\nstop\npause\nresume")
    await ctx.send(embed = em)


  @help.command()
  async def kick(self, ctx):
    em = discord.Embed(title = '__kick__', description = "kicks a member", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark kick <member> [optional][reason]')
    await ctx.send(embed = em)

  #ban help
  @help.command()
  async def ban(self, ctx):
    em = discord.Embed(title = '__ban__', description = "bans a member", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark ban <member> [optional][reason]')
    await ctx.send(embed = em)


  #purge help
  @help.command(aliases = ['clr', 'clean', 'delete'])
  async def purge(self, ctx):
    em = discord.Embed(title = '__Purge__', description = "deletes messages", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark purge [number of messages to delete]')
    em.add_field(name = '**Aliases**', value = 'clr\nclean\ndelete', inline = False)
    await ctx.send(embed = em)


  #8ball help 
  @help.command(aliases = ['8ball'])
  async def question(self, ctx):
    em = discord.Embed(title = '__8ball__', description = "answers your questions", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark 8ball [question]')
    em.add_field(name = '**Aliases**', value = 'question', inline = False)
    await ctx.send(embed = em)


  #ping help
  @help.command()
  async def ping(self, ctx):
    em = discord.Embed(title = '__Ping__', description = "pings server to measure latency", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark ping')
    await ctx.send(embed = em)


  @help.command(aliases = ['yt'])
  async def search(self, ctx):
    em = discord.Embed(title = '__Search__', description = "Searches youtube", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark search [query]')
    em.add_field(name = '**Aliases**', value = 'yt', inline = False)
    await ctx.send(embed = em)


  @help.command()
  async def join(self, ctx):
    em = discord.Embed(title = '__Join__', description ="Joins message author's vc", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark join')
    await ctx.send(embed = em)


  @help.command()
  async def play(self, ctx):
    em = discord.Embed(title = '__play__', description ="Plays an audio from youtube", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark play [URL/Name]')
    await ctx.send(embed = em)


  @help.command()
  async def np(self, ctx):
    em = discord.Embed(title = '__np__', description ="Shows now playing", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark np')
    await ctx.send(embed = em)


  @help.command()
  async def queue(self, ctx):
    em = discord.Embed(title = '__queue__', description ="Shows current queue", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark queue')
    await ctx.send(embed = em)


  @help.command()
  async def pause(self, ctx):
    em = discord.Embed(title = '__pause__', description ="Pauses audio", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark pause')
    await ctx.send(embed = em)


  @help.command()
  async def resume(self, ctx):
    em = discord.Embed(title = '__resume__', description ="Resumes audio", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark resume')
    await ctx.send(embed = em)


  @help.command()
  async def remove(self, ctx):
    em = discord.Embed(title = '__remove__', description ="Removes audio from the queue", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark remove [song name]')
    await ctx.send(embed = em)


  @help.command()
  async def stop(self, ctx):
    em = discord.Embed(title = '__stop__', description ="Stopd audio", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark stop')
    await ctx.send(embed = em)


  @help.command()
  async def leave(self, ctx):
    em = discord.Embed(title = '__leave__', description ="Leaves vc", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark leave')
    await ctx.send(embed = em)


  @help.command()
  async def send(self, ctx):
    em = discord.Embed(title = '__send__', description ="Sends a message to a user.", color = ctx.author.color)
    em.set_footer(text = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar.url)
    em.add_field(name = "**Syntax**", value = 'dark send {member} [message]')
    em.add_field(name = '**permission**', value = 'Administrator')
    await ctx.send(embed = em)





def setup(bot):
	bot.add_cog(help(bot))