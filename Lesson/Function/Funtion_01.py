##########################
#   함수
##########################
# 다른언어와 다르게 타입이 없음
# 1. 매개변수 X, 리턴값 X
# 2. 매개변수 O, 리턴값 X
# 3. 매개변수 X, 리턴값 O
# 4. 매개변수 O, 리턴값 O

# 1번 형태 - 함수 정의
# 1. 매개변수 X, 리턴값 X
def calculate1():
    num1 = int(input('1번째 숫자 입력:'))
    num2 = int(input('2번째 숫자 입력:'))
    op = input('연산자 입력(+,-,*,/)')
    if op == '+':
        res = num1 + num2
        print(f'{num1}+{num2}={res}')
    elif op == '-':
        res = num1 - num2
        print(f'{num1}-{num2}={res}')
    elif op == '*':
        res = num1 * num2
        print(f'{num1}x{num2}={res}')
    elif op == '/':
        res = num1 / num2
        print(f'{num1}/{num2}={res}')


# 2번 형태
# 2. 매개변수 O, 리턴값 X
def calculate2(num1, num2, op):

    if op == '+':
        res = num1 + num2
        print(f'{num1}+{num2}={res}')
    elif op == '-':
        res = num1 - num2
        print(f'{num1}-{num2}={res}')
    elif op == '*':
        res = num1 * num2
        print(f'{num1}x{num2}={res}')
    elif op == '/':
        res = num1 / num2
        print(f'{num1}/{num2}={res}')


# 3번 형태
# 3. 매개변수 X, 리턴값 O
def calculate3():
    num1 = int(input('1번째 숫자 입력:'))
    num2 = int(input('2번째 숫자 입력:'))
    op = input('연산자 입력(+,-,*,/)')
    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    elif op == '/':
        res = num1 / num2
    return res

# 리턴 타입을 명시 하는 방법
"""
def calculate3() -> int: # -> int ( 강제성이 없음 )
    num1 = int(input('1번째 숫자 입력:'))
    num2 = int(input('2번째 숫자 입력:'))
    op = input('연산자 입력(+,-,*,/)')
    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    elif op == '/':
        res = num1 / num2
    return res
"""


# 4번 형태
# 4. 매개변수 O, 리턴값 O
def calculate4(num1, num2, op):

    if op == '+':
        res = num1 + num2
    elif op == '-':
        res = num1 - num2
    elif op == '*':
        res = num1 * num2
    elif op == '/':
        res = num1 / num2
    return res


# 전역 변수, 지역 변수  -> 반드시 함수에서만 적용
gNum = 200  # 전역 변수

def funcLocal():
    # pass  # 빈 함수를 쓰겠다는 표현
    # gNum = 100  # 지역 변수
    gNum = 300
    print("funcLocal : ", gNum)

def funcGlobal():
    global gNum  # 전역변수를 사용하기 위해서는 global 키워드가 필요함
    print("funcGlobal : ", gNum)


def funcList():
    my_list = ['홍길동', 500, '남자', '조선 한양']
    return my_list


print('주의) __main__ 과 상관없이 동작함')  # 메인과 상관없이 실행된다 영향을 받지 않는다

if __name__ == '__main__':  # 파이썬은 순차적 ( 메인이 없다 ) 메인의 흉내를 내기 위해 이 라인을 씀
    # 이것에 의해서 메인이 통제된다
    # calculate1()  # 함수 호출

    # 매개변수 사용
    # calculate2 에 매개변수 전달
    # n1 = int(input('1번째 숫자 입력:'))
    # n2 = int(input('2번째 숫자 입력:'))
    # op = input('연산자 입력(+,-,*,/)')
    # calculate2(n1, n2, op)

    # 리턴값 사용
    # print("calculate3() : ", calculate3())

    # 매개변수 사용, 리턴값 사용
    # calculate4 에 매개변수 전달
    # n1 = int(input('1번째 숫자 입력:'))
    # n2 = int(input('2번째 숫자 입력:'))
    # op = input('연산자 입력(+,-,*,/)')
    # print("calculate4 : ", calculate4(n1, n2, op))

    # funcLocal()
    # funcGlobal()

    list1 = funcList()
    print(type(list1))
    print(list1)
    name, age, gender, addr = funcList()
    print(type(name))
    print('다받은 것 : ', name, age, gender, addr)

    name1, age1, _, _ = funcList()
    print(type(name))
    print('제외한 것 : ', name1, age1, gender1, addr1)
