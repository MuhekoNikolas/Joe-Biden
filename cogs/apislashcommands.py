import discord
from discord import app_commands
import requests
import json
import random
import asyncio
import os
from datetime import datetime
import tweepy

from discord.ext import commands
from discord.ui import Select,View,Button


class apislashcommands(commands.Cog):
  def __init__(self,client):
    self.client = client
    self.tree = self.client.tree
    self.servers = [906381769094356992]
    self.colours= (0x0000FF,0xFF4040,0x7FFF00,0xFFB90F,0xFF1493,0x9400D3)



  @commands.command(name="anon",description="👺Shows an anon meme")
  async def anon(self,ctx):
    await ctx.send("This is a slash command. Use /anon instead")
    return
  

  
  
  @app_commands.command(name="hehe",description="HeHe")
  async def sayHeHe(self,ctx): #discord.Interaction):
    await ctx.response.send_message("HeHe")

  
  @app_commands.command(name="anon",description="Shows an anon meme")
  async def anons(self,sctx:discord.Interaction):
    data = requests.get("https://meme-api.herokuapp.com/gimme/greentext").text
    data = json.loads(data)
    em = discord.Embed(title=data["title"]).set_image(url=data["preview"][-1]).set_footer(text=f'{data["ups"]} 👍')
    await sctx.response.send_message(embed=em)

  
  @app_commands.command(name="anime",description="Shows an anime meme")
  async def animes(self,sctx:discord.Interaction):
    data = requests.get("https://meme-api.herokuapp.com/gimme/"+"animeirl").text
    data = json.loads(data)
    embed=discord.Embed(title=f"{data['title']}", description=f"{data['author']}",timestamp=datetime.utcnow())
    embed.set_image(url=f"{data['url']}")
    await sctx.response.send_message(embed=embed)



  
  @app_commands.command(name="cats",description="Shows a cat meme")
  async def catss(self,sctx:discord.Interaction):

    content=requests.get("https://meme-api.herokuapp.com/gimme/cats").text
    data=json.loads(content)
    embed=discord.Embed(title=f"{data['title']}", description=f"by: {data['author']}",timestamp=datetime.utcnow())
    embed.set_image(url=f"{data['url']}")
    
    bt = Button(label="Next")
    
    
    async def newMeme(interaction:discord.Interaction):
       
        content=requests.get("https://meme-api.herokuapp.com/gimme/cats").text
        data=json.loads(content)
        embed=discord.Embed(title=f"{data['title']}", description=f"by: {data['author']}",timestamp=datetime.utcnow())
        embed.set_image(url=f"{data['url']}")
      
        await interaction.response.edit_message(embed=embed)

    bt.callback = newMeme
    buttons= [bt]
    view = View()
    view.add_item(bt)
    await sctx.response.send_message(embed=embed,view=view)




  #dog
  
  @app_commands.command(name="dogs",description="Shows a dog meme")
  async def dogs(self, sctx:discord.Interaction,breed:str=None):
      
      
      content=requests.get("https://dog.ceo/api/breeds/list").text
      lol=json.loads(content)
      if breed==None:
        breed = random.choice(lol["message"])
  
      if breed != None:
        content= requests.get(f"https://dog.ceo/api/breed/{breed.lower()}/images")
        p=content.text
        if content.ok==False:
          await sctx.response.send_message(f"**That breed is not supported. Here are the supported breeds.**\n`{' `|` '.join(i for i in lol['message'])}` ")
          return
        data=json.loads(p)
        embed=discord.Embed(title=f"A {breed}",timestamp=datetime.utcnow())
        embed.set_image(url=f"{data['message'][random.randint(0,len(data['message'])-1)]}")
    
      
        bt = Button(label="Next")
        view= View()
        view.add_item(bt)
    
        async def dogButtonFunc(int:discord.Interaction):
              if breed:
                content= requests.get(f"https://dog.ceo/api/breed/{breed.lower()}/images")
                p=content.text
                if content.ok==False:
                  await sctx.response.send_message(f"**That breed is not supported. Here are the supported breeds.**\n`{' `|` '.join(i for i in lol['message'])}` ")
                  return
                data=json.loads(p)
                embed=discord.Embed(title=f"A {breed}",timestamp=datetime.utcnow())
                embed.set_image(url=f"{data['message'][random.randint(0,len(data['message'])-1)]}")
                await int.response.edit_message(embed=embed)
            
              else:
                content= requests.get("https://dog.ceo/api/breeds/image/random").text
                data=json.loads(content)
                embed=discord.Embed(title=f"A cute dog",timestamp=datetime.utcnow()).set_image(url=f"{data['message']}")
                await int.response.edit_message(embed=embed)
              
    
    
          
        bt.callback= dogButtonFunc
        
        msg= await sctx.response.send_message(embed=embed,view=view)

      
    

  @app_commands.command(name="decode",description="Decodes encoded text")
  async def decodes(self,sctx:discord.Interaction,encoded_text:str):
        content=requests.get(f"https://normal-api.tk/decode?text={encoded_text}").text
        data=json.loads(content)
        embed=discord.Embed(title=f"Decoded {encoded_text}", description=f"{data['decoded']}",timestamp=datetime.utcnow())
        await sctx.response.send_message(embed=embed)
  

  
  @app_commands.command(name="encode",description="encodes decoded text")
  async def encodes(self,sctx:discord.Interaction,text:str):
    
        content=requests.get(f"https://normal-api.tk/encode?text={text}").text
        data=json.loads(content)
        embed=discord.Embed(title=f"Encoded {text}", description=f"{data['encoded']}",timestamp=datetime.utcnow())
        await sctx.response.send_message(embed=embed)

  
  @app_commands.command(name="djoke",description="Get a dad joke")
  async def djokes(self,sctx:discord.Interaction):
    content=requests.get("https://icanhazdadjoke.com/slack").text
    data=json.loads(content)
    embed=discord.Embed(description=data['attachments'][0]['text'],timestamp=datetime.utcnow())
    await sctx.response.send_message(embed=embed)
    


  @app_commands.command(name="hp", description="Get data about Harry Potter cast")
  async def hp(self, sctx:discord.Interaction):
   async def getData():
    i=  random.randint(0,24)
    content = requests.get("http://hp-api.herokuapp.com/api/characters")
    if not content.ok:
      asyncio.sleep(1)
      content = requests.get("http://hp-api.herokuapp.com/api/characters")
      if not content.ok:
        await sctx.response.send_message("connection to the server timedout")
        return
    content = content.text
    try:
      data = json.loads(content)
    except:
      await sctx.response.send_message("Harry Potter Api undergoing maintance therefore this commands isn't available")
      return

      
    embed = discord.Embed(title=f"**{data[i]['name']}**", description=f"Species: {data[i]['species']}",colour=random.choice(self.colours),timestamp=datetime.utcnow())
    if not data[i]["house"] == None or not data[i]["house"] == "":
      embed.add_field(name="> House:", value=f"{data[i]['house']}")
    else:
      embed.add_field(name="> House:", value=f"unknown")
    if not data[i]["ancestry"] == None or not data[i]["ancestry"] == "":
      embed.add_field(name="> House:", value=f"{data[i]['ancestry']}")
    else:
      embed.add_field(name="> House:", value=f"unknown")

    if "http" in data[i]['image']:
      embed.set_image(url=f"{data[i]['image']}")
      return embed
      
   while True:
     try:
       await sctx.response.send_message(embed=await getData())
       break
     except:
       pass



  @app_commands.command(name="meme", description="Returns a meme")
  async def meme(self, sctx:discord.Interaction):
    content = requests.get("https://meme-api.herokuapp.com/gimme/meme").text
    data = json.loads(content,)
    
    meme = discord.Embed(title=f"{data['title']}", color = discord.Color.random(),timestamp=datetime.utcnow())
    meme.set_image(url=f"{data['url']}")

    view = View()
    bt = Button(label="New")

   
    async def memeButtonFunc(int):
          content = requests.get("https://meme-api.herokuapp.com/gimme/meme").text
          data = json.loads(content,)
          meme = discord.Embed(title=f"{data['title']}", color = discord.Color.random(),timestamp=datetime.utcnow())
          meme.set_image(url=f"{data['url']}")
          
          await int.response.edit_message(embed=meme)

    bt.callback = memeButtonFunc
    view.add_item(bt)
    await sctx.response.send_message(embed=meme,view=view)
    
  

  @app_commands.command(name="nfact", description="Returns a fact about a number")
  async def nfact(self, sctx:discord.Interaction,number:int=0):
    
    if number:
      content=requests.get(f"http://numbersapi.com/{number}/trivia?json").text
      data=json.loads(content)
      
    else:
      content=requests.get("http://numbersapi.com/random/trivia?json").text
      data=json.loads(content)
      
    embed=discord.Embed(title=f"{data['number']}", description=f"{data['text']}",timestamp=datetime.utcnow())
    embed.set_thumbnail(url="https://cutewallpaper.org/21/matrix-gif-background/Matrix-Gif-GIF-Find-and-Share-on-GIPHY.gif")
    await sctx.response.send_message(embed=embed)
      

    

  @app_commands.command(name="q",description="Returns a random qoute if today is not stated")
  async def _quote(self, sctx:discord.Interaction,today:str="lol"):
    
    if today.lower()=="today" or today.lower()=="t":
      content=requests.get("https://zenquotes.io/api/today").text
      data=json.loads(content)
      em=discord.Embed(timestamp=datetime.utcnow())
      em.add_field(name=f"**{data[0]['q']}**",value=f"By: `{data[0]['a']}`")
      await sctx.response.send_message(embed=em)
      return

    content=requests.get("https://zenquotes.io/api/random").text
    data=json.loads(content)

    em=discord.Embed(timestamp=datetime.utcnow())
    em.add_field(name=f"**{data[0]['q']}**",value=f"By: `{data[0]['a']}`")
    await sctx.response.send_message(embed=em)
    return
  


  @app_commands.command(name="recipe", description="Returns a random food recipe")
  async def recipe(self, sctx:discord.Interaction):
    content=requests.get("https://api.spoonacular.com/recipes/random?apiKey=6a4cc535ccd1498791668e638b2b8af7").text
    python=json.loads(content)

    em = discord.Embed(title=f"**{python['recipes'][0]['title']}**", description=f"Ready in: `{python['recipes'][0]['readyInMinutes']} minutes`\nSteps: [{python['recipes'][0]['sourceUrl']}]({python['recipes'][0]['sourceUrl']})")
    em.set_image(url=f"{python['recipes'][0]['image']}")
    
    await sctx.response.send_message(embed=em)



  #trivia
  @app_commands.command(name="trivia", description="Place 'T' for a True or False question. Place 'M' for a multiple choice question")
  async def _trivia(self, sctx:discord.Interaction, choice:str=None):
    view = View()

    if choice == None:
      choice = random.choice(["t","m"])
    if choice== "T".lower():
      content=requests.get("https://opentdb.com/api.php?amount=1&type=boolean").text
      data=json.loads(content)

      if "&quot;" in data['results'][0]['question']:
        new= data['results'][0]['question'].strip("&quot;")
      
      em=discord.Embed(title="**True or False**",timestamp=datetime.utcnow())
      em.add_field(name=f"**Category**: `{data['results'][0]['category']}`",value=f"**Type:**`{data['results'][0]['type']}`",inline=False)
    
      if "&quot;" in data['results'][0]['question'] or "2&quot;" in data['results'][0]['question']:
        s= data['results'][0]['question'].replace("&quot;","\"")
        s= s.replace("2&quot;","\"")
        s= s.replace("&#039;","\"")
        s= s.replace("&rsquo;","\"")
        s= s.replace("&ldquo;","\"")
        em.add_field(name=f"**Difficulty:** `{data['results'][0]['difficulty']}`",value=f"**Question:** `{s}`",inline=False)
      
      else:      
         s= data['results'][0]['question'].replace("&quot;","\"")
         s= s.replace("2&quot;","\"")
         s= s.replace("&#039;","\"")
         s= s.replace("&rsquo;","\"")
         s= s.replace("&ldquo;","\"")
         em.add_field(name=f"**Difficulty:** `{data['results'][0]['difficulty']}`",value=f"**Question:** `{s}`",inline=False)


    
      True_button= Button(label="True", style=discord.ButtonStyle.green)
      False_button=Button(label="False",style=discord.ButtonStyle.blurple)

      async def trueFunc(inte):
        if True_button.label==f"{data['results'][0]['correct_answer']}":
          em.add_field(name=f"**         :white_check_mark:Correct**",value=f"The answer was: **{data['results'][0]['correct_answer']}**")
          await inte.response.edit_message(embed=em,view=None)
          return
      
        else:
          em.add_field(name=f"**        :negative_squared_cross_mark:Wrong**",value=f"The answer was: **{data['results'][0]['correct_answer']}**")
          await inte.response.edit_message(embed=em,view=None)
          return

      async def falseFunc(inte):
        if False_button.label==f"{data['results'][0]['correct_answer']}":
          em.add_field(name=f"**         :white_check_mark:Correct**",value=f"The answer was: **{data['results'][0]['correct_answer']}**")
          await inte.response.edit_message(embed=em,view=None)
          return
      
        else:
          em.add_field(name=f"**        :negative_squared_cross_mark:Wrong**",value=f"The answer was: **{data['results'][0]['correct_answer']}**")
          await inte.response.edit_message(embed=em,view=None)
          return

          
      True_button.callback = trueFunc
      False_button.callback = falseFunc

      view.add_item(True_button)
      view.add_item(False_button)
      
      await sctx.response.send_message(embed=em,view=view)

    if choice ==  "M".lower() or choice=="Multiple".lower():
      content=requests.get("https://opentdb.com/api.php?amount=1&type=multiple").text
      data=json.loads(content)
      a=data['results'][0]['incorrect_answers']
      c=data['results'][0]['correct_answer']
      
      em=discord.Embed(title="**Multiple choice**",timestamp=datetime.utcnow())
      
      em.add_field(name=f"**Category:** {data['results'][0]['category']}",value=f"**Type**:{data['results'][0]['type'].upper()}",inline=False)
      
      if "&quot;" in data['results'][0]['question'] or "2&quot;" in data['results'][0]['question']:
        s= data['results'][0]['question'].replace("&quot;","\"")
        s= s.replace("2&quot;","\"")
        s= s.replace("&rsquo;","\"")
        s= s.replace("&ldquo;","\"")
        s= s.replace("&#039;","\"")
        
        em.add_field(name=f"**Difficulty:** `{data['results'][0]['difficulty']}`",value=f"**Question:** `{s}`",inline=False)
        
      else:      
         s= data['results'][0]['question'].replace("&quot;","\"")
         s= s.replace("2&quot;","\"")
         s= s.replace("&#039;","\"")
         s= s.replace("&rsquo;","\"")
         s= s.replace("&ldquo;","\"")
         em.add_field(name=f"**Difficulty:** `{data['results'][0]['difficulty']}`",value=f"**Question:** `{s}`",inline=False)
   
      x=[i for i in(a)]
      x.append(c)

      

      view = View()

      col = [discord.ButtonStyle.green, discord.ButtonStyle.blurple, discord.ButtonStyle.gray, discord.ButtonStyle.red]
      random.shuffle(col)
      
      button1= Button(label=x[0],style=col[0])
      button2= Button(label=x[1],style=col[1])
      button3= Button(label = x[2],style=col[2])
      button4= Button(label = x[3],style=col[3])

      async def correctAns(inte):
        em.add_field(name=f"**         :white_check_mark:Correct**",value=f"The answer was **{c}**")
        await inte.response.edit_message(embed=em,view=None)
        return  

      async def wrongAns(inte):
        em.add_field(name=f"**        :negative_squared_cross_mark:Wrong**",value=f"The answer was **{c}**")
        await inte.response.edit_message(embed=em,view=None)
        return  

      button4.callback = correctAns
      button1.callback=wrongAns
      button2.callback=wrongAns
      button3.callback= wrongAns

      allButtStr = ["button1", "button2", "button3", "button4"]
    

      random.shuffle(allButtStr)
      
      for ind in allButtStr:
        string = f"view.add_item({ind})"
        
        
        exec(string)

      allButt = []
      for k in allButtStr:
        if k[-1] == "1":
          allButt.append(button1)
        if k[-1] == "2":
          allButt.append(button2)
        if k[-1] == "3":
          allButt.append(button3)
        if k[-1] == "4":
          allButt.append(button4)

      x = [p.label for p in allButt]
      
      d="\n".join(i for i in x)
      em.add_field(name="**Options:**",value=f'`{d}`',inline=False)
      await sctx.response.send_message(embed=em,view=view)
      return
      
      


  #translate
  @app_commands.command(name="translate", description="Returns a translated text")
  async def translate(self,sctx:discord.Interaction,translate_to:str,text:str):
    content= requests.get(f"https://translate-api.ml/translate?text={text}&lang={translate_to}")
    if not content.ok:
      await sctx.response.send_message("please use valid acronyms for a language")
      return

    content = content.text
    data=json.loads(content)
    embed=discord.Embed(title=f"Translation of {text} from [{data['given']['lang']}] to {translate_to}:", description=f"{data['translated']['text']}",timestamp=datetime.utcnow())
    await sctx.response.send_message(embed=embed)
        


  @app_commands.command(name="ym", description="Returns a Yo mama joke")
  async def ym(self, sctx:discord.Interaction,member:discord.Member=None):
    content=requests.get("https://api.yomomma.info/").text
    data=json.loads(content)
    joke= data['joke']
    joke= joke.replace(joke[0:2],"Joe")
    if member==None:
        await sctx.response.send_message(joke)
    else:
        await sctx.response.send_message(f"{member}, {joke}")
  

    #twitter
  @app_commands.command(name="twitter",description= "Info about a twitter account")
  async def twitter(self, sctx:discord.Interaction,name:str=None):
    if name==None:
      name="Ninja"
      
    consumer_key= os.environ["twitter_consumer_key"]
    
    consumer_secret= os.environ["twitter_consumer_secret"]
    access_token= os.environ["twitter_access_token"]
    
    access_secret= os.environ["twitter_access_secret"]
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  #url = auth.get_authorization_url()
  #start,token= url.split("=")
    auth.set_access_token(access_token, access_secret)
    api= tweepy.API(auth)
    friends=[]
    follow_count= []
    j=0
    try:
      user= api.get_user(screen_name= name)
    except:
      return
    try:
      for p in user.friends():
        friends.append(p.screen_name)
        j+=1
        if j== 5:
          break
    except:
      return
    for fcs in friends:
      ff= api.get_user(screen_name=fcs)
      fc= ff.followers_count
      follow_count.append(fc)
    data= {}
    lol= {}
    for js in friends:
      d= friends.index(js)
      data[js]={}
      data[js]["Name"]=js
      data[js]["Followers"]= follow_count[d]
      d= data[js]["Followers"]
      lol[js]=d
    pfp= user.profile_image_url
    name= user.screen_name
    url= user.url
    jhd= f"{[name]}{(url)}"
    
    if len(user.description)>=0 or len(user.description)== None:
      user.description="None"
    em= discord.Embed(description=f"**{name}**\n**> Bio: **`{user.description}`\n**> Followers:** `{(user.followers_count):,}`\n**Website:** {url}")
    em.add_field(name=f'**Friends[{user.friends_count}]:**',value='`\n'+ f'`\n`'.join(i+ f": {lol[i]:,} followers " for i in lol)+"`")
    em.set_thumbnail(url=pfp)
    await sctx.response.send_message(embed=em)


  
async def setup(client):
  await client.add_cog(apislashcommands(client))

