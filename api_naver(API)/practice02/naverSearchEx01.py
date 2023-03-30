# 도서
# 요청 URL https://openapi.naver.com/v1/search/book.json
import datetime
import json
import re
import urllib.parse
import urllib.request
import pandas as pd  # 데이터 분석 라이브러리
from matplotlib import pyplot as plt  # 데이터 시각화 라이브러리
from pandas import DataFrame

Client_Id = 'SrNxTWJA3SuZSEKUsT6J'
Client_Secret = 'KJl3pu_9oO'
category = 'book'
result_dic = None


def search_book(book_in_title):
    global category
    booktitle = book_in_title
    display = 20
    startpage = 1
    sort = 'sim'

    base_url = 'https://openapi.naver.com/v1/search/'
    node = f'{category}.json'
    parameter = f'?query={urllib.parse.quote(booktitle)}'
    parameter += f'&display={display}'
    parameter += f'&start={startpage}'
    parameter += f'$sort={sort}'
    f_url = base_url + node + parameter
    return f_url


def sever_request(url):
    global Client_Id
    global Client_Secret

    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', 'SrNxTWJA3SuZSEKUsT6J')
    req.add_header('X-Naver-Client-Secret', 'KJl3pu_9oO')

    try:
        responce = urllib.request.urlopen(req)
        if responce.getcode() == 200:
            return_data = responce.read().decode('utf-8')  # return type -> str

            # return_data = re.sub("\\\\|<b>|<\\\\/b>|&apos;|&quot;", "", return_data)
            return_data = re.sub("\\\\n|\\\\", "", return_data)
            print(return_data)
            return return_data

    except Exception as ex:
        print(f'[{datetime.datetime.now()}] 서버요청 에러 : {url}')
        print(f'에러 코드 {ex}')
        return None


def json_searchfile(search_name, result_data):
    global category
    filename = f'{category}_{search_name}.json'
    try:
        with open(filename, 'w', encoding='utf-8') as write_fs:
            write_fs.write(result_data)
    except Exception as ex:
        print(f'[{datetime.datetime.now()}] 파일 쓰기 에러 : {ex}')


def json_readfile(search_name):
    global category
    global result_dic
    filename = f'{category}_{search_name}.json'
    print(filename)
    try:
        with open(filename, 'r', encoding='utf-8') as read_fs:
            result_dic = json.load(read_fs)
            result_list = result_dic["items"]
            for i in result_list:
                print('제목 :', i["title"])
                print('이미지 :', i["image"])
                print('작가 :', i["author"])
                print('출판사 :', i["publisher"])
                print('링크 :', i["link"])
                print('----------------------')
                return result_dic["items"], result_list
    except Exception as ex:
        print(f'[{datetime.datetime.now()}] 파일 읽기 에러 : {ex}')


def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False  # 부호를 맞춰준다


def xml_writer(dic):
    korean_font()
    df = DataFrame.from_dict(dic)
    writer = pd.ExcelWriter('book_writer.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1')
    writer.close()  # 닫아줘야한다


def csv_writer(dic):
    df = DataFrame.from_dict(dic)
    df.to_csv('book_csv.csv', encoding='utf-8-sig')
