# BeautifulSoup_03
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

"""
URL = 'https://stackoverflow.com/questions/tagged/python'
page = urlopen(URL)
doc = page.read()
# print(doc)
page.close()

# 패키지 lxml -> bs4 -> html5lib 설치

soup = BeautifulSoup(doc, 'html5lib')
print(soup)

question = soup.find(id='questions')
print(question)

question_list = question.find_all('a', class_='s-link')
print(question_list)

for que in question_list:
    print('질문 : ', que.get_text())  # 컨텐츠만 추출
    print('질문 URL : ', 'https://stackoverflow.com'+que.get('href'))
"""
"""
URL = 'http://www.kb.or.kr/p/?j=41'
page = urlopen(URL)
doc = page.read()

noticedic = {}
soup = BeautifulSoup(doc, 'html5lib')
notice = soup.find(id='ej-tbl')
notice_list = notice.find_all('a')
print(notice_list)

num = 0
for que in notice_list:
    # print(f'공지 {num} : {que.text}')
    # print(f'공지 {num} : {que.get_text()}')
    # print(f'공지 {num} : {que.get("title")}')
    # print('링크 -> ', 'http://www.kb.or.kr' + que.get('href')[2:])
    noticedic[num] = {que.text: 'http://www.kb.or.kr' + que.get('href')[2:]}
    num += 1

for key, value in noticedic.items():
    print(f'\033[95m{key} \033[93m{value}')
"""
'''
# 네이버 영화
# 네이버 영화 평점순 순위
URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20230117'
res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = res.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
movieTitlelist = []
movieScorelist = []
movieURLlist = []
moviedic = {}

for i in soup.select('div[class=tit5] > a'):
    # print(i)
    movieTitlelist.append(i.text)

    # print('타이틀 : ', movieTitlelist)

for a in soup.select('div[class=tit5] > a'):
    # print(i)
    # print(a.get('href'))
    movieURLlist.append('https://movie.naver.com/movie/sdb/rank/' + a.get('href'))

for j in soup.select('td[class=point]'):
    # print(i)
    movieScorelist.append(j.text)

    # print('평점 : ', movieScorelist)
    moviedic = dict(zip(movieTitlelist, movieScorelist))

num = 0
for key, value in moviedic.items():
    print(f'{num+1} {key} {value} ')
    print(' URL ->', movieURLlist[num])
    num += 1
'''
# 게시판 전부다 출력

num = 0
noticedic = {}
for url_num in range(1, 24):
    URL = f'http://www.kb.or.kr/p/index.php?j=41&ej_code=notice&st=100&sv=&pno=15&sort=0&page={url_num}'
    page = urlopen(URL)
    doc = page.read()

    soup = BeautifulSoup(doc, 'html5lib')
    notice = soup.find(id='ej-tbl')
    notice_list = notice.find_all('a')

    noticelist = []
    noticeurl = []

    for que in notice_list:
        # noticedic[num] = {que.text: 'http://www.kb.or.kr' + que.get('href')[2:]}
        noticelist.append(que.text)
        noticeurl.append('http://www.kb.or.kr' + que.get('href')[2:])
        num += 1

    # 리스트 2개를 하나의 딕셔너리로 만들기
    # dictionary = dict(zip(key, value))
    noticedic = dict(zip(noticelist, noticeurl))

    for key, value in noticedic.items():
        print(f' \033[95m{key} \033[93m{value}')
        

'''
def noticelist(a, b):
    num = 0
    noticedic = {}
    for url_num in range(a, b, -1):
        url = f'http://www.kb.or.kr/p/index.php?j=41&ej_code=notice&st=100&sv=&pno=15&sort=0&page={url_num}'
        page = urlopen(url)
        doc = page.read()

        soup = BeautifulSoup(doc, 'html5lib')
        notice = soup.find(id='ej-tbl')
        notice_list = notice.find_all('a')

        for que in notice_list:
            noticedic[num] = {que.text: 'http://www.kb.or.kr' + que.get('href')[2:]}
            num += 1

    return noticedic


if __name__ == '__main__':
    dic = noticelist(20, 1)

    print(type(dic))

    for key, value in dic.items():
        print(f'{key} {value}')
'''
