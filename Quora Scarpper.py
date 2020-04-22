import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
link='https://www.quora.com/topic/Job-Interviews'
browser = webdriver.Chrome()
browser.get(link)
page=requests.get(link)
time.sleep(1)
dn=2
main=browser.find_element_by_tag_name("body")
while dn:
    main.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    dn-=1    

linkk=main.find_element_by_class_name('ui_qtext_more_link')
soup=BeautifulSoup(page.content,'html.parser')
soup=soup.find_all('a',{'class':'ui_qtext_more_link'})
links=[('https://www.quora.com'+item.get('href')) for item in soup]
print(linkk)
