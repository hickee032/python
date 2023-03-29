import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from matplotlib import pyplot as plt
from pandas import DataFrame
import json
import urllib.request
from urllib.parse import quote


def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False


def excel_writer(file_name, dic):
    file_name += '.xlsx'
    korean_font()
    df = DataFrame.from_dict(dic)
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1')
    writer.close()

def json_write(file_name, dic):
    file_name += '.json'
    try:
        with open(file_name, 'w', encoding='utf-8') as json_file:
            ret = json.dumps(dic, indent=4, sort_keys=False, ensure_ascii=False)
            json_file.write(ret)
            print(f'{file_name} 저장됨')
    except Exception as exc:
        print('파일 저장 에러 :', exc)


if __name__ == '__main__':

    driver = webdriver.Chrome()
    url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=H_C_1_1'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 회차
    turn_num = soup.select('#article > div:nth-child(2) > div > div.win_result > h4 > strong')[0].text
    # print(turn_num)
    sel_date = driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/div[2]/p').text[1:-1]
    # print(sel_date)

    lottery_list = [
        driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/div[2]/div/div[1]/p').text.replace('\n', ','),
        driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/div[2]/div/div[2]/p/span').text]
    # print('당첨 번호 :', lottery_list[0], '보너스 번호 ', lottery_list[1])

    total_sell = soup.select('#article > div:nth-child(2) > div > ul > li:nth-child(2) > strong')[0].text
    # print('총 판매 금액 : ', total_sell)

    lotto_dic = {}
    lotto_list = []
    for i in range(1, 6):
        rank = soup.select(f'#article > div:nth-child(2) > div > table > tbody > tr:nth-child({i}) > td:nth-child(1)')[
                   0].get_text()[:-1].replace(',', '')
        total_money = \
            soup.select(f'#article > div:nth-child(2) > div > table > tbody > tr:nth-child({i}) > td:nth-child(2)')[
                0].get_text()[:-1].replace(',', '')
        manypeople = \
            soup.select(f'#article > div:nth-child(2) > div > table > tbody > tr:nth-child({i}) > td:nth-child(3)')[
                0].get_text()[:-1].replace(',', '')
        people_money = \
            soup.select(f'#article > div:nth-child(2) > div > table > tbody > tr:nth-child({i}) > td:nth-child(4)')[
                0].get_text()[:-1].replace(',', '')

        dic_temp = {rank: {'총액' : total_money, '당첨자수' : manypeople, '인당 ' :  people_money}}
        list_temp = [rank, total_money, manypeople, people_money]
        lotto_dic.update(dic_temp)
        lotto_list.append(list_temp)

    # print(lotto_list)
    print(lotto_dic)

    kind_pple = soup.select('#article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(6)')[
        0].get_text().replace(' ', '').replace('\n', '').replace('\t', '').replace('1등', '')

    # print(kind_pple)

    # dict_res = {
    #     turn_num: [sel_date, lottery_list[0], lottery_list[1], total_sell, lotto_list[0], lotto_list[1], lotto_list[2], lotto_list[3], kind_pple]}

    # dict_res = {
    #     turn_num: [sel_date, lottery_list[0], lottery_list[1], total_sell,
    #                lotto_dic,
    #                kind_pple]}

    dict_res = {
        turn_num: {'date': sel_date, 'number': lottery_list, 'total_money':  total_sell,
                   '당첨 현황': lotto_dic, '비고': kind_pple}}

    print(dict_res)
    # index = ['날짜', '당첨번호', '보너스 번호', '총 판매금액', '1등 총 당첨액',  '1등 당첨자 수',  '1등 당첨액', '비고']
    # df = pd.DataFrame(dict_res, index=index)
    # df = pd.DataFrame(dict_res)


    json_write('lotto', dict_res)