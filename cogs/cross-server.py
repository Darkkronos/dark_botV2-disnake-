import os
import json
import disnake 
from disnake.ext import commands

class cross_chat(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.owner = os.environ['owner']
    self.tuffo = os.environ['tufftobeat']


  @commands.Cog.listener()
  async def on_message(self, message: disnake.message):
    ctx = await self.bot.get_context(message)
    TA = 900023065520537630
    AT_1 = 900246069215113237 #not in use
    AT_IDS = 900619170650148864

    if not message.author.bot:
      channels = []
      with open("cs-channels.json") as f:
        data = json.load(f)
        channels = data.get('cross-chats', [])
      
      ban_list = []

      with open("blocked_names.txt", "r") as f:
        for line in f:
          for word in line.split():
            ban_list.append(int(word))
  
      if message.channel.id in channels:

        with open("cs-channels.json") as f:
          data = json.load(f)
          channels = data.get('cross-chats-TA', [])

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
                await channel.send(f"{message.author}: {message.content} ({message.guild.name})", files=files)

      authority = [TA]
      if message.channel.id in authority:
        for c_id in channels:
          files = [await attachment.to_file() for attachment in message.attachments if attachment.content_type.startswith('image') or attachment.content_type.startswith('video')]
          channel = self.bot.get_channel(c_id)
          if channel is not None:
            if c_id != message.channel.id:
              await channel.send(f"[{message.guild.name}]: __{message.author.name}__: **{message.content}**")

    
      if message.guild is None:
        await self.bot.get_user(588050532434968591).send(f"{message.author.name}: {message.content} [ID: {message.author.id}]")



  @commands.command()
  async def add_cs(self, ctx, chanel):
    if ctx.author.id == int(self.owner) or int(self.tuffo):
      with open("cs-channels.json") as f:
        data = json.load(f)

        current_chats = data.get('cross-chats', [])
        current_chats.append(int(chanel))
        data.update({"cross-chats": current_chats})

        current_chats = data.get('cross-chats-TA', [])
        current_chats.append(int(chanel))
        data.update({"cross-chats-TA": current_chats})

      with open("cs-channels.json", "w") as f:
        json.dump(data, f)
        await ctx.send(f"Added {chanel}")
        await self.bot.get_user(588050532434968591).send(f"{ctx.author.name}: chanel:{chanel} [ID: {ctx.author.id}]")





def setup(bot):
	bot.add_cog(cross_chat(bot))