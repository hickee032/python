import random

# 3개의 숫자를 입력 받아 크기가 큰 순서대로 출력
"""
def inputlarge(a, b, c):
    if a > b:
        if a > c:
            if b > c:
                print(f'{a} {b} {c}')
            else:
                print(f'{a} {c} {b}')
        else:
            print(f'{c} {a} {b}')
    else:  # b>a
        if b > c:
            if a > c:
                print(f'{b} {a} {c}')
            else:
                print(f'{b} {c} {a}')
        else:
                print(f'{c} {b} {a}')

n1 = int(input("1 : "))
n2 = int(input("2 : "))
n3 = int(input("3 : "))

inputlarge(n1, n2, n3)
"""

# 숫자 2개를 입력 받아 4칙연산
"""
def plus(a, b):
    return a + b


def minus(a, b):
    return a / b


def multy(a, b):
    return a * b


def div(a, b):
    return a / b


def calculate(num1, num2, op):
    result = 0
    if op == '+':
        result = plus(num1, num2)
    elif op == '-':
        result = minus(num1, num2)
    elif op == '*':
        result = multy(num1, num2)
    elif op == '/':
        if num2 == 0:
            result = "0으로 나눌수 잆습니다"
        else:
            result = div(num1, num2)
    else:
        result = "잘못된 입력"
    return result


n1 = int(input("1 : "))
n2 = int(input("2 : "))
opr = input("op : ")

print(calculate(n1, n2, opr))
"""

# 홀수와 짝수
"""
def oddeven(data):
    arr = list()
    for i in range(len(data)):
        if data[i] % 2 == 0:
            arr.append('짝수')
        else:
            arr.append('홀수')
    for j in range(len(data)):
        print(f'{data[j]} 는 {arr[j]}')


num = list()
for i in range(11):
    num.append(random.randint(1, 100))

oddeven(num)
"""

# 국 영 수 점수를 입력받아 총점과 평균 값
"""
def studentscore():
    dic = {'국어': '', '영어': '', '수학': ''}
    res_dic = {'총점': '', '평균': ''}
    total = 0

    for key, value in dic.items():
        score = input(f'{key} 점수를 입력하세요:')
        while True:
            if 0 <= int(score) <= 100:
                dic[key] = score
                break
            else:
                print('잘못된 입력')

    for key, value in dic.items():
        total += int(value)

    res_dic['총점'] = total
    res_dic['평균'] = total / len(dic)

    for key, value in res_dic.items():
        print(f'{key} : {value}')

studentscore()
"""

# 1개의 숫자를 입력받아 구구단
"""
def gugudan(a):
    for i in range(1, 10):
            print(f"{a} x {i} = {a*i}")

num = int(input('숫자를 입력 : '))
gugudan(num)
"""
# 간단한 로또 출력 리스트 리턴
"""
def lotto():
    lottonum = []
    for i in range(7):
        lottonum.append(random.randint(1,45))
    return lottonum

lottNum = lotto()
print(lottNum)
"""
# 1~ 100까지의 합 짝수 합 홀수 합
"""
def sumodeven(a):
    odd = 0
    even = 0
    for i in range(a+1):
        if i % 2 == 0:
            odd += i
        else:
            even += i
    print(f'홀수의 합 {odd}, 짝수의 합 {even} 전체의 합 {odd+even}')

sumodeven(10)
"""
# 3개의 숫자를 입력 받아 최대 최소
"""
def maxmin(a,b,c):
    max = 0
    min = 0
    if a > b:
        if a > c:
            max = a
            if b > c:
                min = c
            else:
                min = b
        else:
            max = c
            min = b
    elif b > c:
        if b > a:
            max = b
            if a > c:
                min = c
            else:
                min = a
        else:
            max = a
            min = c
    else:
        if c > a:
            max = c
            if a > b:
                min = b
            else:
                min = a
        else:
            max = a
            min = b
    print(f'최대값 {max} 최소값 {min}')

maxmin(3,2,1)
maxmin(1,4,3)
maxmin(1,4,5)
"""
# 점수 랜덤으로 학점을 출력 -> 5명의 국영수 점수

row, col = 3, 5
total = 0
scoreList = [[random.randint(1, 101) for i in range(row)] for j in range(col)]
scoretotal = []
scoreavr = []
for i in range(len(scoreList)):
    for j in range(len(scoreList[i])):
        total += scoreList[i][j]
    scoretotal.append(total)
    scoreavr.append(int(total / 3))
    total = 0

for i in range(5):
    print(f"{i+1} 번 학생의 총점 {scoretotal[i]} 평균 {scoreavr[i]} ")

