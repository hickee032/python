import pandas as pd
import requests


# setting
def set_url(url_addr):
    url = url_addr
    dataf = pd.read_html(url)[0]
    dataf = dataf.loc[:, '회사명':'종목코드']
    dataf['종목코드'] = dataf.종목코드.map('{:06d}'.format)
    return dataf


# 회사명으로 코드 구하기
def cp_getcode(dataframe, companyname):
    idx = dataframe.index[df['회사명'] == companyname][0]
    code = dataframe.iloc[idx, 1]
    return code


# 코드로 주식 정보 가져오기
def name_getvalue(code):
    header = {'User-agent': 'Mozilla/5.0'}
    df_url = pd.DataFrame([])
    for num in range(1, 10):
        url = f'http://finance.naver.com/item/sise_day.nhn?code={code}&page={num}'
        result = pd.read_html(requests.get(url, headers=header).text)[0]
        result = result.dropna()
        df_url = pd.concat([df_url, result], ignore_index=True)
    return df_url


if __name__ == '__main__':

    df = set_url('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')
    company_name = input('회사명을 입력하세요')
    try:
        ccode = cp_getcode(df, company_name)
        dfurl = name_getvalue(ccode)
        print(dfurl)
    except IndexError:
        print('회사 정보가 없습니다.')
