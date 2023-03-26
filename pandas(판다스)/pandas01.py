import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame

def korean_font():
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False

def pandas_basic():
    df = pd.read_csv('test.csv', sep=',')
    print(df)
    print(type(df))
    ax = df.plot(kind='bar')
    ax.set_title('학생 성적표', fontsize=16)
    ax.set_xlabel('학생 이름')
    ax.set_ylabel('각과목 점수')
    ax.legend(loc='center')
    plt.show()

def xml_writer():
    df = DataFrame({'온도':[20.2, 22.3, 26.5, 30.2]})
    writer = pd.ExcelWriter('pandas_writer.xlsx',
                           engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.close()

def xml_writer2():
    df = DataFrame({'온도':[20.2, 22.3, 26.5, 30.2],
                    '습도':[30.2, 32.3, 36.5, 70.2],
                    '조도':[40.2, 42.3, 46.5, 50.2]})
    writer = pd.ExcelWriter('pandas_excel_chart.xlsx',
                           engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    # chart 객체 생성
    chart = workbook.add_chart({'type':'column'})
    # 차트에 출력할 데이터 선택
    chart.add_series({'values':'=Sheet1!$B$2:$B$5'})
    # 특정 위치에 차트 추가
    worksheet.insert_chart('D2', chart)
    # 리소스 해제
    writer.close()

def xml_writer_addr():
    df = DataFrame({'이름': ['홍길동', '전우치', '성춘향'],
                    '전화번호': ['010-1234-1234',
                             '010-1234-1111', '010-2222-1234'],
                    '성별': ['남', '남', '여'],
                    '나이': [100, 200, 300],
                    '주소': ['조선 한양 홍대감댁',
                           '조선 강원 두메산골',
                           '조선 전남 무주구천동'],
                    '직업': ['혁명가', '법사', '아가씨']})
    writer = pd.ExcelWriter('pandas_excel_addr.xlsx',
                            engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    chart = workbook.add_chart({'type': 'column'})
    chart.add_series({'values':'=Sheet1!$E$2:$E$4'})
    worksheet.insert_chart('D6', chart)
    writer.close()

if __name__ == '__main__':
    korean_font()
    #pandas_basic()
    #xml_writer()
    #xml_writer2()
    xml_writer_addr()