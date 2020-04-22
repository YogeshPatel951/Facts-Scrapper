###
# pip requests
# pip BeautifulSoup
# pip pandas
###



import requests
from bs4 import BeautifulSoup
import pandas as pd

global rdlink

def getnextpg(soup):
    isnext=soup.find('a',{'class':'pagination-next'})
    if(isnext):
        return 'True',(soup.find('a',{'class':'pagination-next'})).get('href')
    else:
        return 'False','NULL'
    
def getrdlink(soup):
    readmore=soup.find_all('a',{'class':'fusion-read-more'})
    for i in readmore:
        rdlink.append(i.get('href'))

def getfactsfn():
    factslist=[]
    for l in rdlink:
        factpg=requests.get(l)
        factpgsoup=BeautifulSoup(factpg.content,'html.parser')
        postcon=(factpgsoup.find('div',{'class':'post-content'})).find('ol')
        if(postcon):
            li=postcon.find_all('li')
            for ft in li:
                factslist.append(ft.get_text())
        else:
            continue

    return(factslist)
    
EntLink=[
        "https://www.thefactsite.com/art-design/" ,
        "https://www.thefactsite.com/celebrities/",
        "https://www.thefactsite.com/fashion-beauty/",
        "https://www.thefactsite.com/film-television/",
        "https://www.thefactsite.com/language-literature/",
        "https://www.thefactsite.com/music/",
        "https://www.thefactsite.com/random-facts/",
        "https://www.thefactsite.com/technology/",
        "https://www.thefactsite.com/animals/",
        "https://www.thefactsite.com/environment/",
        "https://www.thefactsite.com/food-drink/",
        "https://www.thefactsite.com/health-body/",
        "https://www.thefactsite.com/life-love/",
        "https://www.thefactsite.com/math/",
        "https://www.thefactsite.com/physics/",
        "https://www.thefactsite.com/space/",
        "https://www.thefactsite.com/business-economy/",
        "https://www.thefactsite.com/crime-law/",
        "https://www.thefactsite.com/history/",
        "https://www.thefactsite.com/holidays-events/",
        "https://www.thefactsite.com/religion/",
        "https://www.thefactsite.com/travel-tourism/"
        ]
global b
b=pd.DataFrame({
        'Facts':['NULL'],
        'Category':['NULL']
    })
total=len(EntLink)
count=0
for item in EntLink :
    count=count+1
    print("Traversing Link " + str(count) + " Out Of " + str(total))
    rdlink=[]
    page=requests.get(item)
    soup=BeautifulSoup(page.content,'html.parser')
    getrdlink(soup)
    status,nextpg=getnextpg(soup)
    while(1):
        if(status=='True'):
            nxtpagere=requests.get(nextpg)
            soupofnextpg=BeautifulSoup(nxtpagere.content,'html.parser')
            getrdlink(soupofnextpg)
            status,nextpg=getnextpg(soupofnextpg)
        else:
            break
    factli=getfactsfn()
    cat=item.replace('https://www.thefactsite.com/','')
    a=(pd.DataFrame({
            'Facts':factli,
            'Category':cat
       }))
    b=(b.append(a,ignore_index=True))


    
print("Making CSV File, Please Wait")   
b.to_csv('Facts.csv')


