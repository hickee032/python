import pandas as pd # 데이터 처리
from pandas import DataFrame
from matplotlib import pyplot as plt # 시각화

def korean_font():
    # 한글 처리
    plt.rc('font', family='Malgun Gothic')
    # - 부호 오류 처리
    plt.rcParams['axes.unicode_minus'] = False

def pandas_basic():
    df = pd.read_csv('test1.csv', sep='/')
    print(df)
    ax = df.plot(kind='bar')
    ax.set_title('학생 성적표', fontsize=16)
    ax.set_xlabel('학생 이름')
    ax.set_ylabel('각과목 점수')
    plt.show()

# pandas 자료 구조
# 1.dataFrame : 2차원 배열 형태
# 2.series : 1차원 배열 형태
def serise_pan():
    # se = pd.Series([1, 2, 3, 4])
    se = pd.Series([1, 2, 3, 4],
                   index=['서울', '부산', '인천', '대구'])
    print(se)
    print('벡터화 연산:', se+100)
    print(type(se[0]))
    print(se['서울'])
    print(se[0:3]) # start:end-1
    print(se['인천':'대구']) # start:end
    print(se[2:]) # print(se[2:4])
    print(se[0:4:1]) # start:end-1:증가치
    # 서울, 대구 만 출력
    print(se[::3])
    print(se[['서울', '대구']])
    # 역순으로 출력
    print(se[::-1])

def frame_pan():
    data = {
        '2015':[11, 22, 33, 44],
        '2016':[22, 33, 44, 55],
        '2017':[33, 44, 55, 66],
        '지역':['수도권', '경상권', '전라권', '경기권'],
        '2015~2018 증가율':[0.1, 0.2, 0.3, 0.4]
    }
    index = ['서울', '대구', '전주', '수원']
    df = pd.DataFrame(data, index=index)
    # print(df['지역'].values)
    # print(df[['지역']])
    # print(df[['지역']].values)
    # print(df[['2015','2017']])

    # print(df)
    # loc:인덱스명, iloc:index
    print(df.loc['서울'])
    # print(type(df.loc[['서울']]))
    # df.loc['서울','2015'] = 110
    # print(df.loc['서울','2015'])
    # print(df.loc['서울':'대구'])
    print(df.iloc[0])
    df.iloc[0, 0] = 220
    print(df.iloc[0, 0])
    print(df.iloc[:2])

def frame_ex1():
    # << 2가지 이상의 방법이 있는지 고민하신후 연습해보기 >>
    # 4명(춘향, 몽룡, 향단, 방자)의 국,영,수 점수를
    # 딕셔너리로 설정 (index명 사용)
    data = {
        '국어': [100, 90, 80, 70],
        '영어': [90, 80, 70, 60],
        '수학': [80, 70, 60, 50]
    }
    idx = ['춘향', '몽룡', '향단', '방자']
    df = pd.DataFrame(data, index=idx)
    print(df)
    # 1. 모든 학생의 수학 점수 출력 (타입 확인)
    # 타입을 반드시 확인
    # print(df['수학'])     # series
    # print(df.수학)        # series
    # print(df[['수학']])   # dataFrame
    # print(df['수학'].values[0]) # 1차원 ndarray
    # print(df[['수학']].values[0][0]) # 2차원 ndarray

    # print(df[['국어', '수학']])
    # print(df.loc[:, '수학'])  # -> 모든 행의 수학점수 Series [] 대괄호 1개 시리즈
    # print(df.loc[:, ['수학']]) # dataFrame [[]] 대괄호 두개 데이터 프레임
    # print(df.loc['방자']) # -> 하나만 쓰면 컬럼
    # print(df.loc[['방자']]) # dataFrame
    # print(df.loc['춘향':'몽룡']) # dataFrame -> 컬럼 정보 ('춘향':'몽룡')
    # print(df.loc[:, '국어':'영어'])  # dataFrame -> 인덱스 정보 ('국어':'영어')
    # print(df.iloc[3])
    # print(df.iloc[[3]])
    # print(df.iloc[:, :-1])
    # print(df.iloc[:, [2]])
    # print(df)
    # df.loc['방자', '영어'] = 80
    # print(df)
    # df.iloc[3, 1] = 90
    # print(df)

    # --------------------------------------
    # 2. 모든 학생의 국어, 영어 점수 출력
    # print(df[['영어', '국어']])
    # --------------------------------------
    # 3. 모든 학생의 각 과목 평균 점수를 새로운 컬럼에 추가
    # axis=0:행, axis=1:열
    # print(df)
    # print(df.mean(axis=1))
    # df['평균'] = df.mean(axis=1)
    # print(df)
    # --------------------------------------
    # 4. 방자의 영어 점수를 80점으로 수정하고 평균 점수
    #    새로 계산하여 출력
    # df.loc['방자', '영어'] = 80
    # df['평균'] = df.mean(axis=1)
    # print(df.round(1))
    # --------------------------------------
    # 5. 춘향 ~ 몽룡까지 국,영,수 출력
    # print(df.loc['춘향':'몽룡', :])
    # 6. 춘향 점수 series 출력
    # print(df.loc['춘향'])
    # # 7. 방자의 모든 과목 점수 출력
    # print(df.loc['방자'])
    # print(df.loc[['방자']])
    # 8. 국,영,수 총점을 구하여 새로운 인덱스(총점)로 추가
    df.loc[:, '평균'] = df.mean(axis=1)
    print(df)
    df.loc['과목총점', :] = df.sum(axis=0)
    print(df)

if __name__ == '__main__':
    korean_font()
    # pandas_basic()
    # serise_pan()
    # frame_pan()
    frame_ex1()