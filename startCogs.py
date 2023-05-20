import discord
from discord.ext import commands
from discord.ui import Select,View
import os


class startCogs(commands.Cog):
  def __init__(self,client):
    self.client = client
    self.tree = self.client.tree
    self.servers = [906381769094356992]
    self.all_cogs = []
    


  @commands.command(name="ls", description="🔧load and sync slash commands")
  async def ls(self,ctx):
    if not str(ctx.author.id) == "564452749425639483":
      return
      
    await self.tree.sync()
    for guild in self.servers:
      await self.tree.sync(guild=discord.Object(id=guild))
    await ctx.send("done")
    



  @commands.command(name="loadall", description="🔧Loads all cogs", aliases = ["la"])
  async def loadall(self, ctx):
    if not str(ctx.author.id) == "564452749425639483":
      return

    
    for command in self.client.commands:
      if not command.cog_name in self.all_cogs:
        self.all_cogs.append(command.cog_name.lower())

        
    for filename in os.listdir("./cogs"):
      file = filename[:-3]
      if filename[-3:]== ".py":
        
        if  file.lower()  in self.all_cogs:
          await ctx.send("That cog is already loaded")
          continue
          
        try:
          await self.client.load_extension(f"cogs.{file}")
          await ctx.send(f"Loaded {file}")
          self.all_cogs.append(file.lower())
        except TimeoutError:
          await ctx.send(f"Already loaded {file}")

        try:
          self.all_cogs.remove("startcogs")
        except:
          pass



  @commands.command(name="unloadall", description="🔧unloads all cogs", aliases = ["ula"])
  async def unloadall(self, ctx):
    
    if not str(ctx.author.id) == "564452749425639483":
      return


    try:
      self.all_cogs.remove("startcogs")
    except:
      pass
      
    await ctx.send(self.all_cogs)
    for filename in self.all_cogs:
        
        file = filename
        if file.lower() == "startcogs":
          continue

        try:
          await self.client.unload_extension(f"cogs.{file}")
          await ctx.send(f"unLoaded {file}")
          self.all_cogs.remove(file.lower())
        except:
          await ctx.send(f"Already unloaded {file}")
        


    


  
  @commands.command(name="load", description="🔧Loads a cog", aliases = ["lc"])
  async def load(self, ctx,extension=None):
    
    if not str(ctx.author.id) == "564452749425639483":
      return

    if extension==None:
      await ctx.send("No extension sent")
      return

    try:
      self.all_cogs.remove("startcogs")
    except:
      pass
      
    

    for command in self.client.commands:
      if not command.cog_name in self.all_cogs:
        self.all_cogs.append(command.cog_name.lower())

    
    
    file = os.listdir("cogs")
    #p = [x[:-3] for x in file]
    if  extension.lower() in self.all_cogs:
      await ctx.send("That cogs is already loaded")
      return


    try:
      self.all_cogs.remove("startcogs")
    except:
      pass
      
    try:
          await self.client.load_extension(f"cogs.{extension}")
          await ctx.send(f"Loaded {file}")
          self.all_cogs.append(extension.lower())
    except:
          await ctx.send(f"Already loaded {extension}")


  @commands.command(name="unload", description="🔧unloads a cog", aliases = ["ulc"])
  async def unload(self, ctx,extension=None):
    if not str(ctx.author.id) == "564452749425639483":
      return

    
    if extension==None:
      await ctx.send("No extension")
      return

    try:
      self.all_cogs.remove("startcogs")
    except:
      pass
      

    if extension.lower() == "startcogs":
      await ctx.send("Cant unload that")
      return

    

    for command in self.client.commands:
      if not command.cog_name in self.all_cogs:
        self.all_cogs.append(command.cog_name.lower())
    
    
    #p = [x[:-3] for x in file]
    if not extension.lower() in self.all_cogs:
      await ctx.send("That cogs are not loaded")
      return

    
    try:
          await self.client.unload_extension(f"cogs.{extension}")
          await ctx.send(f"unLoaded {extension}")
          self.all_cogs.append(extension.lower())
    except:
          await ctx.send(f"Already unloaded {extension}")
    
  


    

async def setup(client):
  await client.add_cog(startCogs(client))