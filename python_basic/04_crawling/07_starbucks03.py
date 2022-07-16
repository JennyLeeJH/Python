from bs4 import BeautifulSoup
from pyparsing import common_html_entity
from selenium import webdriver
import os, time
from selenium.webdriver.common.by import By


path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.get('https://www.starbucks.co.kr/store/store_map.do')
time.sleep(5)
loca = driver.find_element(By.CLASS_NAME,'loca_search')
loca.click()
time.sleep(5)

sido = driver.find_element(By.CLASS_NAME,'sido_arae_box')
lis = sido.find_elements(By.TAG_NAME,'li')
lis[5].click()
time.sleep(5)

gu = driver.find_element(By.CLASS_NAME,'gugun_arae_box')
gu_li = gu.find_elements(By.TAG_NAME,'li')
gu_li[4].click()
time.sleep(20)

result = driver.find_elements(By.CSS_SELECTOR,'ul.quickSearchResultBoxSidoGugun li')
for item in result:
    print('매장이름:',item.find_element(By.TAG_NAME,'strong').text)
    print('매장주소:',item.find_element(By.TAG_NAME,'p').text)
    print()