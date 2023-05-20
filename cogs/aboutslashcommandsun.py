import discord
from discord.ext import commands
from discord.ui import Select,View


class aboutslashcommandsun(commands.Cog):
  def __init__(self,client):
    self.client = client

  
  @commands.command(name="avatar", description="🤖Returns the avatar of a user")
  async def avatar(self, ctx):
    await ctx.send("This is a slash commands. Use /avatar instead.")
    return

  @commands.command(name="info", description="🤖Info about a user")
  async def info(self, ctx):
    await ctx.send("This is a slash commands. Use /info instead.")
    return

  @commands.command(name="invite", description="🤖Add Joe to a guild")
  async def invite(self, ctx):
    await ctx.send("This is a slash commands. Use /invite instead.")
    return
  


async def setup(client):
  await client.add_cog(aboutslashcommandsun(client))