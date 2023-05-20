import discord
import os, requests, random, json, datetime

from datetime import datetime

from discord import app_commands

from discord.ui import Select,View

from discord.ext import commands


class funSlashCommands(commands.Cog):
  def __init__(self,client):
    self.client = client

  @app_commands.command(name="nsfw", description="💋View nsfw content")
  async def nsfws(self, sctx:discord.Interaction,type:str=None):
    #await sctx.response.send_message(embed=discord.Embed(title="hi"))
    
    if not sctx.channel.is_nsfw():
        if sctx.guild.id!=906381769094356992:
          await sctx.response.send_message("Pls use a nsfw channel")
          return

    choices=["cum","bellevid","4k","gif","spank","anal","hentai","lesbian","bj","feet","holo","lewd","pussy","boobs","belle","gasm"]
    em=discord.Embed(description="💋Nsfw", timestamp=datetime.utcnow())
  
    if type != None:
      if not str(type).lower() in choices:
        em.add_field(name="**Nothing found**\n`Please use these catagories`",value="\n".join(i for i in choices))
        await sctx.response.send_message(embed=em)
        return
      
    if type==None:
      type=choices[random.randint(0,choices.index(choices[-1]))]

    em=discord.Embed(description="💋Nsfw", timestamp=datetime.utcnow())
    for x in choices:
      if type.lower()==x:
        url= f"http://api.nekos.fun:8080/api/"+x

        async def det(ur):
          k=requests.get(ur).text
          return json.loads(k)

        data = await det(url)

        if not "image" in data:
            data = await det(url)
            await sctx.response.send_message(data)
            return
        image=data["image"]
    
        if "bellevid" in x.lower():
          em.add_field(name="Vid: ",value=image)
        else:
          em.set_image(url=image)
        await sctx.response.send_message(embed=em)
        return
      
      else:
        pass
        

  
  

async def setup(client):
  await client.add_cog(funSlashCommands(client))
