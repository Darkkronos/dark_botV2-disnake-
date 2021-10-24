import disnake as discord
from disnake.ext import commands
from youtubesearchpython import VideosSearch


class search(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def search(self, ctx, *, search):
    videosSearch = VideosSearch(search, limit = 1)
    link1 = videosSearch.result()['result'][0]['link']
    await ctx.send(link1)





def setup(bot):
	bot.add_cog(search(bot))