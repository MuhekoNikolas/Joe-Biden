import discord
from discord.ui import Select,View
from discord.ext import commands
import math, datetime, random, requests, json

from datetime import datetime


class fun(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(name="ping", description="🏓says pong")
  async def ping(self,ctx):
    
    only = discord.SelectOption(label="Placeholder",description="Placeholder")
    latency = str(round(self.client.latency*1000))
  
    view = View()
    sel = Select(options=[only],disabled=True,placeholder=f"The bot is on {latency} ping")

    view.add_item(sel)
    await ctx.send(view=view)

    
  @commands.command(name="nsfw", description="💋View nsfw content")
  async def nsfw(self,ctx,type=None):
    if not ctx.channel.is_nsfw():
        if ctx.guild.id!=906381769094356992:
          await ctx.send("Pls use a nsfw channel")
          return

    choices=["cum","bellevid","4k","gif","spank","anal","hentai","lesbian","bj","feet","holo","lewd","pussy","boobs","belle","gasm"]
    em=discord.Embed(description="💋Nsfw", timestamp=datetime.utcnow())
  
    if type != None:
      if not str(type).lower() in choices:
        em.add_field(name="**Nothing found**\n`Please use these catagories`",value="\n".join(i for i in choices))
        await ctx.send(embed=em)
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
            await ctx.send(data)
            return
          
        image=data["image"]
        
      
        if "bellevid" in x.lower():
        
          em.add_field(name="Vid: ",value=image)
        else:
          em.set_image(url=image)
        
        await ctx.send(embed=em)
        return
      
      else:
        pass
      


  




async def setup(client):
  await client.add_cog(fun(client))