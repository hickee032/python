# 함수 5
'''
# 람다식
# 임시로 사용하는 간단한 방식의 익명 함수
def calc():
    a = 3
    b = 5
    return lambda x: a*x+b  # 이 부분이 익명 함수


c = calc()
print(c(1), c(2), c(3))  # c(1)에서 1이  lambda x: a*x+b 에 x 에 대입된다


# 람다 표현식 -> lambda (매개 변수) : (본문)
func1 = lambda x, y: x + y
func2 = lambda x: x * x
print(func1(10, 20))
print(func2(3))

# 람다 함수
def func1_lamb(n):
    return lambda x, y: x + y + n

lam1 = func1_lamb(10)
print(lam1(20, 30))
# 축약
print(func1_lamb(1)(2, 3))


# 람다식 + map()
# map() 두개를 맵핑한다고 보면 된다
# map((함수이름),(함수 매개변수))
num1 = [1, 2, 3, 4, 5]
num2 = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x*y, num1, num2)))  # [2, 8, 18, 32, 50]
print(list(map(lambda x: (x+10) if x % 2 == 0 else x, num1)))  # [1, 12, 3, 14, 5]

'''

# 람다식 + filter()
# filter((함수이름),(함수 매개변수))
num3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 3 == 0, num3)))  # 3의 배수

# 람다식 + reduce()
# reduce() 두번째 인자를 사용해서 요소가 1개가 될때 까지 함수가 계속 동작함
from functools import reduce  # 하나의 값이 될때까지 계속 합산

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
