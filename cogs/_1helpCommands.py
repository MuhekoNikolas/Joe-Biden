import discord
from discord import app_commands
from discord.ext import commands
from discord.ui import Select,View


class _1helpCommands(commands.Cog):
  def __init__(self,client):
    self.client = client
    


  @app_commands.command(name="help", description="⁉️Displays the help menu")
  async def helps(self,sctx:discord.Interaction,command:str=None):
    choosen = "Help"
    
    if not command == None:
      names = [p for p in self.client.commands]
      
      for h in names:
        if command.lower() in h.name.lower():
          choosen= h.name.capitalize()
          break
      
      
    
    if True:
      commands = [p for p in self.client.commands]

      def sortCommands(k):
        return k.cog_name

      commands = sorted(commands,key=sortCommands)
      #print(commands)
      #descriptions = [p.description[1:] for p in self.client.commands]
      emoji = [p.description[0] for p in commands]
      #for com in self.client.commands:
        #print(com.cog_name)

      options = []
      embeds = []
      view = View()

      for t in range(0,len(commands)):
        string = f'{commands[t].name}1 =discord.SelectOption(label="{commands[t].name.capitalize()}", emoji="{emoji[t]}",description="{commands[t].description[1:].capitalize()}")'

        comm = commands[t]
        if not "slash" in comm.cog_name.lower():
          emString = f"""{comm.name}2 = discord.Embed(title='.{comm.name.capitalize()}', description='{comm.description[0]+' '+comm.description[1:].capitalize()}',color=discord.Color.blue())\nembeds.append({comm.name}2)
  
        """
        else:
          emString = f"""{comm.name}2 = discord.Embed(title='/{comm.name.capitalize()}', description='{comm.description[0]+' '+comm.description[1:].capitalize()}',color=discord.Color.blue())\nembeds.append({comm.name}2)
  
        """
          
        
        adding = f"options.append({commands[t].name}1)"
        exec(string)
        exec(adding)
        exec(emString)

      
          
      sel = Select(options=options[0:25],placeholder="Choose a command")
      sel2 = Select(options=options[25:],placeholder="Choose a command")
      view.add_item(sel)
      view.add_item(sel2)

      async def help_callback(interaction=None):
        if not interaction == None:

            
            embed = ""
            for p in embeds[0:25]:
             # print(p)
              
              if sel.values[0].capitalize() == p.title[1:]:
                embed= p
              
                
            await interaction.response.edit_message(embed=embed)
          
        
           # await ctx.send("z")

      async def help_callback2(interaction=None):
        if not interaction == None:

            
            embed = ""
            for p in embeds:
             # print(p)
              
              if sel2.values[0].capitalize() == p.title[1:]:
                embed= p
              
                
            await interaction.response.edit_message(embed=embed)
          
      sel.callback = help_callback
      sel2.callback = help_callback2
      
      
      for p in embeds:
            if choosen == p.title[1:].capitalize():
                help_emb = p
      await sctx.response.send_message(embed=help_emb, view=view)
      options = []



  
  @commands.command(name="help", description="⁉️Displays the help menu")
  async def help(self,ctx,command=None):
    choosen = "Help"
    
    if not command == None:
      names = [p for p in self.client.commands]
      
      for h in names:
        if command.lower() in h.name.lower():
          choosen= h.name.capitalize()
          break
      
      
    
    if True:
      commands = [p for p in self.client.commands]

      def sortCommands(k):
        return k.cog_name

      commands = sorted(commands,key=sortCommands)
      #print(commands)
      #descriptions = [p.description[1:] for p in self.client.commands]
      emoji = [p.description[0] for p in commands]
      #for com in self.client.commands:
        #print(com.cog_name)

      options = []
      embeds = []
      view = View()

      for t in range(0,len(commands)):
        string = f'{commands[t].name}1 =discord.SelectOption(label="{commands[t].name.capitalize()}", emoji="{emoji[t]}",description="{commands[t].description[1:].capitalize()}")'

        comm = commands[t]
        if not "slash" in comm.cog_name.lower():
          emString = f"""{comm.name}2 = discord.Embed(title='.{comm.name.capitalize()}', description='{comm.description[0]+' '+comm.description[1:].capitalize()}',color=discord.Color.blue())\nembeds.append({comm.name}2)
  
        """
        else:
          emString = f"""{comm.name}2 = discord.Embed(title='/{comm.name.capitalize()}', description='{comm.description[0]+' '+comm.description[1:].capitalize()}',color=discord.Color.blue())\nembeds.append({comm.name}2)
  
        """
          
        
        adding = f"options.append({commands[t].name}1)"
        exec(string)
        exec(adding)
        exec(emString)

      
          
      sel = Select(options=options[0:25],placeholder="Choose a command")
      sel2 = Select(options=options[25:],placeholder="Choose a command")
      view.add_item(sel)
      view.add_item(sel2)

      async def help_callback(interaction=None):
        if not interaction == None:

            
            embed = ""
            for p in embeds[0:25]:
             # print(p)
              
              if sel.values[0].capitalize() == p.title[1:]:
                embed= p
              
                
            await interaction.response.edit_message(embed=embed)
          
        
           # await ctx.send("z")

      async def help_callback2(interaction=None):
        if not interaction == None:

            
            embed = ""
            for p in embeds:
             # print(p)
              
              if sel2.values[0].capitalize() == p.title[1:]:
                embed= p
              
                
            await interaction.response.edit_message(embed=embed)
          
      sel.callback = help_callback
      sel2.callback = help_callback2
      
      
      for p in embeds:
            if choosen == p.title[1:].capitalize():
                help_emb = p
              
      await ctx.send(embed=help_emb, view=view)
      options = []


      
      


async def setup(client):
  await client.add_cog(_1helpCommands(client))