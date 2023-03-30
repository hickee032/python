import pandas as pd
import requests

# 회사의 회사명 종목코드를 통해서 네이버 주식정보 크롤링
URL = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13'

# df = pd.read_html(URL)  # -> list
# print(df)  # -> 맨 앞에 '[' 가 붙어 있다 -> list -> type() 으로 확인
# 아래와 같이 사용 가능
df = pd.read_html(URL)[0]  # -> DataFrame
print(df)
print(type(df))
pd.set_option('display.max_columns', None)  # -> 모든 컬럼으로 보는 옵션

print(df.head())  # head() -> 상위 5개
print(df.tail())  # tail() -> 하위 5개  컬럼이 길면 ... 보여질수 있다

print(df.info())  # info() -> 컬럼 정보 -> 컬럼이 길면 ... 보여질수 있다 -> 확인을 위해
# non-null 결측치
print(df.describe())  # 전체적인 요약 -> 평균(mean), 표준편차(std) 등등..

df = df.loc[:, '회사명':'종목코드']
# df = df[['회사명','종목코드']]
df['종목코드'] = df.종목코드.map('{:06d}'.format)  # 코드를 6자리 맞추기 앞에 0을 붙이기
print(df)

code_name = '삼성전자'
# 회사명으로 종목코드 만 추출
print(df[df['회사명'] == 'GS'].loc[:, '종목코드'])
print(df[df['회사명'] == code_name].loc[:, '종목코드'])

# 회사명으로 인덱스 추출
idx = df.index[df['회사명'] == code_name][0]
# print(idx)code
idx1 = df.index[df['회사명'] == code_name].tolist()[0]
# print(idx1)

# 인덱스로 코드번호 추출
code = df.iloc[idx, 1]  # -> iloc 행렬 인덱스
# print(code)

header = {'User-agent': 'Mozilla/5.0'}
dfurl = pd.DataFrame([])
url = f'http://finance.naver.com/item/sise_day.nhn?code={code}'
df_url = pd.read_html(requests.get(url, headers=header).text)[0].dropna()  # -> 리스트에 첫번쨰 요소를 가져온다
df_url = df_url.dropna()


# df_url = pd.read_html(requests.get(url, headers=header).text)  # -> 리스트에 첫번쨰 요소를 가져온다
# print(df_url[0])
# print(type(df_url))

######################################################################################################################

# NaN 결측치 -> 처리방법에 따라 데이터가 차이가 날수도 있다
# 결측치 데이터 처리는 원시 데이터( 원본 데이터 )를 확인하고 제거 할지 안할지 결정 -> 필요한 경우도 있다

# NaN 결측치를 확인
print(df_url.isnull())  # 있으면 True -> 확인하기 어려움
print(df_url.isnull().sum())  # 칼럼 마다 NaN 카운트
print(df_url.isnull().sum().sum())  # 데이터에서 모든 NaN 개수

# NaN (결측치) 제거 할 경우
print(df_url.dropna())  # dropna() -> NaN (결측치) 제거

# NaN (결측치) 다른 값으로 대체하는 경우
# 모든 NaN을 0으로 대체
print(df_url.fillna(0))

# 모든 NaN을 평균치 로 대체
tmp_df = df_url.fillna({'종가': df_url['종가'].mean()}, inplace=False)
print(tmp_df)

# 보간법 linear ( 등간격 -> 1,2,NaN,4 -> NaN 에 4가 들어감 ) , pad ( 기존값 )
print(df_url.interpolate())  # lenear
print(df_url.interpolate(method='pad'))  # pad
