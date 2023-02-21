# BeautifulSoup_01

# bs4 라이브러리 설치 필요
import re
import urllib.request

from bs4 import BeautifulSoup

# 첫번째 사용법
"""
with open('example.html', 'r', encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')  # html 파싱한다라는 의미 -> 전부다 가져옴
print(soup)
"""
# 두번째 사용법
"""
url = 'http://movie.daum.net/magazine/new'
with urllib.request.urlopen(url) as res:
    html = res.read()
    soup = BeautifulSoup(html, 'html.parser')
print(soup)
"""

# div를 검색
# find -> 태그 하나만
# find_all -> 모든 태그
"""
with open('example.html', 'r', encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    all_divs = soup.find_all('div')  # 모든 div를 검색
    # print(all_divs)
    # 정규식 패턴 참고
    # . : 모든 문자 (\n 은 제외)
    # + :앞 패턴이 하나 이상이어야함
    # ? :앞 패턴이 없거나 하나 이상이어야함
    # re.sub( 패턴, 바꿀 문자열, 원본 문자열 )
    all_divs = re.sub('<.+?>', '', str(all_divs)).strip()
    print(all_divs)
"""

# 한개의 태그 정보만 검색 ( 중복이면 1번째 정보만 검색 )
"""
with open('example.html', 'r', encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    all_divs = soup.find('div')
    all_divs = re.sub('<.+?>', '', str(all_divs)).strip()
    print(all_divs)
"""

# 클래스( html class )로 검색 -> ex_class
# 중복이면 1번째 정보만 검색
"""
with open('example.html', 'r', encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # ('태그명', { 속성 :  값 })
    ex_class = soup.find('div', {'class': 'ex_class'})
    ex_class = re.sub('<.+?>', '', str(ex_class)).strip()
    print(ex_class)
"""

# 아이디( html id )로 검색 -> ex_id
# find -> id는 하나만 존재
'''
with open('example.html', 'r', encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # ('태그명', { 속성 :  값 })
    ex_id = soup.find('div', {'id': 'ex_id'})
    ex_id = re.sub('<.+?>', '', str(ex_id)).strip()
    print(ex_id)
'''
"""
with open('example.html', 'r', encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # ('태그명', { 속성 :  값 })
    ex_id = soup.find('div', {'id': 'ex_id'})
    ex_id = re.sub('<.+?>', '', str(ex_id)).strip()
    ex_list = list(ex_id)
    print(type(ex_id))
    
    # 리스트에서 \n 제거
    for i in ex_list:
        if '\n' in i:
            ex_list.remove(i)

    print(ex_list)
    print(ex_id)
"""
# 모든 p 태그의 data 정보를 출력
# find_all

with open('example.html', 'r', encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    p_all = soup.find_all('p')
    p_all = re.sub('<.+?>', '', str(p_all)).strip()
    print(type(p_all))
    p_list = []
    result = p_all
    for i in p_all:
        if i in ",[]":
            result = result.replace(i, '')
    p_all.split(' ')
    print('result : ', result)
    p_list = list(result.split(' '))
    print('p_list : ', p_list)

    for n in p_list:
        print(n, end='\t')

"""
with open('example.html', 'r', encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # ('태그명', { 속성 :  값 })
    p_all = soup.find_all('p')
    p_all = re.sub('<.+?>', '', str(p_all)).strip()

    p_list = p_all[1: -1]
    p_list = re.sub(',', '', str(p_list))
    p_list = p_list.split(' ')

    for n in p_list:
        print(n, end='\t')
"""