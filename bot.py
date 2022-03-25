from urllib.request import urlopen, Request
import discord 
from discord.ext import tasks, commands
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

urln = "https://neoxscans.net/wp-content/uploads/2021/05/cropped-neoxscans-270x270.png"

#Crie um arquivo config.json
with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    prefix = data["PREFIX"]
    url = data["URL"]    
    User_Agent = data["USER_AGENT"]

bot = commands.Bot(prefix)

@bot.event
async def on_ready():
        print("Ready")
        #current_manga.start()

@bot.command(name="list")
async def send_lastlist(ctx):
                
        
        headers = {"User-Agent": User_Agent}
        req = Request(url,headers=headers)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html,'html.parser')

        i=0
        m= 3

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
                tipo3cc = soup1.find('div', class_="post-title").span.get_text().lstrip()
                

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
                
              
                await ctx.send(embed=embed)

@tasks.loop(minutes=20)
async def current_manga():
                
        
        headers = {"User-Agent": User_Agent}        
        req = Request(url,headers=headers)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html,'html.parser')

        i=0
        m= 3
        channel = bot.get_channel(956642152195194882)

        for i in range(0,int (m)):
        
                tabsitens =soup.find_all('div', class_="row c-tabs-item__content")
                itens = tabsitens[i]

                titulo = itens.find_next('h3', class_="h4", ).get_text().strip()
                        
                link = itens.find_next(href=True)

        
                titulo2= titulo

                link2 = link['href']
                
                response =  titulo2 + "  -  " + link2

                

                await channel.send(response)                
        
      

                
   





    
bot.run(token)

