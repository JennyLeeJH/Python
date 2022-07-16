from selenium import webdriver
import os,time

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.implicitly_wait(15)

driver.get('https://www.google.co.kr')
time.sleep(3)
driver.get('https://www.youtube.com')
time.sleep(3)
driver.get('https://www.naver.com')
time.sleep(3)

driver.back()
time.sleep(3)
driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)
driver.forward()
time.sleep(3)

driver.quit()