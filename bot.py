from urllib.request import urlopen, Request
from xmlrpc.client import Boolean
import discord 
from discord.ext import commands
import json
from re import I
from urllib.request import urlopen, Request
from xmlrpc.client import Boolean
from bs4 import BeautifulSoup

with open('config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    prefix = data["PREFIX"]


bot = commands.Bot(prefix)

@bot.event
async def on_ready():
        print("Ready")


@bot.command(name="list")
async def send_lastlist(ctx):
                
        url = "https://neoxscans.net/?s&post_type=wp-manga&m_orderby=latest"
        headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
        req = Request(url,headers=headers)
        response = urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html,'html.parser')

        i=0
        m= 3

        for i in range(0,int (m)):
        
                tabsitens =soup.find_all('div', class_="row c-tabs-item__content")
                itens = tabsitens[i]

                titulo = itens.find_next('h3', class_="h4", ).get_text().strip()
                        
                link = itens.find_next(href=True)

        
                titulo2= titulo

                link2 = link['href']
                
                response =  titulo2 + "  -  " + link2
                await ctx.send(response)
        
      

                
   





    
bot.run(token)

