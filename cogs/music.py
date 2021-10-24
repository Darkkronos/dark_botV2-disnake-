import disnake as discord
import DiscordUtils
from disnake.ext import commands


class main(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.music = DiscordUtils.Music()


  @commands.command()
  async def join(self, ctx):
    await ctx.author.voice.channel.connect()
    await ctx.send(f'joined {ctx.author.voice.channel.name}')
  

  @commands.command()
  async def play(self, ctx, *, url):
    music = self.music
    player = music.get_player(guild_id=ctx.guild.id)

    if not ctx.guild.me.voice:
      await ctx.invoke(self.bot.get_command('join'))

    if not player:
      player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    
    if not ctx.voice_client.is_playing():
      await player.queue(url, search=True)
      song = await player.play()
      await ctx.send(f"Playing {song.name}")
    
    else:
      song = await player.queue(url, search=True)
      await ctx.send(f"Queued {song.name}")


  @commands.command()
  async def queue(self, ctx):
    music = self.music
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")


  @commands.command()
  async def stop(self, ctx):
    player = self.music.get_player(guild_id=ctx.guild.id)
    await player.stop()
    await ctx.send("Stopped")


  @commands.command()
  async def leave(self, ctx):

    if ctx.voice_client.is_playing():
      player = self.music.get_player(guild_id=ctx.guild.id)
      await player.stop()
      await ctx.voice_client.disconnect()
    
    else:
      await ctx.voice_client.disconnect()
      await ctx.send(f'left {ctx.author.voice.channel.name}')


  @commands.command()
  async def np(self, ctx):
    player = self.music.get_player(guild_id=ctx.guild.id)
    song = player.now_playing()
    await ctx.send(song.name)


  @commands.command()
  async def skip(self, ctx):
    player = self.music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)

    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    
    else:
        await ctx.send(f"Skipped {data[0].name}")


  @commands.command()
  async def volume(self, ctx, vol):
    player = self.music.get_player(guild_id=ctx.guild.id)
    song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
    await ctx.send(f"Changed volume for {song.name} to {volume*100}%")


  @commands.command()
  async def remove(self, ctx, index):
    player = self.music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")





  #error handling
  #join error
  @join.error
  async def jerror(self, ctx, error):
    if isinstance(error, discord.ClientException):
      await ctx.send('Error:clientException')
    elif isinstance(error, commands.MissingPermissions):
      await ctx.send('I dont have permission to join that channel')
    elif isinstance(error, commands.CommandInvokeError):
      await ctx.send('you need to be joined in a vc to use that')
    else:
      await ctx.send('Already connected to voice')





def setup(bot):
	bot.add_cog(main(bot))