from urllib.request import urlopen
import seaborn as sns
import pandas as pd
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

# df = pd.read_csv('법정동코드 전체자료.txt',
#                  sep='\t', encoding='cp949')
# print(df)

# df = pd.read_excel('KIKcd_B.20180122.xlsx')
# print(df)
df = pd.read_csv('국토교통부_전국 법정동_20221031.csv',
                 sep=',', encoding='cp949')
in_sido = '대구광역시'
in_gugun = '동구'
res = df[df['시도명']==in_sido]
# print(res)
res = res[res['시군구명'] == in_gugun]
res = res[res['읍면동명'].isnull()]
code = str(res['법정동코드'].values[0])[:5]
page = 1
numRow = 10
year = 202005

baseURL = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
param = '?serviceKey=NMEoUhvnwRKfms6GyYCguKH9EylZibVsxnK91C%2B1iwyLQNnN%2Bj41aKFDl%2F2%2BGFMIHtlNQf6N4eVMIuLXmrFKBg%3D%3D'
param += f'&pageNo={page}&numOfRows={numRow}'
param += f'&LAWD_CD={code}&DEAL_YMD={year}'
URL = baseURL + param
print(URL)
resxml = urlopen(URL)
res_data = resxml.read()
soup = BeautifulSoup(res_data, 'lxml-xml')
#print(soup)
items = soup.findAll('item')
itemList = []
for te in items:
    price = te.find('거래금액').text.strip()
    price = price.replace(',', '')
    price = (int(price))
    # price = format(price, ',')
    build_year = te.find('건축년도').text
    apt_name = te.find('아파트').text
    width = float(te.find('전용면적').text)
    floor = te.find('층').text
    print('거래금액:', price)
    print('건축년도:', build_year)
    print('아파트명:', apt_name)
    print('전용면적:', width)
    kor_width = round(float(width)/3.3)
    print('평수:', kor_width, '평')
    print('층수:', floor)
    dic = {'price':price, 'build_y':build_year,
           'apt_name':apt_name, 'apt_width':width,
           'ko_width':int(kor_width), 'floor':floor}
    itemList.append(dic)
    print('==================================')

korean_font()
df = pd.DataFrame.from_dict(itemList)
df.index = df.apt_name
df = df.loc[:, ['price', 'build_y', 'apt_width', 'ko_width', 'floor']]
data_y1 = df.loc[:, 'price']
x1 = data_y1.index
y1 = data_y1
data_y2 = df.loc[:, 'apt_width']
x2 = data_y2.index
y2 = data_y2
fig, ax = plt.subplots()

#================= 1번째 데이터 시각화 =================#
# 선 그래프 시각화 옵션 | color: 선 색깔, linewidth: 선 굵기, marker 선택
line1 = ax.plot(y1, 'o-', label='가격(만원)',
                color='blue', linewidth=1)
# 값 출력
for i, v in enumerate(x1):
    # plt.text(x축 데이터, y 축 데이터, 문자열)
    plt.text(v, y1[i], str(y1[i])+'만원', fontsize=10, color='blue',
             horizontalalignment='center',  # 수평
             verticalalignment='bottom',  # 수직
             rotation=15)
plt.xticks(x1, fontsize=10, rotation=15)  # 인덱스로 세팅
plt.yticks(fontsize=10)
plt.xlabel('아파트명', fontsize=10)
plt.ylabel('가격(만원)', fontsize=10)

#================= 2번째 데이터 시각화 =================#
ax2 = ax.twinx()  # twinx() 두 겹으로 하기위해
line2 = ax2.plot(y2, '.--', label='평형',
                 color='r', linewidth=1)
for i, v in enumerate(x2):
    if y2[i] > 90.0:
        plt.text(v, y2[i]-5, str(round(y2[i]))+'평', fontsize=10,
                 color='red', horizontalalignment='center',
                 verticalalignment='bottom', rotation=15)
    else:
        plt.text(v, y2[i]+5, str(round(y2[i]))+'평', fontsize=10,
                 color='red', horizontalalignment='center',
                 verticalalignment='bottom', rotation=15)

plt.yticks(fontsize=10)
plt.ylabel('평형', fontsize=10)
plt.title('2020년 5월 아파트 매매', fontsize=10) # 그래프 제목

# 범례 표시
lines = line1 + line2
labels = [line.get_label() for line in lines]
ax.legend(lines, labels, loc=1,  fontsize=10)
ax.grid()
plt.show()