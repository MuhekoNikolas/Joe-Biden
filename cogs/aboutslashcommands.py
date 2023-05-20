import discord
import os
import requests
import json
import random

from discord import app_commands
from discord.ui import Select,View,Button
from discord.ext import commands

from datetime import datetime


class aboutslashcommands(commands.Cog):
  def __init__(self,client):
    self.client = client


  @commands.command(name="about", description="🤖Tells you stuff about the bot")
  async def about(self, ctx):
    await ctx.send("This is a slash commands. Use /about instead.")
    return
    
    
  @app_commands.command(name="about", description="Tells you stuff about the bot")
  async def abouts(self, sctx:discord.Interaction):
    h= 0
    with open("./res/json/c_counter.json") as r:
        data= json.load(r)
        counter= data["Commands_counter"]
      
    with open("./res/json/last_offline.json") as r:
        data= json.load(r)
        last_offline= data["last_offline"]
  
    for p in self.client.guilds:
      h+= len(p.members)
    niko= await self.client.fetch_user(564452749425639483)
    embed=discord.Embed(title=f"👋Hello {sctx.user}",description="**Here is some info about me**",timestamp=datetime.utcnow())
    embed.set_footer(text=f"Requested by: {sctx.user}", icon_url=f"{self.client.user.avatar}")
    embed.set_thumbnail(url=f"{self.client.user.avatar}")
    embed.add_field(name=f"**My creator is:** {niko.mention}", value=f"**About me:**\n`I currently have` **2000+** `lines of code. Im a multipurpose bot with` **{len(self.client.commands)} commands.** `Am available in `**{len(self.client.guilds)} servers,**` Including: `**[{sctx.guild}].** \n`My total users are: `**{h:,}.**", inline=False)
    embed.add_field(name=f"**Completed command requests:** `{counter:,}`\n**Prefix:**", value=f"`You can start interacting with me by using`** /help** `or` **.help**\n\nLast reboot: {last_offline}",inline=False)
    await sctx.response.send_message(embed=embed)



  @app_commands.command(name="avatar", description="Returns the profile picture of the user")
  async def av(self,sctx:discord.Interaction,user:discord.User=None):
    if user:
      embed=discord.Embed(title=f"{user}'s avatar", description="Hot", colour=discord.Color.random(),timestamp=datetime.utcnow())
      embed.set_image(url=f"{user.avatar}")
      
      if user=="":
        await sctx.response.send_message("Write a target")
      else:
        await sctx.response.send_message(embed=embed)
    else:
      embed=discord.Embed(title=f"{sctx.user}'s avatar", description="Hot", colour=discord.Color.random(), timestamp=datetime.utcnow())
      embed.set_image(url=f"{sctx.user.avatar}")
      await sctx.response.send_message(embed=embed)




  @app_commands.command(name="invite", description="Returns a Invite link used to invite the bot to the server")
  async def invite(self, sctx:discord.Interaction) :
        embed = discord.Embed(
            color= discord.Colour.green(),timestamp=datetime.utcnow())
        embed.set_thumbnail(url=self.client.user.avatar)
        embed.add_field(name='Invite me' ,value=f'[Click me](https://discord.com/oauth2/authorize?client_id={self.client.user.id}&permissions=2134207679&scope=bot%20applications.commands)', inline=False)
        embed.add_field(name="Website",value="[Joe Biden](https://dashboard.joebidenbot.repl.co)")
        await sctx.response.send_message(embed=embed)



  
 #whois
  @app_commands.command(name="info", description="Returns a user's account info")
  async def info(self,sctx:discord.Interaction,member:discord.Member=None):  
    if member==None:
      member=sctx.user
      
    roles=[]
    for role in member.roles:
      if role.name != "@everyone":
        roles.append(role)

    m = member.mobile_status
    p= member.desktop_status
    w= member.web_status
    alp= "abcdefghijklmnopq"
    mw= "".join(random.choices(alp,k= 6))
    pw= "".join(random.choices(alp,k= 6))
    ww= "".join(random.choices(alp,k= 6))
    mw= str(m)+"/"+ mw
    pw= str(p) +"/"+ pw
    ww =str(w) +"/"+ ww
    d= {
      mw: {
        "name": "Mobile",
        "symbol": "📱"
      },
      pw: {
        "name": "Desktop",
        "symbol": " 🖥"
      },
      ww: {
        "name": "Website",
        "symbol": " 🌐"
      }
    }

    r= []
    for x in member.guild_permissions:
      if not x[1]==False or x[1]== None:
        r.append(f"`{(x[0].capitalize()).replace('_',' ')}`")
    r= sorted(r)

  
    statuses= discord.Embed()
    perms=discord.Embed(title="Permissions",description="\n".join(str(r.index(i)+1)+": "+ i for i in r))
    embed=discord.Embed(description=f"Info about: {member.mention}", timestamp=sctx.created_at)
    
    embed.set_thumbnail(url=f"{member.avatar}")
    embed.add_field(name= "**> Name:** ", value=f"`{member.name}`", inline=False)
    embed.add_field(name= "**> ID: **", value=f"`{member.id}`")
    embed.add_field(name="**> Joined Discord:** ", value=f"`{member.created_at.strftime('%a %d, %b 20%y at %H:%M')}`", inline=False)
    embed.add_field(name="**> Joined server:** ", value=f"`{member.joined_at.strftime('%a %d, %b 20%y at %H:%M')}`", inline=False)
    if len(roles)>0:
      embed.add_field(name=f"**> Roles [{len(roles)}]:** ", value=", ".join([role.mention for role in roles]), inline=False)
      embed.add_field(name="**> HighestRole:** ", value=member.top_role.mention, inline=False)
    
    else:
      embed.add_field(name=f"**> Roles[0]]:** ", value="`This user doesnot have any roles`", inline=False)
    embed.add_field(name="**> Bot:** ", value=f"`{member.bot}`\n", inline=False)

  
    for x in d:
      name= d[x]["name"]
      symbol= d[x]["symbol"]

      h= x[-7]
      print(x)
      print(h)
      x,randoms,*other = x.split(h)

     
      if str(x)== "online":
        cmd="🟢"
      elif str(x) == "offline":
        cmd= "⚪️"
      elif str(x)== "dnd":
        cmd= "🔴"
      elif str(x) == "idle":
        cmd= "🌙"
      else:
        cmd= "test"

      statuses.add_field(name=f"> {name}{symbol}:",value=f"{cmd} {str(x)}")

    basicBt = Button(label="Basic Info")
    statusBt = Button(label="Statuses")
    permBt = Button(label="Permissions")
    view = View()

    async def basicBtFunc(inte):
      if  inte.user == sctx.user:
        await inte.response.edit_message(embed=embed)
      else:
        await inte.response.send_message("This is not your interaction", ephemeral=True)

    async def statusBtFunc(inte):
      
      if   inte.user == sctx.user:
        await inte.response.edit_message(embed=statuses)
      else:
        await inte.response.send_message("This is not your interaction", ephemeral=True)

    async def permBtFunc(inte):
      if  inte.user == sctx.user:
        await inte.response.edit_message(embed=perms)
      else:
        await inte.response.send_message("This is not your interaction", ephemeral=True)
    

    basicBt.callback = basicBtFunc
    statusBt.callback = statusBtFunc
    permBt.callback = permBtFunc

    view.add_item(basicBt)
    view.add_item(statusBt)
    view.add_item(permBt)

    await sctx.response.send_message(embed=embed,view=view)





  @app_commands.command(name="server", description="Returns info about a server")
  async def server(self, sctx:discord.Interaction):
    name=sctx.guild
    owner=sctx.guild.owner
    owner_status=sctx.guild.owner.status
    description=sctx.guild.description
    created= sctx.guild.created_at.strftime("%A %d, %B %Y  @ %H:%m")
    unix= sctx.guild.created_at.timestamp()
    bo=0
    real=0
    for members in sctx.guild.members:
      if members.bot:
        bo+=1
      else:
        real+=1
    member=sctx.guild.member_count

    role=len(sctx.guild.roles)
    invite = "unk"
    if len( await sctx.guild.invites()) >0:
        invite = await sctx.guild.invites()
        invite =[ p.code for p in invite]
        invite = invite[0]
        print(invite)

    if invite=="unk":
      try:
        invite= await sctx.channel.create_invite(max_age=0,max_uses=0,unique=False)
      except:
        pass
      

    embed=discord.Embed(timestamp=datetime.utcnow())
    embed.add_field(name="> Owner: ", value=f"{owner.mention}**||**`{owner}`", inline=False)
    embed.add_field(name="> Owner status: ", value=f"`{owner_status}`", inline=False)
    embed.add_field(name="> Server name:", value=f"`{name}`", inline=False)
    embed.add_field(name="> Description: ", value=f"`{description}`", inline=False)
    embed.add_field(name="> Member count: ", value=f"`{member:,}`",inline=False)
    embed.add_field(name="> Real people: ", value=f"`{real:,}`",inline=False)
    embed.add_field(name="> Bots: ", value=f"`{bo:,}`",inline=False)
    embed.add_field(name="> Roles count: ", value=f"`{role:,}`",inline=False)
    embed.add_field(name="> Bots: ", value=f"`{bo:,}`",inline=False)
    embed.add_field(name="> created: ", value=f"`{created}` (<t:{unix:.0F}:R>)",inline=False)
    embed.set_thumbnail(url=sctx.guild.icon)
    try:
      embed.add_field(name="> Invite link: ", value=f"[Invite link](https://discord.gg/{invite})",inline=False)
    except:
      pass
    await sctx.response.send_message(embed=embed)






async def setup(client):
  await client.add_cog(aboutslashcommands(client))