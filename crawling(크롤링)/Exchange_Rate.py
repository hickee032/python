from bs4 import BeautifulSoup
import requests as requests
import pandas as pd
import urllib.request
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

# 환율 정보를 가져옴 euro
sub_url = 'https://finance.naver.com/marketindex/exchangeDetail.naver?marketindexCd=FX_EURKRW'
res = requests.get(sub_url, headers={'User-Agent': 'Mozilla/5.0'})
html = res.text
soup = BeautifulSoup(html, 'html.parser')
ex_rate_temp = soup.select('#container > div.aside > div.spot_aside > table > tbody > tr:nth-child(1) > td')[0].text \
    .replace('\n', '').replace('\t', '').replace(',', '')
ex_rate = round(float(ex_rate_temp))

url = 'https://www.transfermarkt.com/transfers/transferrekorde/statistik?saison_id=alle&land_id=0&ausrichtung' \
      '=&spielerposition_id=&altersklasse=&leihe=&w_s='
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = res.text
soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all('td', {'class': {'hauptlink': 'a'}})

date_tran = []
for i in range(1, 26):
    date_tran.append(soup.select(f'#yw2 > table > tbody > tr:nth-child({i}) > td:nth-child(3) > a')[0].text)
print(date_tran)

list_temp_name = []
list_temp_team = []
list_temp_fee = []
dict_temp = {}

num = 0
for res in result:
    if num % 3 == 0:
        list_temp_name.append(res.get_text().replace('\n', ''))
    elif num % 3 == 1:
        list_temp_team.append(res.get_text().replace('\n', ''))
    elif num % 3 == 2:
        transfer_fee = res.get_text().replace('\n', '')[1:6]
        list_temp_fee.append(round(float(transfer_fee) * ex_rate))

    num += 1

# print(list_temp_name)
# print(list_temp_team)
# print(list_temp_fee)

for j in range(len(list_temp_name)):
    print(date_tran[j] + list_temp_name[j])

#
# transfer_dic = dict(zip( zip(list_temp_team, list_temp_fee)))
#
# print(transfer_dic)
