import pandas as pd
import requests

URL = 'http://kind.krx.co.kr/corpgeneral/corpList.do?' \
      'method=download&searchType=13'
# pd.set_option('display.max_columns', None)
df = pd.read_html(URL)[0]
# print(df.head());
# print(df.tail())
#print(df.info())
#print(df.describe())
#print(df['종목코드'].map('{:06d}'.format))
df = df[['회사명', '종목코드']]
df['종목코드'] = df['종목코드'].map('{:06d}'.format)
#print(df)

code_name = '삼성전자'
idx = df.index[df['회사명'] == 'DSR'][0]
idx = df.index[df['회사명'] == code_name].tolist()[0]
code = df.iloc[idx, 1]
header = {'User-agent':'Mozilla/5.0'}
url = f'http://finance.naver.com/item/sise_day.nhn?code={code}'
print(url)
df_url = pd.read_html(requests.get(url, headers=header).text)[0]
df_url = df_url.dropna()
print(df_url)

# NaN
# print(df_url.isnull().sum().sum())
# print(df_url.dropna())  # 모든 결측치 제거
# print(df_url.fillna(0)) # 모든 결측치 0으로 대체
# tmp_df = df_url.fillna({'종가':df_url['종가'].mean()}, inplace=False)
# print(tmp_df)
# 보간법 : linear(등간격), pad(기존값)
# print(df_url.interpolate()) # 디폴트 linear
# print(df_url.interpolate(method='pad'))








