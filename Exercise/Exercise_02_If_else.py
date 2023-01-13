# -*- coding: utf-8 -*-

# 블로그 if 3,4,5 switch 문제3 if
# 블로그 반복문 4,6

# 홀짝 계산기
num = int(input("숫자를 입력하세요"))
if num % 2 == 0:
    print(f"{num}은 짝수입니다.")
else:
    print(f"{num}은 홀수입니다.")

# 간단한 계산기
'''
firNum = int(input("첫번째 숫자를 입력 :"))
secNum = int(input("두번째 숫자를 입력 :"))
operator = input("연산자를 입력 :")

if operator == '+':
    print(f"{firNum} {operator} {secNum} = {firNum+secNum}")
elif operator == '-':
    print(f"{firNum} {operator} {secNum} = {firNum-secNum}")
elif operator == '*':
    print(f"{firNum} {operator} {secNum} = {firNum*secNum}")
elif operator == '/':
    if secNum == 0:
        print("0 으로 나눌수 없습니다")
    else:
        print(f"{firNum} {operator} {secNum} = {int(firNum / secNum)}")
else:
    print("잘못된 연산자 입니다")
'''

# 윤년
# 4로 나누면 나머지 0 100으로 나누면 0이 아님 400으로 나누면 나머지 0
'''
year = int(input("년도를 입력해주세요"))
if year % 4 ==0 and year / 100 != 0  or year / 400 == 0  : 
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")
'''
# 원하는 음료수
'''
print("--------------------------")
print("1. 콜라 1100")
print("2. 사이다 900")
print("3. 환타 1000")
print("--------------------------")
num = int(input("음료수를 선택하세요 : "))
if num == 1:
    print("콜라를 선택하였습니다")
    print("--------------------------")
    money = int(input("금액를 입력하세요 : "))
    if money < 1100:
        print("구입할수 없습니다.")
    else:
        print(f"거스름돈은 {money - 1100} 입니다")
elif num == 2:
    print("사이다를 선택하였습니다")
    print("--------------------------")
    money = int(input("금액를 입력하세요 : "))
    if money < 900:
        print("구입할수 없습니다.")
    else:
        print(f"거스름돈은 {money - 900} 입니다")
elif num == 3:
    print("환타를 선택하였습니다")
    print("--------------------------")
    money = int(input("금액를 입력하세요 : "))
    if money < 1000:
        print("구입할수 없습니다.")
    else:
        print(f"거스름돈은 {money - 1000} 입니다")
'''

# 두개의 숫자를 입력 두수 사이의 합
'''
result = 0
n = int(input("첫번째 숫자를 입력"))
m = int(input("두번째 숫자를 입력"))
for i in range(n, m + 1):
    result += i
print(result)
'''
# 구구단 출력
'''
for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j} * {i} = {i*j}', end=' ')
    print()
'''
