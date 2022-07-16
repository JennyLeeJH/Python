from bs4 import BeautifulSoup
import urllib.request
import requests

starbugs = requests.get('https://www.starbucks.co.kr/store/store_map.do')
print(starbugs.text)
soup = BeautifulSoup(starbugs.text,'lxml')
item = soup.select_one('li.quickResultLstCon')
print(item)