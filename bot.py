
import discord 
from discord.ext import tasks, commands
import json
from urllib.request import urlopen, Request
from discord.ext import commands
from bs4 import BeautifulSoup
from numpy import number
import os

with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    prefix = data["PREFIX"]
    url = data["URL"]    
    User_Agent = data["USER_AGENT"]

headers = {"User-Agent": User_Agent}        
req = Request(url,headers=headers)
response = urlopen(req)
html = response.read()
soup = BeautifulSoup(html,'html.parser')


urln = "https://neoxscans.net/wp-content/uploads/2021/05/cropped-neoxscans-270x270.png"



bot = commands.Bot(prefix)
client = discord.Client()


@bot.event
async def on_ready():
        print("Ready")
        print(bot.user.id)
        current_manga.start()



@bot.command()
async def list(ctx, *expression):

        
        m=1
        
        expression = "".join(expression)    
        m = eval(expression)
        i=0
        
        
        
        for i in range(0,int (m)):
                
            #Scraping lista de tudo da página
            tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
            itens = tabsitens[i]
                        
        #Scraping Titulo
            def manga_titulo(titulo):
                    try:
                        titulo = itens.find_next('h3', class_="h4", ).get_text().strip()
                        return titulo
                    except AttributeError:
                        titulo = "None"
                        return titulo
                

        #Scraping Manga-cap
            def manga_caplk(link): 
                    try:
                        linkk = itens.find_next('span', class_="font-meta chapter")
                        link = linkk.find_next(href=True)
                        return link['href']
                    except AttributeError:
                        link = "None"
                        return link
                

                        
        #Scraping Capitulo
            def manga_capl(cap):
                    try: 
                        cap = itens.find_next('span', class_="font-meta chapter" ).get_text().strip()
                        return cap
                    except AttributeError:
                        cap = "None"
                        return cap

        #Scraping link-manga
            def manga_url(links):
                        links =  itens.find_next('div', class_="tab-thumb c-image-hover").a
                        return links['href']
                        

        ########################## ########################## ##########################
            req1 = Request(manga_url(any),headers=headers)
            response1 = urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1,'html.parser')
        ########################## ########################## ##########################
                        
        #Scraping urlFt
            def manga_urlFt(ftb):
                    try:     
                        fta = soup1.find('div', class_="tab-summary")
                        ftb = fta.find('div', class_='summary_image').a.img
                        return ftb['data-src']
                    except AttributeError:
                        ftb = "None"
                        return ftb
                        

        #Scraping Gênero
            def manga_genre(genre):
                    try:
                        genre = soup1.find('div', class_="genres-content").get_text( ).lstrip()
                        return genre
                    except AttributeError:
                        genre = "None"
                        return genre
        #Scraping Tipo
            def manga_tipo(tipo3cc):
                    try:
                        tipo3cc = soup1.find('div', class_="post-title").span.get_text().lstrip()
                        return tipo3cc
                    except AttributeError:
                        tipo3cc = "None"
                        return tipo3cc
                

        #Scraping Rank    
            def manga_rank(rank):
                    try:
                        rank = soup1.find('div', class_="post-rating").span.get_text().lstrip()
                        return rank
                    except AttributeError:
                        rank = "None"
                        return rank
        
        
                        
########################## ########################## ########################## ########################## 
                 

            embed = discord.Embed(
                        title = "```"+ manga_titulo(all) + "```", 
                        description = "",
                        color = 0x0000FF

                )
                
               
            embed.add_field(
                 name="```Gênero```",
                 value= "" + manga_genre(all), 
                 inline= True
                 
                 )
                 
            embed.add_field(
                 name="```Tipo```",
                 value=manga_tipo(all), 
                 inline= False)

            embed.add_field(
                        name="```Cap```", 
                        value=manga_capl(all), 
                        inline= True)

            embed.add_field(
                        name="```Rank```", 
                        value=manga_rank(all), 
                        inline= True)

            embed.add_field(
                        name="```Link```", 
                        value=manga_caplk(all), 
                        inline= False )

            embed.set_footer()

            embed.set_author(
                name="Neox Scanlator",
                icon_url=urln)
            embed.set_image(
                        url=manga_urlFt(all)
                )
        
        
            await ctx.author.send(embed=embed)
                



@tasks.loop(minutes=30)
async def current_manga():

        
        channel = bot.get_channel(956642152195194882)
        
        
        
        m=3
        i=0
        
        
        
        for i in range(0,int (m)):
                
            #Scraping lista de tudo da página
            tabsitens = soup.find_all('div', class_="row c-tabs-item__content")
            itens = tabsitens[i]
                        
        #Scraping Titulo
            def manga_titulo(titulo):
                    try:
                        titulo = itens.find_next('h3', class_="h4", ).get_text().strip()
                        return titulo
                    except AttributeError:
                        titulo = "None"
                        return titulo
                

        #Scraping Manga-cap
            def manga_caplk(link): 
                    try:
                        linkk = itens.find_next('span', class_="font-meta chapter")
                        link = linkk.find_next(href=True)
                        return link['href']
                    except AttributeError:
                        link = "None"
                        return link
                

                        
        #Scraping Capitulo
            def manga_capl(cap):
                    try: 
                        cap = itens.find_next('span', class_="font-meta chapter" ).get_text().strip()
                        return cap
                    except AttributeError:
                        cap = "None"
                        return cap

        #Scraping link-manga
            def manga_url(links):
                        links =  itens.find_next('div', class_="tab-thumb c-image-hover").a
                        return links['href']
                        

        ########################## ########################## ##########################
            req1 = Request(manga_url(any),headers=headers)
            response1 = urlopen(req1)
            html1 = response1.read()
            soup1 = BeautifulSoup(html1,'html.parser')
        ########################## ########################## ##########################
                        
        #Scraping urlFt
            def manga_urlFt(ftb):
                    try:     
                        fta = soup1.find('div', class_="tab-summary")
                        ftb = fta.find('div', class_='summary_image').a.img
                        return ftb['data-src']
                    except AttributeError:
                        ftb = "None"
                        return ftb
                        

        #Scraping Gênero
            def manga_genre(genre):
                    try:
                        genre = soup1.find('div', class_="genres-content").get_text( ).lstrip()
                        return genre
                    except AttributeError:
                        genre = "None"
                        return genre
        #Scraping Tipo
            def manga_tipo(tipo3cc):
                    try:
                        tipo3cc = soup1.find('div', class_="post-title").span.get_text().lstrip()
                        return tipo3cc
                    except AttributeError:
                        tipo3cc = "None"
                        return tipo3cc
                

        #Scraping Rank    
            def manga_rank(rank):
                    try:
                        rank = soup1.find('div', class_="post-rating").span.get_text().lstrip()
                        return rank
                    except AttributeError:
                        rank = "None"
                        return rank
        
        
                        
########################## ########################## ########################## ########################## 
                 

            embed = discord.Embed(
                        title = "```"+ manga_titulo(all) + "```", 
                        description = "",
                        color = 0x0000FF

                )
                
               
            embed.add_field(
                 name="```Gênero```",
                 value= "" + manga_genre(all), 
                 inline= True
                 
                 )
                 
            embed.add_field(
                 name="```Tipo```",
                 value=manga_tipo(all), 
                 inline= False)

            embed.add_field(
                        name="```Cap```", 
                        value=manga_capl(all), 
                        inline= True)

            embed.add_field(
                        name="```Rank```", 
                        value=manga_rank(all), 
                        inline= True)

            embed.add_field(
                        name="```Link```", 
                        value=manga_caplk(all), 
                        inline= False )

            embed.set_footer()

            embed.set_author(
                name="Neox Scanlator",
                icon_url=urln)
            embed.set_image(
                        url=manga_urlFt(all)
                )
        

                
            await channel.send(embed=embed)

                






bot.run(token)

                      






                             
        
      

                
   





    


