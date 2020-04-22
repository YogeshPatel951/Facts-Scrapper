import pandas as pd
import requests
from bs4 import BeautifulSoup
linkls=[]
catls=[]
factlist=[]
categorylist=[]
cnt=0
page=requests.get('https://thefactfile.org')
soup=BeautifulSoup(page.content,'html.parser')
linkelem=soup.find_all('h3',{'class':'entry-title td-module-title'})
catlem=soup.find_all('a',{'class':'td-post-category'})
for item,cat in zip(linkelem,catlem):
    linkls.append((item.find('a')).get('href'))
    catls.append(cat.get_text())
sz=len(linkls)    
for l,c in zip(linkls,catls):
    cnt=cnt+1
    print(str(cnt)+' / '+ str(sz))
    category=c
    ppage=requests.get(l)
    psoup=BeautifulSoup(ppage.content,'html.parser')
    post=psoup.find('div',{'class':'td-post-content'})
    factcon=post.find_all('p',{'class':None})
    for f in factcon:
        factlist.append(f.get_text())
        categorylist.append(c)
        
print("making dataFrame")
a=pd.DataFrame({
        'Facts':factlist,
        'Category':categorylist
    })
print("No. of Rows in Frame: "+ str(a.shape[0]))
print("********Making CSV ********")
a.to_csv('TheFactFile.csv')

        
        

