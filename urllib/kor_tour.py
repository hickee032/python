import json
import urllib.request
from urllib.parse import quote
from matplotlib import pyplot as plt
import pandas as pd
from pandas import DataFrame

import tour_data as td


# item = 20
# page_no = 1


def ym_input():
    local = select_local()

    year = int(input('검색할 년도를 입력하세요 : '))
    start_month = input('검색을 시작 할 달을 입력하세요 : ').zfill(2)
    end_month = input('검색을 종료 할 달을 입력하세요 : ').zfill(2)
    start_ym = f'{year}{str(start_month).zfill(2)}'
    end_ym = f'{year}{str(end_month).zfill(2)}'
    return start_ym, end_ym, local


def select_local():
    selectlocal = ''
    print('검색 지역을 선택하세요')
    print('1. 서울특별시')
    print('2. 인천광역시')
    print('3. 대구광역시')
    print('4. 부산광역시')
    select_no = int(input('번호 선택 : '))

    if select_no == 1:
        selectlocal = '서울특별시'
    elif select_no == 2:
        selectlocal = '인천광역시'
    elif select_no == 3:
        selectlocal = '대구광역시'
    elif select_no == 4:
        selectlocal = '부산광역시'

    return selectlocal


if __name__ == '__main__':
    startym, endym, sido = ym_input()
    print('시작 년월 -', int(startym))
    print('종료 년월 -', int(endym)+1)
    print('시도 - ', sido)
    urllist = []
    for i in range(int(startym), int(endym)+1):
        urllist.append(td.url_setting_page_non(i, sido))

    datalist = []
    for j in urllist:
        td.get_tour_data(datalist, j)

    data_dict = {}
    for dl in datalist:
        data_dict = json.loads(dl)
        print(data_dict)
