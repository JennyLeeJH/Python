from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,os

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.get('https://www.naver.com')
query = driver.find_element(By.ID, 'query')
query.clear()
query.send_keys('여름바다')
time.sleep(3)
query.send_keys(Keys.ENTER)
time.sleep(3)
bolgitem = driver.find_element(By.CLASS_NAME,'keyword_item')
bolgitem.click()
time.sleep(3)
print(driver.page_source)