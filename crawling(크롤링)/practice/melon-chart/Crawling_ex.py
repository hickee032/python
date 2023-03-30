import pandas as pd
import requests as requests
from bs4 import BeautifulSoup
import re

import cx_Oracle as db

URL = 'https://www.melon.com/chart/day/index.htm?classCd=GN1000'
res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = res.text

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

song_list = []
sing_list = []
album_list = []

chart_dic = {}


for sing in soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a'):
    sing_list.append(sing.text)
for sing in soup.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a'):
    sing_list.append(sing.text)

for song in soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'):
    song_list.append(song.text)
for song in soup.select('#lst100 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a'):
    song_list.append(song.text)

for album in soup.select('#lst50 > td:nth-child(7) > div > div > div.ellipsis.rank03 > a'):
    album_list.append(album.text)
for album in soup.select('#lst100 > td:nth-child(7) > div > div > div.ellipsis.rank03 > a'):
    album_list.append(album.text)

numlist = []
for i in range(100):
    numlist.append(i+1)

print(numlist)

# 3개의 리스트를 하나의 딕셔너리로
chart_dic = dict(zip(numlist, zip(sing_list, zip(song_list, album_list))))
#chart_dic = dict(zip(sing_list, song_list))

# for item in chart_dic.items():
#     print(f' \033[95m{item} ')

# print(f'\033[95m{chart_dic.keys()}')
# print(f'\033[95m{chart_dic.values()}')

for key, val in chart_dic.items():
    print(f'\033[95m{key} \033[93m{val[0]} \033[95m{val[1][0]} \033[93m{val[1][1]}')

# print(pd.DataFrame(chart_dic))





