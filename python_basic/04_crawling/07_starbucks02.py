from bs4 import BeautifulSoup
from selenium import webdriver
import os,time

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.get('https://www.starbucks.co.kr/store/store_map.do')
time.sleep(10)
soup = BeautifulSoup(driver.page_source,'lxml')
result = soup.select('ul.quickSearchResultBox li')
for item in result:
    print(item.text)