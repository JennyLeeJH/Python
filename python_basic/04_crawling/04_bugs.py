import urllib.request

from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res,'lxml')

# print(soup)
titlelist = []
title = soup.select('p.title a')

# print(len(title))
for item in title:
    titlelist.append(item.string)
artist = soup.select('p.artist > a:nth-of-type(1)')

artistlist= []
for item in artist:
    artistlist.append(item.string)
print(list(zip(titlelist,artistlist)))