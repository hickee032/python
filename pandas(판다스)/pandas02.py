import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame

def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

# scala:상수, vector:1차원, matrix:2차원, tensor:3차원이상
# Series: vector, dataFrame: matrix
def serise_pa():
    # 2015년도 각 도시의 인구
    s = pd.Series([9904312, 3448737, 2890451, 2466052],
                  index=['서울', '부산', '인천', '대구'])
    # s = pd.Series([9904312, 3448737, 2890451, 2466052])
    # print(s)
    # print(s.values)
    # print('벡터화 연산:', s/10000)
    # print(f's[1]:{s[1]}, s["부산"]:{s["부산"]}')
    # s_idx = s[[0, 3, 1]] # 부분 indexing
    # print(s_idx)
    # s_idx2 = s[['서울', '대구']]
    # print(type(s_idx2))

    # slicing
    # print(s[1:3])
    # print(s[1:-1])
    # print(s[::-1])
    # print(s[::3])
    
    # 객체처럼 '.'으로 접근
    print(f'대구:{s.대구} 부산:{s.부산}')
    print('서울 검색:', '서울' in s)

    for k, v in s.items():
        print(f'key:{k}, value:{v}')

def frame_pd():
    data = {
        '2015':[9904312, 3448737, 2890451, 2466052],
        '2016':[9904111, 3448111, 2890111, 2466111],
        '2017':[9904222, 3448222, 2890222, 2466222],
        '2018':[9904333, 3448333, 2890333, 2466333],
        '지역':['수도권', '경상도', '충청도', '전라도'],
        '2015~2018 증가율':[0.0283, 0.0163, 0.0982, 0.0141]
    }
    index = ['서울', '대구', '천안', '광주']
    df = pd.DataFrame(data, index=index)
    print(df)
    # print(df.values)
    df['2015~2018 증가율'] = df['2015~2018 증가율'] * 100
    #print(df)
    df['2017~2018 증가율'] = \
        ((df['2018']-df['2017']) / df['2017']*100)
    #print(df)
    print(type(df['지역'])) # series
    print(df[['지역']]) # dataFrame

    # loc:컬럼명, iloc:index
    #print(df.loc['서울'].values)
    #print(df.iloc[0])
    print(df.loc['서울']['2018'])
    df.loc['서울','2018'] = 1111
    print(df.loc['서울', '2018'])
    df.iloc[0, 3] = 2222
    # 전치행렬
    #print(df.T)

def frame_ex1():
    # 4명(춘향, 몽룡, 향단, 방자)의 국어, 영어, 수학
    # 점수를 임의로 설정
    # 1. 모든 학생의 수학 점수 출력
    # 2. 모든 학생의 국어, 영어 점수 출력
    # 3. 모든 학생의 각 과목 평균 점수를 새로운 컬럼에 추가
    # 4. 방자의 영어 점수를 80점으로 수정하고 평균 점수
    #    새로 계산하여 출력
    data = {
        '국어':[100, 90, 80, 70],
        '영어': [95, 90, 70, 60],
        '수학': [90, 80, 70, 60],
    }
    index = ['춘향', '몽룡', '향단', '방자']
    df = pd.DataFrame(data, index=index)
    print(df)
    #print('========================')
    # axis=0:row , axis=1:column
    #print(df.mean(axis=0)) # 평균

    # print(df['수학']); print(type(df.수학))
    # print(df[['수학']]); print(type(df[['수학']]))
    #print(df['수학'].values); print(type(df['수학'].values))

    #print(df[['국어', '영어']])

    # 0: 행, 1:열
    #print(df.mean(axis=0))
    # 국,영,수 총점을 구하여 새로운 인덱스로 추가
    # #
    # #df.loc['방자', '영어'] = 80
    # df.iloc[3, 1] = 99
    # df['평균'] = df.mean(axis=1)
    # print(df.round(1))

    # 5. 춘향 ~ 몽룡까지 국,영,수 출력
    # print(df[:'몽룡'])
    # print(df['춘향':'몽룡']) # end 포함
    print(df[:2]) # end - 1
    # 6. 춘향 점수 series 출력
    print(type(df.loc['춘향']))
    # 7. 방자의 모든 과목 점수 출력
    print(df.loc[['방자']])
    print(df[['국어']])
    # 8. 국,영,수 총점을 구하여 새로운 인덱스(총점)로 추가
    t_mean = df.mean(axis=0)
    t_sum = df.sum(axis=0)
    print(t_mean)
    df.loc['과목 총점'] = t_sum
    df.loc['과목 평균'] = t_mean
    print(df)

def frame_ex2():
    dic = {
        'a':[1, 2, 3, 4],
        'b':[4, 5, 6, 7],
        'c':['a', 'b', 'c', 'd']}
    df = pd.DataFrame(dic)
    print(df)
    # print(df['c']); print(type(df.c))
    # print(df.loc[:, 'a':])
    # print(df.iloc[:2, 1:3])
    # 1. b 컬럼의 데이터 출력
    # print(df.b); print(df['b']); print(df.loc[:, 'b'])
    # print(type(df.iloc[:, 1]))
    # 2. a ~ b 컬럼의 데이터 출력
    # print(df[['a', 'b']])
    # print('------------------')
    # print(df.loc[:, ['a', 'b']])
    # print('------------------')
    # print(df.iloc[:, [0, 1]])
    # print('------------------')
    # print(df.iloc[:, :2])
    # print('------------------')
    # print(df.loc[:, 'a':'b'])
    # 3. row:0~1, col:a, c 만 추출
    # print(df.loc[0:1, ['a', 'c']])
    # print('------------------')
    # print(df.iloc[[0, 1], [0, 2]])
    # print('------------------')
    # print(df.iloc[:2, ::2])

    import numpy as np
    # c컬럼에서 a와 같은 행 정보 출력
    # print(df[df['c'] == 'a'])
    # print(df.iloc[np.where(df['c'] == 'a')])
    
    # 1.c컬럼에서 a와 같은 정보행 출력하되, 컬럼 a정보만 출력
    print(df.iloc[np.where(df['c']=='a')].loc[:, 'a'])
    # 2.c컬럼에서 a와 같은 정보행 출력하되, 컬럼 a,b 출력
    print(df.iloc[np.where(df['c'] == 'a')].iloc[:, 0:2])
    # 3.c컬럼에서 a와 같은 정보행 출력하되, 컬럼 a,c 출력
    print(df.iloc[np.where(df['c'] == 'a')].loc[:, ['a','c']])

if __name__ == '__main__':
    #serise_pa()
    #frame_pd()
    #frame_ex1()
    frame_ex2()