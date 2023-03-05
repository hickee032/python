import re
import urllib.request
from bs4 import BeautifulSoup

# with open("exam.html", 'r', encoding="UTF-8") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
# print(soup)

# url = 'https://movie.daum.net/magazine/new'
# with urllib.request.urlopen(url) as res:
#     html = res.read()
#     soup = BeautifulSoup(html, 'html.parser')
# print(soup)

# with open("exam.html", 'r', encoding="UTF-8") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
#     all_divs = soup.find_all('div') # 모든 div 검색
#     #print(all_divs)
#     # 정규식 패턴 참고
#     # . : '\n'을 제외한 모든 문자
#     # + : 앞 패턴이 하나 이상이어야 함
#     # ? : 앞 패턴이 없거나 하나이어야 함
#     # re.sub(패턴, 바꿀 문자열, 원본 문자열)
#     all_divs = re.sub('<.+?>', '', str(all_divs)).strip()
#     print(all_divs)

# 1개의 태그 정보만 검색 (중복이면 1번째 정보만 검색)
# with open("exam.html", 'r', encoding="UTF-8") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
#     all_divs = soup.find('div')
#     all_divs = re.sub('<.+?>', '', str(all_divs)).strip()
#     print(all_divs)

# with open("exam.html", 'r', encoding="UTF-8") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
#     # '태그명', {'속성':'값'}
#     ex_class = soup.find('div', {'class':'ex_class'})
#     ex_class = re.sub('<.+?>', '', str(ex_class)).strip()
#     print(ex_class)

# div 태그에서 id = 'ex_id' 정보를 찾아서 순수 data 출력
# with open("exam.html", 'r', encoding="UTF-8") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
#     # '태그명', {'속성':'값'}
#     ex_id = soup.find('div', {'id':'ex_id'})
#     print(ex_id)
#     ex_id = re.sub('<.+?>', '', str(ex_id)).strip()
#     ex_list = [ex_id] # ex_list = list(ex_id)

# 모든 p 태그의 순수 data를 출력
with open("exam.html", 'r', encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    ptag = soup.find_all('p')
    p_value = re.sub('<.+?>', '', str(ptag)).strip()
    #print(p_value)
    p_value_list = p_value[1:-1]
    p_value_list = re.sub(',', '', str(p_value_list))
    p_value_list = p_value_list.split(' ')
    for n in p_value_list:
        print(n, end='\t')








