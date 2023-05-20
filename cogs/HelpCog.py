import discord
import os
import random

from datetime import datetime

from discord import app_commands

from discord.ui import Select,View,Button

from discord.ext import commands


class helpCog(commands.Cog):
  def __init__(self,client):
    self.client = client
    self.colours=(0x0000FF,0xFF4040,0x7FFF00,0xFFB90F,0xFF1493,0x9400D3)
    #emojis
    self.ewarn= client.get_emoji(921692510986833931)
    self.private_perms=client.get_emoji(921711898687328276)
    self.elocktext=client.get_emoji(921712120637304842)
    self.einfo=client.get_emoji(921712290921865246)
    self.emute=client.get_emoji(921790232997797938)
    self.vmutee=client.get_emoji(921708198841425963)
    self.infoe="<:info:921712290921865246>"
    self.locktext="<:locked_textchannel:921712120637304842>"
    self.unpermit="<:private_permissions:921711898687328276>"
    self.warne="<:win11_warning_icon:921692510986833931>"
    self.bote="<:Robot_smile_face:920379058347450429>"
    self.helpe="<:help_button:920379658246168586>"
    self.admine=("<:Admin_Badge:920377935800709220>")
    self.mutee=("<:mute:921790232997797938>")
    self.evmute=("<:voice_muted:921708198841425963>")
    self.locked_vc=("<:locked_vc:921796253304651867>")



  


  @app_commands.command()
  async def helps(self,sctx:discord.Interaction):


    help_em=discord.Embed(title="<:help_button:920379658246168586>Help", description= "These are the available commands", timestamp=datetime.utcnow(),colour=discord.Color.random())
    help_em.set_thumbnail(url=f"{self.client.user.avatar}")
    help_em.set_author(name=f"{self.client.user.name}  - Boa")
    help_em.add_field(name="> **💻api ||`meme commands and related`**", value="> **<:Robot_smile_face:920379058347450429>bot `commands to check on the bot`**",inline=False)
    help_em.add_field(name="> **👷‍♂️creator `Commands only whitelisted people can perform`** ", value="> **🥴fun `just for fun and a little trolling`**", inline=False)
    help_em.add_field(name=">  **<:Admin_Badge:920377935800709220> mod**", value="`Commands that perform moderation actions`", inline=False)    

  


    

    bot_em=discord.Embed(title="Bot related commands",description="commands to check on the bot", timestamp=datetime.utcnow(),colour=discord.Color.random())
    bot_em.set_thumbnail(url=f"{self.client.user.avatar}")  
    bot_em.add_field(name=f"> 💁**about** `This lets the bot tell you abit about himself`", value=f"`[-about]`", inline=False)
    bot_em.add_field(name=f"> 🧑**av** `Avatar of the person you mention \n[-av {sctx.user}]`", value=f"> 🆘**help** `This displays all the available commands \n[-help]`", inline=False)
    bot_em.add_field(name="> ℹ️**info** `info about the mentioned user \n[-info {ctx.author}]`", value=f"> 🔗**invite** `The bot will share the invite link used to add it to the server \n[-invite]`", inline=False)
    bot_em.add_field(name="> 🏓**ping** `The bot will reply with the Bot's Latency/ping \n[-ping]`", value="> 🖥**server** `Server stats of the current server\n[-server]`", inline=False)
    bot_em.add_field(name=f"> 🎗**remind** `The bot will remind you something [-remind 1h 2m 3s Go eat lunch]`",value="> 📆**date** `The bot will tell you what the date is [-date]`")




    mod_em=discord.Embed(title=f"{self.admine} Moderation commands", description="Commands that perform mod actions", timestamp=datetime.utcnow(),colour=discord.Color.random())
    mod_em.set_thumbnail(url=f"{self.client.user.avatar}")
    mod_em.add_field(name=f"> 🔨**ban** `ban user [-ban {sctx.user}]`", value=f"> {self.locktext}**ctc**  `Create a text channel [-ctc hangout]`", inline=False)
    mod_em.add_field(name=f"> {self.locktext}**cpt** `Create a private text channel [-cpt private_hangout`", value=f"> 🎤**cvc**\n`Create a voice channel [-cvc voicechannel1]`", inline=False)
    mod_em.add_field(name=f"> 🎤**cpv**\n `Create a private voice channel [-cpv private_voicechannel1]`", value=f"> <:win11_warning_icon:921692510986833931>**warns**  `See someone's warn count [-warns {sctx.user}]`", inline=False)
    mod_em.add_field(name=f"> 🔑**createrole**  `Creates a role [-createrole VIP]`", value=f"> 🔑**delrole** `Deletes a role [-delrole UnwantedRole]`", inline=False)

    mod_em.add_field(name=f"> {self.locktext}**delc** `delete a channel [-delc #{sctx.user}]`", value=f"> <:win11_warning_icon:921692510986833931>**delw**  `Delete a member's warns [-delw {sctx.user}]`", inline=False)
    mod_em.add_field(name=f"> 🔑**giverole**  `Gives a user a role [-giverole {sctx.user} Admin]`", value=f"> 🔨**kick**  `kick user [-kick {sctx.user}]`", inline=False)
    mod_em.add_field(name=f"> {self.locktext}**lock** `Locks a channel [-lockdown #{sctx.channel}]`", value=f"> {self.mutee}**mute**  `mute someone [-mute {sctx.user}]`", inline=False)
    
    mod_em.add_field(name=f"> 💬**purge** `purge messages [-purge {random.randint(10,100)}]`", value=f"> 🔑**takerole** `Takes a role from a user [-takerole {sctx.user} Admin]`", inline=False)
    mod_em.add_field(name=f"> 🔨**unban** `unban someone [-unban user#1997]`", value=f"> {self.mutee}**unmute** `unmute someone [-unmute {sctx.user}]`", inline=False)

    mod_em.add_field(name=f"> {self.locktext}**unlock** `Unlocks a channel [-unlockdown #{sctx.channel}]`", value=f"> {self.evmute}**unvlock**\n`Unlocks a voice channel [-unvlock voicechannel1]`", inline=False)

    mod_em.add_field(name=f"> {self.locked_vc}**vlock** `Locks a voice channel [-vlock voicechannel1 ]`", value=f"> <:win11_warning_icon:921692510986833931>**warn** `warn someone [-warn {sctx.user} reason]`", inline=False)
    mod_em.add_field(name="> **rr:** Creates a reaction role",value="Usage: -rr [role] <channel>\n`Create a reaction role`")




    options = ["bot_em","help_em"]
    view = View()

    
    botButton = Button(label="Bot")
    helpEmButton = Button(label="Main")
    modButton = Button(label="Mod")

    async def botButtonCallback(inte):
     await inte.response.edit_message(embed=bot_em)

    async def helpButtonCallback(inte):
     await inte.response.edit_message(embed=help_em)

    async def modButtonCallback(inte):
     await inte.response.edit_message(embed=mod_em)
      

    helpEmButton.callback = helpButtonCallback
    botButton.callback = botButtonCallback
    modButton.callback = modButtonCallback

    view.add_item(botButton)
    view.add_item(helpEmButton)
    view.add_item(modButton)

    """
    for opt in options:
      createButton = f"{opt}_= Button(label='{opt}')"
      buttonCallback = f"async def {opt}callback(inte):\n  global {opt}\n  await inte.response.edit_message(embed={opt})"
      assign= f"{opt}_.callback = {opt}callback"
      addView = f"view.add_item({opt}_)"
      
      exec(createButton)
      exec(buttonCallback)
      exec(assign)
      exec(addView)

    """
    
    await sctx.response.send_message(embed=help_em, view=view)
  
    

async def setup(client):
  await client.add_cog(helpCog(client))