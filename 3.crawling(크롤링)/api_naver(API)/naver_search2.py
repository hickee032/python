import json
import re
import urllib.parse
import urllib.request

search = '한파'
category = 'news'
display = 20
start = 1
sort = 'sim'

baseURL = 'https://openapi.naver.com/v1/search/'
node = f'{category}.json'
param = f'?query={urllib.parse.quote(search)}'
param += f'&display={display}'
param += f'&start={start}'
param += f'&sort={sort}'
URL = baseURL + node + param
request = urllib.request.Request(URL)
request.add_header('X-Naver-Client-Id', 'bwvcfH0XTJPsuWGdKnjW')
request.add_header('X-Naver-Client-Secret', 'b5BbKw3Owy')
try:
    response = urllib.request.urlopen(request)
    if response.getcode() == 200: # success code
        ret_data = response.read().decode('utf-8')
except Exception as ex:
    print('서버 요청 에러')

ret_data = re.sub("\\\\|<b>|<\\\\/b>|&apos;|&quot;", "", ret_data)
file_name = f'{category}_{search}.json'
try:
    with open(file_name, 'w', encoding='utf-8') as wfs:
        wfs.write(ret_data)
        print(file_name, '생성 완료!')
except Exception as ex:
    print('파일 생성 에러:', ex)

try:
    with open(file_name, 'r', encoding='utf-8') as rfs:
        dic_data = json.load(rfs)
        list_data = dic_data['items']
        for n in list_data:
            print('제목:', n['title'])
            print('링크:', n['link'])
            print('----------------------------')

except Exception as ex:
    print('파일 읽기 에러:', ex)