import disnake
from disnake.ext import commands

class cross_chat(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.peng = disnake.AllowedMentions.none()
  


  @commands.Cog.listener()
  async def on_message(self, message: disnake.message):
    ctx = await self.bot.get_context(message)
    am = disnake.AllowedMentions(
      users = False,
      everyone = False,
      roles = False
    )

    TA = 900023065520537630
    AT_1 = 900246069215113237 #not in use
    AT_IDS = 900619170650148864
    TRI = 900242049784250378 #not in use
    ch1 = 835424051202752525
    ch2 = 899595770041356311
    ch3 = 899694823219552317
    ch4 = 899900184220303410
    ch5 = 899986934447874069
    ch6 = 899999169127788554
    ch7 = 900227016886984736
    ch11 = 899623537881538630
    ch22 = 899647480843624510

    if not message.author.bot:
      channel_ids = [ch11, ch22]
      if message.channel.id in channel_ids:
        for c_id in channel_ids:
          files = [await attachment.to_file() for attachment in message.attachments if attachment.content_type.startswith('image') or attachment.content_type.startswith('video')]
          if c_id != message.channel.id:
            await self.bot.get_channel(c_id).send(f"{message.author}: {message.content} ({message.guild.name})", files=files, allowed_mentions = am)




      channels = [ch1, ch2, ch3, ch4, ch5, ch6, ch7]
      ban_list = []

      with open("blocked_names.txt", "r") as f:
        for line in f:
          for word in line.split():
            ban_list.append(int(word))
  
      if message.channel.id in channels:

        channels = [ch1, ch2, ch3, ch4, ch5, ch6, TA, ch7]

        if message.author.id in ban_list:
          return await message.author.send("You're banned from cross-chat")
        
        AT_ID_channel = self.bot.get_channel(AT_IDS)
        await AT_ID_channel.send(f"{message.author}: {message.author.id}: {message.guild.name}: {message.guild.id} channel_ID: {message.channel.id}")
        
        for c_id in channels:
          files = [await attachment.to_file() for attachment in message.attachments if attachment.content_type.startswith('image') or attachment.content_type.startswith('video')]
          channel = self.bot.get_channel(c_id)

          if channel is not None:
            if c_id != message.channel.id:
              if message.author.id not in ban_list:
                await channel.send(f"{message.author}: {message.content} ({message.guild.name})", files=files, allowed_mentions=am)

      authority = [TA]
      if message.channel.id in authority:
        for c_id in channels:
          files = [await attachment.to_file() for attachment in message.attachments if attachment.content_type.startswith('image') or attachment.content_type.startswith('video')]
          channel = self.bot.get_channel(c_id)
          if channel is not None:
            if c_id != message.channel.id:
              await channel.send(f"[{message.guild.name}]: __{message.author.name}__: **{message.content}**", files=files, allowed_mentions = am)

    
      if message.guild is None:
        await self.bot.get_user(588050532434968591).send(f"{message.author.name}: {message.content} [ID: {message.author.id}]")

  




def setup(bot):
	bot.add_cog(cross_chat(bot))