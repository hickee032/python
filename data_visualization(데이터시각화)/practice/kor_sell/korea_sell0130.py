from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

# df = pd.read_csv('법정동코드 전체자료.txt',
#                  sep='\t', encoding='cp949')
# print(df)

# df = pd.read_excel('KIKcd_B.20180122.xlsx')
# print(df)
df = pd.read_csv('국토교통부_전국 법정동_20221031.csv', sep=',', encoding='cp949')
in_sido = '대구광역시'
in_gugun = '동구'
res = df[df['시도명']==in_sido]
# print(res)
res = res[res['시군구명'] == in_gugun]
res = res[res['읍면동명'].isnull()]
code = str(res['법정동코드'].values[0])[:5]
page = 1
numRow = 10
year = 201804

baseURL = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
param = '?serviceKey=uCZZRB7y5CHHFkZGubwB3El38Ne0AsC9gphmZVxmFE2kd07GhyWMpU4ZIakuX5gzppdBDMHC5v5s8T23KFFZqQ%3D%3D'
param += f'&pageNo={page}&numOfRows={numRow}'
param += f'&LAWD_CD={code}&DEAL_YMD={year}'
URL = baseURL + param
print(URL)
resxml = urlopen(URL)
res_data = resxml.read()
soup = BeautifulSoup(res_data, 'lxml-xml')
#print(soup)
items = soup.findAll('item')
for te in items:
    price = te.find('거래금액').text.strip()
    build_year = te.find('건축년도').text
    apt_name = te.find('아파트').text
    width = te.find('전용면적').text
    floor = te.find('층').text
    print('거래금액:', price, '만원')
    print('건축년도:', build_year)
    print('아파트명:', apt_name)
    print('전용면적:', width)
    print('층수:', floor)
    print('==================================')


