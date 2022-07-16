from lib2to3.pgen2 import driver
from selenium import webdriver
import os,time
path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.implicitly_wait(15)

driver.fullscreen_window()
time.sleep(3)
driver.minimize_window()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.set_window_rect(100,100,500,500)
time.sleep(3)
print(driver.get_window_rect())
time.sleep(3)
driver.set_window_position(0,0)
time.sleep(3)
driver.quit()