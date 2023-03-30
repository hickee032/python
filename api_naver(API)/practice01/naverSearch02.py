import json
import re
import urllib
from urllib import parse
from urllib import request
import html


# API (Application Programming Interface)
# 다른 사용자가 사용하기 편하게 제공하는 함수, 클래스
# -> https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4


# http 에서 정보를 넘길때 get방식 post방식 두가지가 있다
search = '프로'
category = 'news'
display = 20
start_page = 1
sort = 'sim'

# 요청 URL을 만드는 과정
# -> https://openapi.naver.com/v1/search/news.json

base_URL = 'https://openapi.naver.com/v1/search/'
node = f'{category}.json'
param = f'?query={urllib.parse.quote(search)}'
# 변수를 연결하기 위해 & 사용
param += f'&display={display}'
param += f'&start={start_page}'
param += f'$sort={sort}'
t_url = base_URL + node + param
# API를 요청할 때 다음 예와 같이 HTTP 요청 헤더에 클라이언트 아이디와 클라이언트 시크릿을 추가해야 한다
request = urllib.request.Request(t_url)
# 네이버인 경우 필요 -> 대부분은 서비스 키만 필요
request.add_header('X-Naver-Client-Id', 'SrNxTWJA3SuZSEKUsT6J')
request.add_header('X-Naver-Client-Secret', 'KJl3pu_9oO')
try:
    responce = urllib.request.urlopen(request)
    if responce.getcode() == 200:  # success code
        return_data = responce.read().decode('utf-8')
except Exception as ex:
    print(f'[{datetime.datetime.now()}] 서버요청 에러 : {url}')

# 필요 없는 문자를 제거 해야함 -> <b>, &quot;, &apos; 등등

# print(return_data)  # 문자열
# print(type(return_data))  # 문자열 str 이다 0> 이 시점에서 파싱

# 정규식으로 파싱
print('-------------------',type(return_data))
return_data = re.sub("\\\\|<b>|<\\\\/b>|&apos;|&quot;","",return_data)
# 쌍따옴표 (특수문자) 를 유지 하면서 파싱
#return_data = html.unescape(return_data).replace('\\', '').replace('<b>', '').replace('</b>', '')
# print(return_data)

# dic_data = json.loads(return_data)  # 문자열을 딕셔너리 형태로 바꿈
# print(return_data)
# print(type(dic_data))

# json 파일로 저장
file_name = f'{category}_{search}.json'
# with open() 경우 close를 따로 안해줘도 된다
try:
    with open(file_name, 'w', encoding='utf-8') as wfs:
        wfs.write(return_data)
except Exception as ex:
    print('파일 쓰기 오류')

# json 파일을 불러오기
# 불러올때는 딕셔너리 형태로 불러와야 한다
try:
    with open(file_name, 'r', encoding='utf-8') as rfs:
        ret_dic = json.load(rfs)  # -> 딕셔너리 형태
        # json.loads() -> 문자열 형태
        ret_list = ret_dic["items"]
        # ret_dic['items'] items는 key
        for i in ret_list:
            print('제목', i["title"])
            print('링크', i["link"])
except Exception as ex:
    print('파일 읽기 오류', ex)
