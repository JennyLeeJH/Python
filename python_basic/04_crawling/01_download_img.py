#import urllib.request

#url 주소값을 알고 있을 경우 사용 가능! 하지만 오류가 날 경우도 있으니 해당 경우에는 예외처리 해주면 된다.
#url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2qvBrEpA13GBLJIakRMuBXLSD2HW4XZN1Jw&usqp=CAU' #이미지 url 주소
#savename = 'test.png' #저장할 이름

#urllib.request.urlretrieve(url, savename)




# from urllib import request

url = 'https://www.naver.com/'
# mem = request.urlopen(url).read()
# print(mem.decode('utf-8'))



import requests

#r = requests.get(url)
#print(r.text)
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.stust_code)
print(r.encoding)
print(r.json())