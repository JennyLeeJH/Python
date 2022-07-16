import os,sys,urllib.request,json

client_id = "MZ9ZRbV3eDKdiw3JaKYv"
client_secret = "KFR7kg2yME"
keyword = input('검색할 단어 >>> ')
encText = urllib.parse.quote(keyword)
url = "https://openapi.naver.com/v1/search/errata.json?query=" + encText # json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
print(response.read().decode('utf-8'))