id='아이디'
pw='패스워드'

from selenium import webdriver
from selenium.webdriver.common.by import By
import os,time

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.get('https://nid.naver.com/nidlogin.login')

driver.implicitly_wait(10)
# input_id = driver.find_element(By.ID,'id')
# input_id.send_keys(id)
# input_pw = driver.find_element(By.ID,'pw')
# input_pw.send_keys(pw)

driver.execute_script("document.getElementById('id').value=\'"+id+"\'")
driver.execute_script("document.getElementById('pw').value=\'"+pw+"\'")
time.sleep(5)
button_login = driver.find_element(By.CLASS_NAME,'btn_login')
button_login.click()

btn = driver.find_element(By.CLASS_NAME,'btn_cancel')
btn.click()
time.sleep(5)

driver.get('https://order.pay.naver.com/home')
npoint = driver.find_element(By.CSS_SELECTOR,'dl.my_npoint strong')
print(npoint.text)