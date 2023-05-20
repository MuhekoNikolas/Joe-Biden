
import os
os.system("clear")


import json, random, requests, datetime, hosting, os


try:
  import discord
  from discord.ui import Select,View
  
except:
  os.system("pip install discord.py==2.0.1")
  from discord.ui import Select,View

from hosting import keep_alive

from discord.ext import commands

from datetime import datetime


intents = discord.Intents.all()
intents.members = True  
intents.presences = True

client = commands.Bot(command_prefix=".", help_command=None, intents=intents, case_insensitive=True)

all_cogs = []

last_offline= f"<t:{(datetime.utcnow().timestamp()):.0f}:R>"

with open("./res/json/last_offline.json","r") as r:
  data = json.load(r)
  
  data["last_offline"] = last_offline
  with open("./res/json/last_offline.json","w") as w:
    json.dump(data,w,indent=4)

@client.event
async def on_ready():
    channel = await client.fetch_channel(936638017320419378)
    await channel.send("Online")
  
    await client.load_extension("startCogs")

    for filename in os.listdir("./cogs"):
      file = filename[:-3]
      if filename[-3:]== ".py":
        
        if  file.lower()  in all_cogs:
          await channel.send(f"That cog {file} is already loaded")
          continue
          
        try:
          await client.load_extension(f"cogs.{file}")
          await channel.send(f"Loaded {file}")
          all_cogs.append(file.lower())
          
        except TimeoutError:
          await channel.send(f"Already loaded {file}")

        try:
          all_cogs.remove("startcogs")
        except:
          pass
  



announcement="""
**Important Announcement** ```Joe Biden will be closing its services and never be updated again on the 30th/August/2022. 
This is due to discord introducing a new intent and denying Joe Biden access to it. This has thus broke Joe Biden. It’s been a good year with you. Have a fun school term. In the meantime. Enjoy Joe Biden’s “slash commands”
```
"""
  

  
keep_alive()
Token = os.environ["TOKENV2"]
client.run(Token)
