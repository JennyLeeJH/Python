'''
부경대학교 용당캠퍼스
경도: 129.089434819122
위도: 35.1159904918259
'''
import requests
REST_API_KEY = 'd2655853bc943c913c772015760bb183'
headers = {'Authorization': f'KakaoAK {REST_API_KEY}'}
query = input('편의점 이름 >>> ')
x=129.089434819122
y=35.1159904918259
radius=2000
url = f"https://dapi.kakao.com/v2/local/search/keyword.json?y={y}&x={x}&radius={radius}&category_group_code=CS2&query={query}"
print(url)
r = requests.get(url,headers=headers)
print(r.json())
data = r.json()
print('경도:',data['documents'][0]['x'])
print('위도:',data['documents'][0]['y'])