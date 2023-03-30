# xml data
# 국토교통부_아파트매매 실거래 상세 자료
# 지역 코드 정보를 먼저 알아야 한다
from urllib.request import urlopen
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

# 한글 이슈가 있음
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False  # 부호를 맞춰준다

# txt 파일 불러오기
df = pd.read_csv('D:\Data_crawling\법정동코드 전체자료.txt', sep='\t', encoding='cp949')
input_sido = '대구광역시 동구'
code_num = pd.Series(df[df['법정동명'] == input_sido].loc[:, '법정동코드'], dtype="string")
code = code_num.values[0][0:5]
print(code)

page = 1
numRow = 10
year = 202005

base_url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
pramiter = '?serviceKey=NMEoUhvnwRKfms6GyYCguKH9EylZibVsxnK91C%2B1iwyLQNnN%2Bj41aKFDl%2F2%2BGFMIHtlNQf6N4eVMIuLXmrFKBg%3D%3D'
pramiter += f'&pageNo={page}&numOfRows={numRow}'
pramiter += f'&LAWD_CD={code}&DEAL_YMD={year}'
URL = base_url + pramiter
print(URL)

result_xml = urlopen(URL)
result_data = result_xml.read()
soup = BeautifulSoup(result_data, 'lxml-xml')
print(soup)
items = soup.findAll('item')
itemList = []

for te in items:
    price = te.find('거래금액').text.strip()
    build_year = te.find('건축년도').text
    apt_name = te.find('아파트').text
    width = float(te.find('전용면적').text)
    floor = te.find('층').text
    print('거래금액:', price, '만원')
    print('건축년도:', build_year)
    print('아파트명:', apt_name)
    print('전용면적:', width)
    kor_width = round(float(width) / 3.31)  # 평수를 구함
    print('평수:', kor_width, '평')
    print('층수:', floor)
    dic = {'price': price, 'build_y': build_year,
           'apt_name': apt_name, 'apt_width': width,
           'ko_width': int(kor_width), 'floor': floor}
    itemList.append(dic)
    print('==================================')

df = pd.DataFrame.from_dict(itemList)
df.index = df.apt_name  # 아파트 이름을 인덱스로 지정
df = df.loc[:, ['price', 'build_y', 'apt_width', 'ko_width', 'floor']]

data_y1 = df.loc[:, 'price']  # 좌측 Y
x1 = data_y1.index
y1 = data_y1

data_y2 = df.loc[:, 'ko_width']  # 오른쪽 Y
x2 = data_y2.index
y2 = data_y2
fig, ax = plt.subplots()
# 시각화에 데이터가 데이터 프레임인지 시리즈 인지 인덱스가 무엇인지 확인
# 선 그래프 시각화 옵션 | color: 선 색깔, linewidth: 선 굵기, marker 선택
line1 = ax.plot(y1, 'o-', label='가격(만원)', color='blue', linewidth=1)
# 값 출력
for i, v in enumerate(x1):
    # plt.text(x축 데이터, y 축 데이터, 문자열)
    plt.text(v, y1[i], str(y1[i]) + '만원', fontsize=10, color='blue',
             horizontalalignment='center',  # 수평
             verticalalignment='bottom',  # 수직
             rotation=15)
plt.xticks(x1, fontsize=10, rotation=15)  # 인덱스로 세팅
plt.yticks(fontsize=10)
plt.xlabel('아파트명', fontsize=10)
plt.ylabel('가격(만원)', fontsize=10)

ax2 = ax.twinx()  # twinx() 두 겹으로 하기위해
line2 = ax2.plot(y2, '.--', label='평형',
                 color='r', linewidth=1)
for i, v in enumerate(x2):
    if y2[i] > 90.0:
        plt.text(v, y2[i] - 5, str(round(y2[i])) + '평', fontsize=10,
                 color='red', horizontalalignment='center',
                 verticalalignment='bottom', rotation=15)
    else:
        plt.text(v, y2[i] + 3, str(round(y2[i])) + '평', fontsize=10,
                 color='red', horizontalalignment='center',
                 verticalalignment='bottom', rotation=15)

plt.yticks(fontsize=10)
plt.ylabel('평형', fontsize=10)
plt.title('2020년 5월 아파트 매매', fontsize=10)  # 그래프 제목

# 범례 표시
lines = line1 + line2
labels = [line.get_label() for line in lines]
ax.legend(lines, labels, loc=1, fontsize=10)
ax.grid()
plt.show()
