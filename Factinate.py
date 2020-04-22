import requests
from bs4 import BeautifulSoup
import pandas as pd
link=['https://www.factinate.com/category/people/']
page=requests.get('https://www.factinate.com/category/people/')
soup=BeautifulSoup(page.content,'html.parser')
total=(((soup.find('div',{'class':'wp-pagenavi'})).find('span')).get_text()).replace('1/','')
for i in range(2,int(total)+1):
    uri=('https://www.factinate.com/category/people/page/'+str(i)+'/')
    link.append(uri)
link.append('https://www.factinate.com/category/places/')
plinkls=[]
fact=[]
factp=[]
b=pd.DataFrame({
        'Facts':['NULL'],
        'Category':['NULL']
    })
for item in link:
    ppage=requests.get(item)
    psoup=BeautifulSoup(ppage.content,'html.parser')
    plink=psoup.find_all('div',{'class':'c-be-body post-title'})
    for l in plink:
        plinkls.append((l.find('a')).get('href'))
cnt=0
for a in plinkls:
    cnt=cnt+1
    print(str(cnt)+' / '+str(len(plinkls)))
    fpage=requests.get(a)
    fsoup=BeautifulSoup(fpage.content,'html.parser')
    rawfact=fsoup.find('div',{'class':'infinite_content'})
    factp=rawfact.find_all('p')
    factp.pop()
    for g in factp:
        fact.append(g.get_text())    
    fact.pop(0)
    a=pd.DataFrame({'Fact':fact,'Category':'People'})
    b=(b.append(a,ignore_index=True))
print("Making CSV")
b.to_csv('Factinate.csv')
print('Merging')
c=pd.read_csv('FactSite.csv')
c=(c.append(b,ignore_index=True))
print('Making Merged CSV')
c.to_csv('OneMillionFacts.csv')
