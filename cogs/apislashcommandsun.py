import discord
import requests
import json


from discord import app_commands
from discord.ext import commands
#from discord.ui import Select,View


class apislashcommandsun(commands.Cog):
  def __init__(self,client):
    self.client = client
    

  

  @commands.command(name="testing", description="🤖testing slash command")
  async def testing(self,ctx):
    await ctx.send("This is a slash command. Use /testing instead")
    return

  @commands.command(name="anime",description="🤖Shows an anime meme")
  async def anime(self,ctx):
    
    await ctx.send("This is a slash command. Use /anime instead")
    return

  @commands.command(name="cats",description="🤖Shows a cat meme")
  async def cats(self,ctx):
    
    await ctx.send("This is a slash command. Use /cat instead")
    return

  @commands.command(name="dogs",description="🤖Shows a dog meme")
  async def dogs(self,ctx):
    
    await ctx.send("This is a slash command. Use /dog instead")
    return

  @commands.command(name="decode",description="🤖Decode encoded text")
  async def decodes(self,ctx):
    
    await ctx.send("This is a slash command. Use /decode instead")
    return

  @commands.command(name="encode",description="🤖encode text")
  async def encodes(self,ctx):

    await ctx.send("This is a slash command. Use /encode instead")
    return

  @commands.command(name="djoke",description="🤖Dad joke meme")
  async def djoke(self,ctx):

    await ctx.send("This is a slash command. Use /djoke instead")
    return

  @commands.command(name="hp",description="🤖Info about Harry Potter Cast")
  async def hp(self,ctx):

    await ctx.send("This is a slash command. Use /hp instead")
    return


  @commands.command(name="meme",description="🤖Returns a meme")
  async def meme(self,ctx):

    await ctx.send("This is a slash command. Use /meme instead")
    return

  @commands.command(name="nfact",description="🤖Returns a fact about a number")
  async def nfact(self,ctx):
    await ctx.send("This is a slash command. Use /nfact instead")
    return


  @commands.command(name="qoute",description="🤖Returns a random qoute if today is not specified")
  async def qoute(self,ctx):
    await ctx.send("This is a slash command. Use /q instead")
    return

  @commands.command(name="trivia",description="🤖Play a trivia game")
  async def trivia(self,ctx):
    await ctx.send("This is a slash command. Use /trivia instead")
    return

  @commands.command(name="ym",description="🤖Returns a yo mama joke")
  async def ym(self,ctx):
    await ctx.send("This is a slash command. Use /ym instead")
    return

  @commands.command(name="twitter",description="🤖Get info about a twitter user")
  async def twitter(self,ctx):
    await ctx.send("This is a slash command. Use /twitter instead")
    return

    

async def setup(client):
  await client.add_cog(apislashcommandsun(client))
