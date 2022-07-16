'''
curl -v -X GET "https://dapi.kakao.com/v2/local/search/address.json" \
  -H "Authorization: KakaoAK ${REST_API_KEY}" \
  --data-urlencode "query=전북 삼성동 100" 
'''

import requests
REST_API_KEY = 'd2655853bc943c913c772015760bb183'
headers = {'Authorization': f'KakaoAK {REST_API_KEY}'}
addr = input('주소입력 >>> ')
url = f"https://dapi.kakao.com/v2/local/search/address.json?query={addr}"
print(url)
r = requests.get(url,headers=headers)
print(r.json())
data = r.json()
print('경도:',data['documents'][0]['x'])
print('위도:',data['documents'][0]['y'])