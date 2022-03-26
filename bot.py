from urllib.request import urlopen, Request
import discord 
from discord.ext import tasks, commands
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from discord.utils import get


urln = "https://neoxscans.net/wp-content/uploads/2021/05/cropped-neoxscans-270x270.png"


with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    prefix = data["PREFIX"]
    url = data["URL"]    
    User_Agent = data["USER_AGENT"]

bot = commands.Bot(prefix)
client = discord.Client()


@bot.event
async def on_ready():
        print("Ready")
        current_manga.start()

@bot.command()
async def list(ctx, *expression,):
        
       
        headers = {"User-Agent": User_Agent}
        req = Request(url,headers=headers)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html,'html.parser')
       
        
        i=0
        m=0
        expression = "".join(expression)    
        m = m + eval(expression)

        
          
        

        for i in range(0,int (m)):
                

                #Scraping lista de tudo da página
                tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
                itens = tabsitens[i]
                
                #Scraping Titulo
                titulo = itens.find_next('h3', class_="h4", ).get_text().strip()

                #Scraping Manga-cap 
                linkk = itens.find_next('span', class_="font-meta chapter").a
                link = linkk.find_next(href=True)

                
                #Scraping Capitulo 
                cap = itens.find_next('span', class_="font-meta chapter" ).get_text().strip()

                #Scraping link-manga
                links =  itens.find_next('div', class_="tab-thumb c-image-hover").a
                

                ########################## ########################## ##########################
                req1 = Request(links['href'],headers=headers)
                response1 = urlopen(req1)
                html1 = response1.read()
                soup1 = BeautifulSoup(html1,'html.parser')
                ########################## ########################## ##########################
                
                #Scraping urlFt     
                fta = soup1.find('div', class_="tab-summary")
                ftb = fta.find('div', class_='summary_image').a.img
                

                #Scraping Gênero
                genre = soup1.find('div', class_="genres-content").get_text( ).lstrip()

                 #Scraping Tipo
                try:
                  tipo3cc = soup1.find('div', class_="post-title").span.get_text().lstrip()
                except AttributeError:
                  tipo3cc = "none"
                

                #Scraping Rank
                rank = soup1.find('div', class_="post-rating").span.get_text().lstrip()
            
           
                    
                ########################## ########################## ########################## ########################## ##########################          

                embed = discord.Embed(
                        title = "```"+ titulo + "```", 
                        description = "",
                        color = 0x0000FF

                )
                
               
                embed.add_field(
                 name="```Gênero```",
                 value= "" + genre, 
                 inline= True
                 
                 )
                 
                embed.add_field(
                 name="```Tipo```",
                 value=tipo3cc, 
                 inline= False)

                embed.add_field(
                        name="```Cap```", 
                        value=cap, 
                        inline= True)

                embed.add_field(
                        name="```Rank```", 
                        value=rank, 
                        inline= True)

                embed.add_field(
                        name="```Link```", 
                        value=link['href'], 
                        inline= False )

                embed.set_footer()

                embed.set_author(
                name="Neox Scanlator",
                icon_url=urln)
                embed.set_image(
                        url=ftb['data-src']
                )
                

                
@tasks.loop(minutes=30)
async def current_manga():
                
        channel = bot.get_channel(956642152195194882)
        headers = {"User-Agent": User_Agent}        
        req = Request(url,headers=headers)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html,'html.parser')


        i=0
        m=5
        

        for i in range(0,int (m)):
        
                #Scraping lista de tudo da página
                tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
                itens = tabsitens[i]
                
                #Scraping Titulo
                titulo = itens.find_next('h3', class_="h4", ).get_text().strip()

                #Scraping Manga-cap 
                linkk = itens.find_next('span', class_="font-meta chapter")
                link = linkk.find_next(href=True)

                
                #Scraping Capitulo 
                cap = itens.find_next('span', class_="font-meta chapter" ).get_text().strip()

                #Scraping link-manga
                links =  itens.find_next('div', class_="tab-thumb c-image-hover").a
                

                ########################## ########################## ##########################
                req1 = Request(links['href'],headers=headers)
                response1 = urlopen(req1)
                html1 = response1.read()
                soup1 = BeautifulSoup(html1,'html.parser')
                ########################## ########################## ##########################
                
                #Scraping urlFt     
                fta = soup1.find('div', class_="tab-summary")
                ftb = fta.find('div', class_='summary_image').a.img
                

                #Scraping Gênero
                genre = soup1.find('div', class_="genres-content").get_text( ).lstrip()

                #Scraping Tipo
                try:
                  tipo3cc = soup1.find('div', class_="post-title").span.get_text().lstrip()
                except AttributeError:
                  tipo3cc = "none"
                

                #Scraping Rank
                rank = soup1.find('div', class_="post-rating").span.get_text().lstrip()
            
           
                    
                ########################## ########################## ########################## ########################## ##########################          

                embed = discord.Embed(
                        title = "```"+ titulo + "```", 
                        description = "",
                        color = 0x0000FF

                )
                
               
                embed.add_field(
                 name="```Gênero```",
                 value= "" + genre, 
                 inline= True
                 
                 )
                 
                embed.add_field(
                 name="```Tipo```",
                 value=tipo3cc, 
                 inline= False)

                embed.add_field(
                        name="```Cap```", 
                        value=cap, 
                        inline= False)

                embed.add_field(
                        name="```Rank```", 
                        value=rank, 
                        inline= True)

                embed.add_field(
                        name="```Link```", 
                        value=link['href'], 
                        inline= False )

                embed.set_footer()

                embed.set_author(
                name="Neox Scanlator",
                icon_url=urln)
                embed.set_image(
                        url=ftb['data-src']
                )

        
                await channel.send(embed=embed)

                




bot.run(token)

                      






                             
        
      

                
   





    


