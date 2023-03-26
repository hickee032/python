import requests as requests
from bs4 import BeautifulSoup

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

#===========================================
# find: 태그를 검색하여 원하는 부분 추출
# select: tag 객체를 검색하여 추출
#===========================================

# 네이버 영화 조회순 순위를 리스트에 저장한 후 출력
# URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
# res = requests.get(URL, headers={'User-Agent':'Mozilla/5.0'})
# html = res.text
# soup = BeautifulSoup(html, 'html.parser')
# #print(soup)
# rank_list = []
# for i in soup.select('div[class=tit3]'):
#     rank_list.append(i.text.strip())
#
# cnt = 1
# print('==============================')
# print('네이버 영화 현재 조회 순위')
# print('==============================')
# for n in rank_list:
#     print(f'{cnt}:{n}')
#     cnt += 1

# 네이버 영화 평점순 순위(현재 상영 영화)
# URL을 직접 조사하여 해보기
URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20230115'
res = requests.get(URL, headers={'User-Agent':'Mozilla/5.0'})
html = res.text
soup = BeautifulSoup(html, 'html.parser')
rank_list = []
#for i in soup.select('div[class=tit5]'):
for i in soup.select_one('div.tit5 > a'):
    rank_list.append(i.text.strip())

cnt = 1
print('==============================')
print('네이버 영화 평점순 순위')
print('==============================')
for n in rank_list:
    print(f'{cnt}:{n}')
    cnt += 1