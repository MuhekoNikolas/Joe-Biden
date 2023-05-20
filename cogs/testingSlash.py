import discord
import os
from datetime import datetime

from discord import app_commands

from discord.ui import Select,View

from discord.ext import commands


class testingSlash(commands.Cog):
  def __init__(self,client):
    self.client = client

  
  

async def setup(client):
  await client.add_cog(testingSlash(client))
