# BeautifulSoup_02

import requests as requests
from bs4 import BeautifulSoup
import re
# http protocol(네트워크 규약)
# request(클라이언트) -> response(서버)
# URL = 'https://news.naver.com/main/list.nhn'
# res = requests.get(URL, headers={'User-Agent':'Mozilla/5.0'})
# html = res.text
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# # 네이버 뉴스 속보
# for i in soup.select('span[class=lede]'):
#     print(i.text.strip())

# find: 태그를 검색하여 원하는 부분 추출
# select: tag 객체를 검색하여 추출

"""
# http protocol
URL = 'https://news.naver.com/main/list.nhn'
res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = res.text
soup = BeautifulSoup(html, 'html.parser')
print(soup)

# 순수 데이터 처리하기
for i in soup.select('span[class=lede]'):
    print(i)
"""
# 네이버 영화 조회순 순위
"""
URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = res.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
movielist = []
moviedic = {}

num = 1
# for i in soup.select('div.tit3 > a'):
for i in soup.select('div[class=tit3] > a'):
    # print(i)
    print(i.text)
    movielist.append(i.text)
    moviedic[num] = i.text
    num += 1

print(movielist)
print(movielist[0])

print(moviedic)

for key, value in moviedic.items():
    print(key, value)
"""

# 네이버 영화 평점순 순위
URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20230115'
res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = res.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
movieTitlelist = []
movieScorelist = []
moviedic = {}

for i in soup.select('div[class=tit5] > a'):
    # print(i)
    print(i.text)
    movieTitlelist.append(i.text)

    # print('타이틀 : ', movieTitlelist)

for j in soup.select('td[class=point]'):
    # print(i)
    print(j.text)
    movieScorelist.append(j.text)

    # print('평점 : ', movieScorelist)

for k in range(len(movieTitlelist)):
    moviedic[k] = {movieTitlelist[k]: movieScorelist[k]}

for key, value in moviedic.items():
    pkey = str(value.keys())[12:-3]
    pvalue = str(value.values())[14:-3]
    print(f'{key} {pkey} {pvalue}')

