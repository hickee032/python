from urllib.request import urlopen
from bs4 import BeautifulSoup
# lxml, bs4, html5lib 설치

URL = 'http://stackoverflow.com/questions/tagged/python'
page = urlopen(URL)
doc = page.read()
#print(doc)
page.close()

soup = BeautifulSoup(doc, 'html5lib')
#print(soup)
question = soup.find(id='questions')
#print(question)

question_list = question.find_all('a', class_='s-link')
print(question_list)

for que in question_list:
    print('질문정보:', que.get_text()) # 컨텐츠만 추출
    print('질문URL:',
          'http://stackoverflow.com'+que.get('href'))
    print('=========================================')

# kb.or.kr -> 커뮤니티 -> 공지사항 
# 게시물의 제목과 URL 링크 추출하기










