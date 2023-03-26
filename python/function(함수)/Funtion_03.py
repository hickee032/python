# 함수 3
# 객체 지향 언어
# 오버로딩을 지원하지 않는 다
# 디폴트 매개변수, 가변 매개변수

# 디폴트 매개변수 1
# def printstr(text, count=1):
#     for i in range(count):
#         print(text)


# 매개 변수가 하나만 들어가면 디폴트 값이 1 ( count = 1 )
#  count = 1 디폴트 매개변수는 반드시 뒤에 와야한다
# printstr('매개변수 1개 일 경우')
# printstr('안녕하세요')
# 매개변수가 두개가 들어가면 디폴트 값이 변화햔다
# printstr('매개변수 2개 일 경우')
# printstr('안녕하세요', 5)


# 디폴트 매개변수 2
# def print_info(name, pos='staff', nation='korea'):
#     print(f'{name}')
#     print(f'{pos}')
#     print(f'{nation}')
#
#
# print_info(name='홍길동', pos='혁명가', nation='율도국')
# print('---------')
# print_info('김길동')

# 가변인자 - tuple
# tuple을 매개변수로 쓸때는 * 이 필요하다
# def str_append(*textlist):
#     res = ''
#     for i in textlist:
#         res += i
#     return res
#
#
# print(str_append('아버지가 방에 들어가신다'))
# print(str_append('아버지가 방에'))
# print(str_append('아버지가'))
# tup = ('가', '나', '다', '라')
# print(str_append(*tup))  # * 을 사용하여 매개변수를 쓴다


# 가변인자 - dictionary
# 매개변수 사용시 ** 필요
#
# def show_team(**player):
#     for i in player.keys():
#         print(f'{i}={player[i]}')
#     print()
#
#
# show_team(노이어='GK', 호날두='FW')
# show_team(노이어='GK', 호날두='FW', 손흥민='DF')
# show_team(노이어='GK', 호날두='FW', 손흥민='DF', 메시='MF')
#
#
# # 일반 매개변수 + 가변 매개변수
# def print_args(argc, *argv):
#     for i in range(argc):
#         print(argv[i])
#
#
# print_args(2, '1', '2')
# # print_args(3, '1', '2')  # 가변 매개변수 개수를 넘어가기 때문에 오류가 생김
# # print_args(argc=2,'1', '2') # 사용 불가
# print_args(4, '1', '2', '3', '4')
#
# tu = (1, 2)
# print_args(len(tu), *tu)
#

def tuple_func(*data):
    for i in data:
        for j in i:
            print(j, end='\t')
        print()


t_data = ('홍길동', 200, '한양')
tuple_func(t_data)
tt_data = ('전우치', 300, '산골')
tuple_func(tt_data)


# 재귀함수
def factorial(cnt):
    if cnt > 0:
        factorial(cnt-1)
    print(cnt)


factorial(3)
