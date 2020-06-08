import requests
from pprint import pprint
key="AIzaSyB68ntsft9Zwn3K32pXNdl1MEFA-Z-j7_Q"

# string interpolation
search=input("검색어를 입력해 주세요 : ")
q=f'q={search}'
my_type='type=video'
part='part=snippet'
url=f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}&maxResults=20'

response=requests.get(url)
data=response.json()
#pprint(data)

for data in data['items'][:10]:
    print(data['snippet']['title'], end=' 채널명 ')
    print(data['snippet']['channelTitle'])


# 1. 검색어를 입력하면
# 2. 영상들을 검색할 것
# 3. 그 영상들의 제목과 채널명