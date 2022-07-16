from selenium import webdriver
import os,time

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')

driver.implicitly_wait(15)
driver.get('https://google.co.kr')
time.sleep(5)
driver.quit()