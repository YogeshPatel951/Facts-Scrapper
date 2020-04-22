import pandas as pd
import requests
from bs4 import BeautifulSoup
import re



    
pd.options.display.max_colwidth = 10000000
link='https://web.archive.org/web/20171024063612/http://lanyrd.com/profile/peterfriese/'
Name=[]
DP_URL=[]
Title=[]
City=[]
Country=[]
Attened_Events=[{}]
All_Videos=[{}]
Topics=[]
Slide_Decks=[{}]
Linkedin=[]
Twitter=[]
Wikipedia=[]
Facebook=[]
Website=[]


    
page=requests.get(link)
soup=BeautifulSoup(page.content,'html.parser')
Name.append(soup.find('h1',{'class':'fn n'}).get_text())
DP_URL.append(soup.find('div',{'class':'avatar avatar-big-profile'}).find('img').get('src'))
Title.append((soup.find('p',{'class':'tagline'})).get_text() if (soup.find('p',{'class':'tagline'})) else "N/A")
City.append((soup.find('a',{'class':'sub-place'})).get_text() if (soup.find('a',{'class':'sub-place'})) else "N/A")
Country.append((((soup.find('span',{'class':'place-context'})).find('a').get_text())) if((((soup.find('span',{'class':'place-context'}))))) else "N/A")

####Attending#####0
attendLink="https://web.archive.org"+((soup.find(class_='number-feature').find('a').get('href')).replace('speaking','attending'))
attendsoup=BeautifulSoup((requests.get(attendLink)).content,'html.parser')

for it in attendsoup.find_all('div',{'class':'pagination'}):
    for item in ((it.find_all('li'))):
        if()
    

        

              

print(Name)
print(DP_URL)
print(Title)
print(City)
print(Country)

              















##
##a=pd.DataFrame({
##        'Company':Head,
##        'Content URl':uri,
##        'Content':content
##    })
##a.to_csv('a.csv')


