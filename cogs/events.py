import discord

from discord.ext import commands
from discord.ui import Select,View

class events(commands.Cog):
  def __init__(self,client):
    self.client= client

  

    
  


  
  @commands.Cog.listener()
  async def on_message_delete(self, message):
    chann = message.channel
    author = message.author
    log = ""
    
    for channel in message.guild.channels:
      if "log" in channel.name.lower():
        log = channel
        break
        
    if log == "":
      try:
        log = await message.guild.create_channel(name="Log Channel")
      except:
        print("cant create")
        return

    try:
      await log.send(f"{message.content}\n{author.mention}\n{chann.name}")
    except:
      print("No access")
        




async def setup(client):
  await client.add_cog(events(client))