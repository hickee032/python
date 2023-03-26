import json
import re
import urllib.parse
import urllib.request
from itertools import chain

import pandas as pd

search = '한파'
category = 'news'
display = 20
start = 1
sort = 'sim'

baseURL = 'https://openapi.naver.com/v1/search/'
node = f'{category}.json'
param = f'?query={urllib.parse.quote(search)}'
param += f'&display={display}'
param += f'&start={start}'
param += f'&sort={sort}'
URL = baseURL + node + param
request = urllib.request.Request(URL)
request.add_header('X-Naver-Client-Id', 'bwvcfH0XTJPsuWGdKnjW')
request.add_header('X-Naver-Client-Secret', 'b5BbKw3Owy')
try:
    response = urllib.request.urlopen(request)
    if response.getcode() == 200: # success code
        ret_data = response.read().decode('utf-8')
except Exception as ex:
    print('서버 요청 에러')

#print(ret_data)
ret_data = re.sub("\\\\|<b>|<\\\\/b>|&apos;|&quot;", "", ret_data)
data_dic = json.loads(ret_data)
df = pd.DataFrame.from_dict(data_dic['items'])
print(df.info())
writer = pd.ExcelWriter('json_excel.xlsx',
                           engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.close()