#=========================
#   파일 제어
#=========================
# 1. 기본 파일 쓰기
# file = open('test.txt', 'w')
# file.write('안녕하세요')
# file.close()
import struct

# 2. 기본 파일 읽기
# try:
#     file = open('test1111.txt', 'r')
#     data = file.read()
#     print(data)
#     file.close()
# except FileNotFoundError as e:
#     print('파일을 찾을수가 없습니다.')
# # finally: # 생략 가능
# #     file.close()

# 3. 라인 단위로 파일 쓰기
# with open() 으로 파일을 제어하면 close() 생략 가능
# lines = ['안녕하세요\n', '반갑습니다\n', '홍길동입니다']
# try:
#     with open('hello.txt', 'w') as f:
#         for line in lines:
#             f.write(line)
#         #print('파일 쓰기 성공!')
# except Exception as err:
#     print('파일 쓰기 에러: ', err)
# else:
#     print('파일 쓰기 성공!')

# 4. 라인 단위로 파일 읽기
# try:
#     with open('hello.txt', 'r') as f:
#         line = f.readline()
#         while line != '':
#             print(line)
#             line = f.readline()
# except FileNotFoundError as err:
#     print("파일 읽기 에러: ", err)

# 라인 전체를 파일에 쓰기
# lines = ['안녕하세요2\n', '반갑습니다2\n', '홍길동입니다2']
# try:
#     with open('hello2.txt', 'w') as f:
#         f.writelines(lines)
# except FileNotFoundError as err:
#     print('FileNotFoundError:', err)
# except Exception as err:
#     print('파일 처리 에러:', err)

# 전체 라인을 파일로 읽기
# try:
#     with open('hello2.txt', 'r') as f:
#         lines = f.readlines() # 오타 주의
#         for line in lines:
#             print(line)
# except FileNotFoundError as err:
#     # err 내부에 다양한 에러 정보가 존재함
#     print('파일 읽기 에러:', err)
# except Exception as err:
#     print('알수없는에러:', err)

# utf8 타입으로 쓰기
# lines = ['你好', 'こんにちは', '안녕하세요']
# with open('hello_utf8.txt', 'w', encoding='utf-8') as f:
#     for line in lines:
#         f.write(line+"/")
#
# # utf8 읽기
# with open('hello_utf8.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)

# bin 파일 쓰기
# # import struct
struct_fmt = '=16s2fi' # char[16], float[2], int
city_info = [
    ('서울'.encode(encoding='utf-8'), 37.566, 126.977, 100),
    ('뉴욕'.encode(encoding='utf-8'), 40.712, -74.005, 200),
    ('파리'.encode(encoding='utf-8'), 48.856, 2.352, 300),
    ('런던'.encode(encoding='utf-8'), 51.507, -0.127, 400)
]
with open('citi_info.dat', 'wb') as f:
    for city in city_info:
        f.write(struct.pack(struct_fmt, *city))

struct_fmt = '=16s2fi'
struct_len = struct.calcsize(struct_fmt)
cities = []
with open('citi_info.dat', 'rb') as f:
    while True:
        buffer = f.read(struct_len)
        if not buffer: break
        city = struct.unpack(struct_fmt, buffer)
        cities.append(city)

for city in cities:
    name = city[0].decode(encoding='utf-8')
    print(f'도시:{name}, '
          f'경도/위도:{city[1]}/{city[2]},'
          f'인기점수:{city[3]}')












