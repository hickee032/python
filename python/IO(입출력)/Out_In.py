# 파이썬 : 스크립트 언어
# C C++ C# Java : 컴파일러 언어 엄밀히 말하면 Java는 둘다 있다

# 주석 처리
# 1줄 주석

"""
여러줄 주석
"""

# 변수 타입이 존재 하지 않음

num = 3
str1 = "홍길동"
fNum = 3.14

# 단일 변수 출력
print('num : ', num)
print('str1 : '+str1)

num = 2000
pi = 3.1415
print('정수 num%d' % num)
print("실수 pi%.2f" % pi)
print("정수 num%d,실수 pi%.2f" % (num, pi))

name = "이순신"
gender = "남자"
age = 120
addr = "충무 명량"

print("이름: {0}, 성별: {1},나이: {2}".format(name, gender, age))
print(f"이름{name},성별{gender},나이{age}")

# 변수 타입에 구분자 추가
print(name, gender, age, addr, sep="/")

# 콘솔 입력 - 기본 적으로 문자열 타입
in1 = input("첫번쨰 정수 입력 : ")
in2 = input("두번째 실수 입력 : ")
# 변수의 타입을 확인
print(type(in1))
# <class 'str'>

print(type(in2))
# <class 'str'>

res = int(in1) + float(in2)
print(f"res:{res}")

# 위 두개를 합친것
in3 = int(input("세번째 정수 입력 :"))
in4 = int(input("네번째 실수 입력 :"))
