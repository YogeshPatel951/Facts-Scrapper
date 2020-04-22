import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
pd.options.display.max_colwidth = 10000000
link='https://www.geeksforgeeks.org/amazon-off-campus-all-india-campus-hiring-sde-1/'
Head=[]
content=[]
uri=[]

for i in range(10):
    page=requests.get(link)
    soup=BeautifulSoup(page.content,'html.parser')
    Content_Container=soup.find(id='content')
    Heading=Content_Container.find('header',{'class':'entry-header'}).text
    Content=Content_Container.find('div',{'class':'entry-content'}).text
    Pre_Con=soup.find(class_='nav-previous')
    A_con=Pre_Con.find('a')
    Head.append(Heading)
    content.append(Content)
    uri.append(link)
    link=A_con.get('href')
a=pd.DataFrame({
        'Company':Head,
        'Content URl':uri,
        'Content':content
    })
a.to_csv('a.csv')


