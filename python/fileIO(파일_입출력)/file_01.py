# 파일 제어

"""
# 1. 기본 파일 쓰기
file = open('test.txt', 'w')
file.write('안녕하세요')
file.close()

# 2. 파일 읽기
try:
    file = open('test1111.txt', 'r')
    data = file.read()  # 파이썬은 실행하는 시점에서 변수에 값이 있는 지 파악하여 메모리에 할당한다
    print(data)
    # file.close()
except FileNotFoundError as e:
    print('파일을 찾을수가 없습니다.')
finally:  # 생략가능
    file.close()  # 오류가 발생

try:
    file = open('test.txt', 'r')
    data = file.read()  # 파이썬은 실행하는 시점에서 변수에 값이 있는 지 파악하여 메모리에 할당한다
    print(data)
    # file.close()
except FileNotFoundError as e:
    print('파일을 찾을수가 없습니다.')

# 3. 라인 단위로 파일쓰기
lines = ['안녕하세요\n', '반갑습니다\n', '홍길동입니다']
try:
    with open('hello.txt','w') as f:
        for line in lines:
            f.write(line)
except Exception as err:
    print('파일 쓰기 에러 : ', err)
else:
    print('파일 쓰기 성공')

# 4. 라인 단위로 파일 읽기
try:
    with open('hello.txt','r') as f:
        line = f.readline()
        while line != '':
            print(line)
            line = f.readline()
except FileNotFoundError as err:
    print('파일 읽기 에러 : ', err)


# 5. 라인 전체를 파일에 쓰기
lines = ['안녕하세요2\n', '반갑습니다2\n', '홍길동입니다2']
try:
    with open('hello2.txt', 'w') as f:
        f.writelines(lines)

# 코드는 순차적으로 실행된다 Exception이 위에 존재한다면 FileNotFoundError 에러라 하더라도 위쪽 Exception 에 걸리게 되어
# 예외 처리문을 빠져 나가 FileNotFoundError에는 걸리지 않게 된다
# 아래의 두개의 예외처리 는 순서를 바꿔 줘야한다 ( FileNotFoundError 위에 Exception 아래에 )

except Exception as err:  # Exception 은 모든 오류가 걸림
    print('파일 쓰기 에러 : ', err)
except FileNotFoundError as err:  # FileNotFoundError 파일 찾기 오류가 거림
    print('파일 찾기 에러 : ', err)

# 6 전체 라인을 파일로 열기
try:
    with open('hello2.txt', 'r') as f:
        lines = f.readlines()  # 오타 주의 ( readlines, readline )
        for line in lines:
            print(line)
except FileNotFoundError as err:
    print('파일 읽기 에러 : ', err)  # err 내부에는 다양한 에러 정보가 존재
except Exception as err:
    print('알수 없는 에러 : ', err)


# 7 utf-8 타입으로 쓰기
lines = ['안녕하세요', 'こんにちは', '你好']
with open('hello_utf8.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        f.write(line+'\n')

# utf-8 읽기
with open('hello_utf8.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# bin (바이너리) 파일 쓰기
import struct
struct_fmt = '=16s2fi'  # char[16] float[2] int
city_info = [
    ('서울'.encode(encoding='utf-8'), 37.566, 126.977, 1),
    ('뉴욕'.encode(encoding='utf-8'), 48.712, -74.005, 2),
    ('파리'.encode(encoding='utf-8'), 48.856, 2.352, 3),
    ('런던'.encode(encoding='utf-8'), 51.507, -0.127, 4),
]
with open('city_info.dat', 'wb') as f:
    for city in city_info:
        f.write(struct.pack(struct_fmt, *city))
"""
import struct

struct_fmt = '16s2fi'  # format 형태 지정
struct_len = struct.calcsize(struct_fmt)
cities = []
with open('../../city_info.dat', 'rb') as f:
    while True:
        buffer = f.read(struct_len)
        if not buffer: break
        city = struct.unpack(struct_fmt, buffer)
        cities.append(city)

for city in cities:
    name = city[0].decode(encoding='utf-8')
    print(f'도시 : {name} 경도 {city[1]:.2f} 위도 {city[2]:.2f}, 점수 {city[3]}')  # city[1]:.2f 소수점 두자리
