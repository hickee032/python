import pandas as pd  # 데이터 분석 라이브러리
from matplotlib import pyplot as plt  # 데이터 시각화 라이브러리
from pandas import DataFrame


# 한글 이슈가 있음
def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False  # 부호를 맞춰준다


# scala(스칼라) : 상수
# vector : 1 차원
# matrix : 2 차원
# tensor ; n 차원 ( 3차원 이상 )
# Serise : vector
# DataFrame : matrix
'''
def serise_pa():
    # 2015년 도시별 인구
    s = pd.Series([9904312, 3448737, 2890451, 2466052],
                  index=['서울', '부산', '인천', '대구'])
    print('pandas series')
    print(s)
    print(s.values)  # series의 순수한 값
    print('벡터화 연산 : ', s / 10000)
    print(f's[1] : {s[1]},s["부산"]:{s["부산"]}')  # 인덱스로도 접근할수 있고 컬럼명으로도 접근할 수 있다
    s_idx = s[[0, 3, 1]]  # 부분 indexing
    print(s_idx)
    s_idx2 = s[['서울', '대구']]  # 인덱스 대신 여러개의 컬럼으로 출력
    # Series 는 1차원 형태인데 2차원 배열의 형태 (?) 
    # -> 서울 대구 의 인덱스의 데이터를 가져와 s에 저장한다 하는 뜻으로 해석
    
    print(s_idx2)

    # slicing -> end index는 포함이 안된다는 것을 기억 
    # print(s[1:3])  # 부산 인천 만 출력
    # print(s[1:-1])  # 부산 인천 만 출력
    # print(s[::-1])  # 역순으로 출력
    # print(s[::3])

    # 객체처럼 접근  .  으로 접근
    # print(f'대구 : {s.대구} 부산 : {s.부산}')

    # 검색
    print('서울 검색 : ', '서울' in s)  # 존재하면 True
    print('런던 검색 : ', '런던' in s)  # 없으면 False

    # 딕셔너리처럼 사용도 가능하다
    for k, v in s.items():
        print(f'key : {k} value : {v}')


'''

#########################################################################################################
'''
# 행과 컬럼이 존재하는 2차원 배열과 흡사 하다
def frame_pd():
    # 딕셔너리 ( 키 : 값 ) -> 2015 컬럼 , [ ] : 데이터
    data = {'2015': [9904312, 3448737, 2890451, 2466052],
            '2016': [9914312, 3548737, 2790451, 2366052],
            '2017': [9924312, 3648737, 2690451, 2266052],
            '2018': [9934312, 3748737, 2590451, 2166052],
            '지역': ['서울', '부산', '인천', '대구'],
            '2015~2018 증가율': [0.025, 0.016, 0.09, 0.014]
            }
    # 인덱스 추가 -> 인덱스를 자동으로 지정하지 않을 경우 자동으로 설정된다
    index = ['수도권', '경남', '경기', '경북']
    df = pd.DataFrame(data, index=index)
    # print(type(df))
    # print(df.values)  # 인덱스는 순수 데이터에 포함하지 않는다

    # 데이터를 바꾸기
    df['2015~2018 증가율'] = df['2015~2018 증가율'] * 100
    # print(df)

    df['2017~2018 증가율'] = ((df['2018'] - df['2017']) / df['2017'] * 100).round(2)
    # print(df)

    # print(df['지역'])  # DataFrame에서 [ ] 로 특정 컬럼을 가져오게된다면 타입이 series가 된다
    # print(type(df['지역']))  # 출력 형태 가 4행 2열 배열의 형태이지만 타입은 Series (1차원 형태) 이다

    # print(df[['지역']])  # [[]]로 추출하게되면 타입이 DataFrame가 된다
    # print(type(df[['지역']]))  # 컬럼명이 추가 된다 -> series는 컬럼명이 없다

    # loc : 컬럼명
    # iloc : index
    print(df.loc['수도권'])
    print(df.loc['수도권'].values)
    print(df.iloc[0].values)

    # 특정값을 바꿈
    print(df.loc['수도권']['2018'])
    df.loc['수도권', '2018'] = 1111  # 인덱스 명 컬럼 명

    # df.iloc-

    print(df.loc['수도권']['2018'])

    # 전치 행렬
    print(df.T)  # 행과 열을 뒤집는 다 


def serise_pa2():
    # 2015년 도시별 인구
    s = pd.Series([9904312, 3448737, 2890451, 2466052])
    print('pandas series')
    print(s)

'''


def frame_ex1():
    # 4명 (춘향 몽룡 향단 방자) 의 국어, 영어, 수학
    # 점수를 임의로 설정

    data = {
        '국어': [90, 87, 85, 70],
        '영어': [81, 90, 56, 84],
        '수학': [79, 89, 67, 96]
    }
    index = ['춘향', '몽룡', '향단', '방자']
    df = pd.DataFrame(data, index=index)
    print(df)

    # 모든 학생의 수학 점수 출력
    # for i in range(len(df)):
    #     print(f'{df.index[i]} - 수학점수 : {df["수학"][i]}')

    print(df['수학'].values)
    print(type(df['수학'].values))  # numpy.ndarray

    print(df['수학'])
    print(type(df['수학']))  # -> Series

    print(df[['수학']])
    print(type(df[['수학']]))  # -> DataFrame

    # 모든 학생의 국어, 영어 점수 출력
    # for i in range(len(df)):
    #     print(f'{df.index[i]} - 국어 점수 : {df["국어"][i]}, 영어 점수 : {df["영어"][i]}')

    print(df[['국어', '영어']])

    # 평균 점수를 새로운 칼럼으로 추가
    df['평균'] = df.mean(axis=1).round(2)

    # 주의
    # 행 우선  axis=0 # 동작으로 생각
    # 열 우선 axis=1

    print(df)
    # 방자의 영어 점수 80점으로 수정 평균 점수 새로 출력
    # pd.set_option('mode.chained_assignment', None)  # <==== 경고를 끈다
    # df["영어"][3] = 90
    df.loc['방자', '영어'] = 90

    df['평균'] = df.mean(axis=1)
    print(df.round(2))

    df.iloc[3, 1] = 99
    df['평균'] = df.mean(axis=1).round(1)
    print(df.round(2))

    print(df.mean(axis=0))
    # s = pd.Series(df.mean(axis=0).round(2))
    # print(s)

    # 춘향 몽룡까지 국 영 수 점수 데이터 타입 출력
    print(df[1:3])
    print(type(df[1:3]))

    print(df[:'몽룡'])
    print(df['춘향':'몽룡'])  # end 포함

    # 춘향 점수 series 및 데이터 타입 출력
    print(df.loc['춘향'])
    print(type(df.loc['춘향']))

    # 방자의 모든 과목 점수
    print(df.loc['방자'].round(1))
    print(df.loc[['방자']].round(1))

    # df = pd.DataFrame(data, index=df.sum(axis=1).round(1))

    ssum = pd.Series(df.sum(axis=0).round(1))
    savg = pd.Series(df.mean(axis=0).round(1))
    print(ssum)
    print(type(ssum))
    df.loc['과목 총합'] = ssum
    df.loc['과목 평균'] = savg
    df['점수 총합'] = df['국어'] + df['영어'] + df['수학']
    print(df)


# 슬라이싱
def frame_ex2():
    dic = {'a': [1, 2, 3, 4], 'b': [4, 5, 6, 7], 'c': ['a', 'b', 'c', 'd']}
    df = pd.DataFrame(dic)
    '''
    print(df.c)
    print(type(df.c))
    print(df['c'])
    print(type(df['c']))

    print(df.loc[:, 'a'])  # A 컬럼
    print(df.loc[:, 'a':'b'])  # A ~ B 컬럼
    print(df.loc[:, 'a':])  # A ~ 끝
    print(df.iloc[:, 1:3])  # B ~ C

    print(df.iloc[:2, 1:3])  # 전체가 아닌 중간 까지
    '''

    # b 컬럼만 ( 한 컬럼 만)
    """
    print(df.b)
    print(type(df.b))  # -> Series
    
    print(df.loc[:, 'b'])
    print(type(df.loc[:, 'b']))  # -> Series
    
    print(df[['b']])
    print(type(df[['b']]))  # -> DataFrame

    print(df['b'])
    print(type(df['b']))  # -> Series

    print(df.iloc[:, 1])
    print(type(df.iloc[:, 1])) # -> Series
    """
    # a ~ b
    """
    print(df.loc[:, 'a':'b'])
    print(type(df.loc[:, 'a':'b']))  # -> DataFrame

    print(df[['a', 'b']])
    print(type(df[['a', 'b']]))  # -> DataFrame
    
    print(df.loc[:, ['a', 'b']])
    print(type(df.loc[:, ['a', 'b']]))  # -> DataFrame

    print(df.iloc[:, [0, 1]])
    print(type(df.iloc[:, [0, 1]]))  # -> DataFrame
    
    print(df.iloc[:, :2])
    print(type(df.iloc[:, :2]))  # -> DataFrame
    """
    # row 0~1 col a c  -> 부분 추출
    """
    print(df.loc[:1, ['a', 'c']])
    print(df.iloc[[0, 1], [0, 2]])
    print(df.iloc[:2, ::2])
    print(df.iloc[:2, 0:3:2])
    """
    import numpy as np
    # C 컬럼에서 A 와 같은 행 정보 출력
    print(df[df['c'] == 'a'])
    # numpy
    print(df.iloc[np.where(df['c'] == 'a')])

    # C 컬럼에서 A 와 같은 행 정보 출력하되 컬럼 A정보만 출력
    print(df.iloc[np.where(df['c'] == 'a')].loc[:, 'a'])
    print(df[df['c'] == 'a'].loc[:, 'a'])

    # C 컬럼에서 A와 같은 정보를 출력 컬럼 a,b 정보만 출력
    #print(df.iloc[np.where(df['c'] == 'a')].iloc[:, 0:2])
    # C 컬럼에서 A와 같은 정보를 출력 컬럼 a,c 정보만 출력
    #print(df.iloc[np.where(df['c'] == 'a')].loc[:, ['a', 'c']])


if __name__ == '__main__':
    # serise_pa()
    # serise_pa2()  # 인덱스 자동으로 0번부터 시작
    # frame_pd()
    # frame_ex1()
    frame_ex2()
