# 함수 4
# 함수를 변수에 담기 1
def myfunc(a):
    print(a)


# p 가 마치 함수가 된것 처럼 동작한다
p = myfunc
p(1111)
p('홍길동')


# 함수를 변수에 담기 2
def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


# first 리스트에 담아 사용가능하다
first = [plus, minus]
n1, n2 = 2, 1
print(first[0](n1, n2))
print(first[1](n1, n2))


# 함수를 매개변수에 담기 3
def hello_korea():
    print('안녕하세요')


def hello_english():
    print('Hello')


def greet(hello):
    hello()


greet(hello_korea)
greet(hello_english)


# 함수를 리턴
def greet2(wh):
    if wh == 'korea':
        return hello_korea
    else:
        return hello_english


hello = greet2('korea')
hello()

# 중첩 함수 Nested function
# 외부에서는 접근 불가
import math


def studdev(*args):
    def mean():  # 평균
        return sum(args) / len(args)

    def variance(m):  # 분산 -> 평균으로부터 데이터가 얼마나 떨어져있는 정도
        total = 0
        for arg in args:
            total += (arg - m) ** 2  # 분산을 제곱을 하는 이유 -> 평균으로 부터 오차를 부각시키기 위해서 (-1 음수를 없애기 위해)
        return total / (len(args) - 1)

    v = variance(mean())  # 내부에 있는 함수는 이시점에서 동작된다
    return math.sqrt(v)  # 표준편차  -> sqrt 루트 ( 위시점에 제곱한것을 처리 )


print(studdev(1, 2, 3, 4))
