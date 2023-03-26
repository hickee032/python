from urllib.request import urlopen
from bs4 import BeautifulSoup
# lxml, bs4, html5lib 설치

URL = 'http://kb.or.kr/p/?j=41'
page = urlopen(URL)
doc = page.read()
#print(doc)
page.close()

soup = BeautifulSoup(doc, 'html5lib')
#print(soup)
question = soup.find(id='ej-tbl')
#print(question)

question_list = question.find_all('a')
#print(question_list)

BASE_URL = 'http://kb.or.kr'
for que in question_list:
    #print('공지제목:', que.get_text()) # 컨텐츠만 추출
    print('공지제목:', que.get('title'))
    #new_href = que.get('href')[2:]
    new_href = que.get('href')
    print('제목URL:', BASE_URL + new_href[2:])
    print('=========================================')
    
# 1.제목을 Key, URL을 value 설정하여 딕셔너리에 저장 후 출력
# (옵션: 함수 사용)
# 2.공지사항 게시판의 모든 게시물 추출 (23 x 15)
# 3.네이버 영화 평점순 순위 - 제목, 평점 추출하여 출력