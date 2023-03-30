import json
import urllib.request
from urllib.parse import quote
from matplotlib import pyplot as plt
import pandas as pd
from pandas import DataFrame


# Json파일로 쓰기
def json_write(file_name, dic):
    try:
        with open(file_name, 'w', encoding='utf-8') as json_file_write:
            ret = json.dumps(dic, indent=4, sort_keys=False, ensure_ascii=False)
            json_file_write.write(ret)
            print(f'{file_name} 저장됨')
    except Exception as exc:
        print('파일 저장 에러 :', exc)


# Json파일 읽어오기
def json_read(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as json_file_read:
            res_dic = json.load(json_file_read)
            # -> json파일을 확인 태그
            res_list = res_dic['response']['body']['items']['item']
            for i in res_list:
                print('관광지', i["resNm"])
                print('위치', i["gungu"])
                print('내국인 관광객수', i["csMvCnt"])
                # print('외국인 관광객수', i["csForCnt"])
                print('---------------------------------')
            return res_list
    except Exception as exc:
        print('파일 읽기 오류', exc)


def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False  # 부호를 맞춰준다


# xlsx 저장
def excel_writer(file_name, dic):
    file_name += '.xlsx'
    korean_font()
    df = DataFrame.from_dict(dic)
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1')
    writer.close()  # 닫아줘야한다


year = 2022
month = 11
ym = f'{year}{str(month).zfill(2)}'
sido = '대구광역시'
gungu = ''
items = 39
pageno = 1

print(ym)

service_key = 'NMEoUhvnwRKfms6GyYCguKH9EylZibVsxnK91C%2B1iwyLQNnN%2Bj41aKFDl%2F2%2BGFMIHtlNQf6N4eVMIuLXmrFKBg%3D%3D'
# End Point가 아니라 상세설명 -> 서비스URL
service_url = 'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList'

# 요청변수 설정 Request Parameter
# &YM=201201&SIDO=부산광역시&GUNGU=해운대구&RES_NM=부산시립미술관
Parameter = f'?_type=json&serviceKey={service_key}'
Parameter += f'&YM={ym}&SIDO={quote(sido)}'
Parameter += f'&numOfRows={items}'
Parameter += f'&pageNo={pageno}'

# url에 한글이 들어갈 경우 from urllib.parse import quote
# ascii' codec can't encode characters in position 213-217: ordinal not in range(128) 방지

url = service_url + Parameter
print(url)

request = urllib.request.Request(url)
responce = urllib.request.urlopen(request)
try:
    if responce.getcode() == 200:
        ret_data = responce.read().decode('utf-8')
except Exceptionas as ex:
    print('HTTP에러', ex)

# print(type(ret_data))  # -> 문자열 string
dic_data = json.loads(ret_data)
# print(type(dic_data))  # -> json.loads 딕셔너리
print(dic_data)

# 찾아 들어가기
print(dic_data['response']['header']['resultMsg'])

json_write(f'{sido}_{gungu}_관광지.json', dic_data)

alist = json_read(f'{sido}_{gungu}_관광지.json')
print(alist)
# excel_writer(f'{sido}_{gungu}_관광지', alist)
# print('alist 타입', type(alist))

'''
df = DataFrame(alist)
writer = pd.ExcelWriter('pandas_wlsx_chart.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='sheet1')
workbook = writer.book
worksheet = writer.sheets['sheet1']
# chart 객체 생성
chart = workbook.add_chart({'type': 'column'})
# chart 에 출력할 데이터 선택
chart.add_series({'name': '전체 관광객', 'categories': '=sheet1!$G$2:$G$8', 'values': '=sheet1!$D$2:$D$8'})
chart.add_series({'name': '내국인 관광객', 'categories': '=sheet1!$D$1:$D$1', 'values': '=sheet1!$E$2:$E$8'})
# 특정 위치에 chart 추가
worksheet.insert_chart('B9', chart)
# 리소스 해제
writer.close()
'''
# def xml_writer2():
#     df = DataFrame({'온도': [20.2, 22.3, 26.5, 30.3]})
#     writer = pd.ExcelWriter('pandas_wlsx_chart.xlsx', engine='xlsxwriter')
#     df.to_excel(writer, sheet_name='sheet1')
#     workbook = writer.book
#     worksheet = writer.sheets['sheet1']
#     # chart 객체 생성
#     chart = workbook.add_chart({'type': 'column'})
#     # chart 에 출력할 데이터 선택
#     chart.add_series({'values': '=sheet1!$B$2:$B$6'})
#     # 특정 위치에 chart 추가
#     worksheet.insert_chart('D2', chart)
#     # 리소스 해제
#     writer.close()
