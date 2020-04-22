
#### Change this According to your path ########################

excel_file_path= (r"C:\Users\Dell\Downloads\ejxample.xlsx")
chrome_driver_path=(r'chromedriver')

################################################################


import time
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import pandas as pd
def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None
driver= webdriver.Chrome(chrome_driver_path)
driver.get('http://latinresearch.org/65-2/')
a=pd.read_excel(excel_file_path)
emailadd= ""
last_name=""
first_name=""
x,y= a.shape
for i in range(x):
    emailadd= a.iloc[i,2]
    last_name= a.iloc[i,1]
    first_name= a.iloc[i,0]
    fname=driver.find_element_by_id('dk-speakout-first-name-1')
    fname.send_keys(first_name)
    lname=driver.find_element_by_id('dk-speakout-last-name-1')
    lname.send_keys(last_name)
    email=driver.find_element_by_id('dk-speakout-email-1')
    email.send_keys(emailadd)
    driver.find_element_by_xpath('//*[@id="dk-speakout-petition-1"]/form/div[6]/button/span').click() 
    wait=ui.WebDriverWait(driver,5)
    wait.until(page_is_loaded)
    time.sleep(3)
    driver.refresh()




