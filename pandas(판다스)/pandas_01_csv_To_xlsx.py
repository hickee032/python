import pandas as pd  # 데이터 분석 라이브러리
from matplotlib import pyplot as plt  # 데이터 시각화 라이브러리
from pandas import DataFrame


# 한글 이슈가 있음
def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False  # 부호를 맞춰준다


def pandas_basic():
    df = pd.read_csv('../DataBaseConnect 데이터베이스 연결/test.csv', sep=',')
    print(df)
    print(type(df))  # DB등 어떤 데이터 분석에는 타입이 반드시 DataFrame 타입이어야 한다
    ax = df.plot(kind='bar')
    ax.set_title('학생성적표', fontsize=10)
    ax.set_xlabel('학생이름')
    ax.set_ylabel('각과목 점수')
    # ax.legend(loc='center')  # 범례 중앙으로
    plt.show()


'''
def xml_writer():
    df = DataFrame({'온도': [20.2, 22.3, 26.5, 30.3]})
    writer = pd.ExcelWriter('pandas_writer.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1')
    writer.close()  # 닫아줘야한다


def xml_writer2():
    df = DataFrame({'온도': [20.2, 22.3, 26.5, 30.3]})
    writer = pd.ExcelWriter('pandas_wlsx_chart.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1')
    workbook = writer.book
    worksheet = writer.sheets['sheet1']
    # chart 객체 생성
    chart = workbook.add_chart({'type': 'column'})
    # chart 에 출력할 데이터 선택
    chart.add_series({'values': '=sheet1!$B$2:$B$6'})
    # 특정 위치에 chart 추가
    worksheet.insert_chart('D2', chart)
    # 리소스 해제
    writer.close()
'''


# 이름, 전화번호, 성별, 나이, 주소, 학년, 점수
# 데이터 3개를 가지는 dataframe 생성
# excel에 저장 차트를 추가

def xml_std_writer():
    df = DataFrame({
        '이름': ['김길동', '박길동', '이길동', '최길동'],
        '주소': ['중구', '남구', '서구', '동구'],
        '학년': ['1학년', '2학년', '3학년', '1학년'],
        '점수': [70, 80, 90, 67],
    })

    df.set_index('이름', inplace=True)  # 이름을 인덱스로 지정함
    writer = pd.ExcelWriter('../DataBaseConnect 데이터베이스 연결/std_writer.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1')
    writer.close()  # 닫아줘야한다
    return df


'''
def xml_std_chartwriter():
    df = DataFrame({
        '이름': ['김길동', '박길동', '이길동'],
        '주소': ['중구', '남구', '서구'],
        '학년': ['1학년', '2학년', '3학년'],
        '점수': [70, 80, 90],

        # '김길동': ['4857', '중구', '남', '1학년', 79],
        # '박길동': ['1236', '남구', '남', '2학년', 80],
        # '이길동': ['8977', '서구', '여', '3학년', 90]
    })
    df.set_index('이름', inplace=True)
    writer = pd.ExcelWriter('std_wlsx_chart.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1')

    workbook = writer.book
    worksheet = writer.sheets['sheet1']
    # chart 객체 생성
    chart = workbook.add_chart({'type': 'column'})

    # # chart 에 출력할 데이터 선택
    chart.add_series({'name': '=sheet1!$A$2:$A$2', 'categories': '=sheet1!$D$1:$D$1', 'values': '=sheet1!$D$2:$D$2'})
    chart.add_series({'name': '=sheet1!$A$3:$A$3', 'categories': '=sheet1!$D$1:$D$1', 'values': '=sheet1!$D$3:$D$3'})
    chart.add_series({'name': '=sheet1!$A$4:$A$4', 'categories': '=sheet1!$D$1:$D$1', 'values': '=sheet1!$D$4:$D$4'})
    # # 특정 위치에 chart 추가
    worksheet.insert_chart('F2', chart)
    # # 리소스 해제
    writer.close()
'''
'''
def xml_std_chartwriter(dataframe):
    df = dataframe
    # df.set_index('이름', inplace=True)
    writer = pd.ExcelWriter('std_wlsx_chart.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1')

    workbook = writer.book
    worksheet = writer.sheets['sheet1']
    # chart 객체 생성
    chart = workbook.add_chart({'type': 'column'})

    # # chart 에 출력할 데이터 선택
    chart.add_series({'name': '=sheet1!$A$2:$A$2', 'categories': '=sheet1!$D$1:$D$1', 'values': '=sheet1!$D$2:$D$2'})
    chart.add_series({'name': '=sheet1!$A$3:$A$3', 'categories': '=sheet1!$D$1:$D$1', 'values': '=sheet1!$D$3:$D$3'})
    chart.add_series({'name': '=sheet1!$A$4:$A$4', 'categories': '=sheet1!$D$1:$D$1', 'values': '=sheet1!$D$4:$D$4'})
    chart.add_series({'name': '=sheet1!$A$5:$A$5', 'categories': '=sheet1!$D$1:$D$1', 'values': '=sheet1!$D$5:$D$5'})
    # # 특정 위치에 chart 추가
    worksheet.insert_chart('F2', chart)
    # # 리소스 해제
    writer.close()
'''

def xml_std_chartwriter(dataframe):
    df = dataframe
    # df.set_index('이름', inplace=True)
    writer = pd.ExcelWriter('../DataBaseConnect 데이터베이스 연결/std_wlsx_chart.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='sheet1')

    workbook = writer.book
    worksheet = writer.sheets['sheet1']
    # chart 객체 생성
    chart = workbook.add_chart({'type': 'column'})

    # # chart 에 출력할 데이터 선택
    chart.add_series({'name': '=sheet1!$D$1:$D$1', 'categories': '=sheet1!$A$2:$A$5', 'values': '=sheet1!$D$2:$D$5'})
    # # 특정 위치에 chart 추가
    worksheet.insert_chart('F2', chart)
    # # 리소스 해제
    writer.close()

# csv는 ,로 구분되어져 있다
if __name__ == '__main__':
    korean_font()
    # pandas_basic()
    # xml_writer2()
    # xml_writer2()
    # xml_std_writer()

    df = xml_std_writer()
    xml_std_chartwriter(df)
