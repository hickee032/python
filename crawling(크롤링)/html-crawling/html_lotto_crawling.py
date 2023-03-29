import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://dhlottery.co.kr/gameResult.do?method=byWin&wiselog=H_C_1_1'
driver.get(url)
html = driver.page_source
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
# print(type(soup.select('#article > div:nth-child(2) > div > div.win_result > h4 > strong')))
print(soup.select('#article > div:nth-child(2) > div > div.win_result > h4 > strong')[0].text)

last_lotto_no = soup.select('#article > div:nth-child(2) > div > div.win_result > h4 > strong')[0].text[0:-1]
print('최근 로또 회차 : ', last_lotto_no)

total_sell = soup.select('#article > div:nth-child(2) > div > ul > li:nth-child(2) > strong')[0].text
print('총 판매 금액 : ', total_sell)
# #article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(1)

infos = soup.select('table.tbl_data > tbody > tr')
# td:nth-of-type(1) ~ td:nth-of-type(n)
for info in infos:
    print('순위 : ', info.select('td:nth-of-type(1)')[0].get_text().strip())
    print('총 당첨금액 : ', info.select('td:nth-of-type(2)')[0].get_text().strip())
    print('당첨자 수 : ', info.select('td:nth-of-type(3)')[0].get_text().strip())
    print('당첨 금액 : ', info.select('td:nth-of-type(4)')[0].get_text().strip())
    print('---------------------------------------------')

lotto_rlist = []
lotto_dic = {}
t_list = []

sel_data = driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/div[2]/p').text
# print(sel_data[1:-1])
# print(type(sel_data))

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

    lotto_dic1 = {rank: [total_money, manypeople, people_money]}
    t_dic1 = [sel_data, {last_lotto_no: {rank: [total_money, manypeople, people_money]}}]

    lotto_dic.update(lotto_dic1)
    t_list.append(t_dic1)

kind_pple = soup.select('#article > div:nth-child(2) > div > table > tbody > tr:nth-child(1) > td:nth-child(6)')[
    0].get_text().replace(' ', '').replace('\n', '').replace('\t', '').replace('1등', '')
lotto_type_dic = {last_lotto_no, kind_pple}

# print(lotto_dic.keys())
# print(lotto_dic)
print(t_list)

df = pd.DataFrame(t_list)
print(df)

# for key, values in lotto_dic.items():
#     print('순위 : ', key)
#     print('총 당첨금액 : ', values[0])
#     print('당첨자 수 : ', values[1])
#     print('당첨금액 :', values[2])
#     if key == '1':
#         print('당첨 유형 : ', kind_pple)

# print(lotto_dic)

driver.close()
