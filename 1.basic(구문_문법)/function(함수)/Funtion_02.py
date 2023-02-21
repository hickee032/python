# 함수 02

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


def gugudan():
    for i in range(1,10):
        for j in range(2,10):
            print(f'{j} x {i} = {j*i}', end=" ")
        print()
    print()


def program_exit():
    print('프로그램 종료')
    exit()


def showmenu():
    print('콘솔프로그램 동작 테스트')
    print('1 계산기')
    print('2 구구단')
    print('3 프로그램 종료')
    menu = int(input('메뉴 선택'))
    return menu


if __name__ == '__main__':
    while True:
        select = showmenu()
        if select == 1:
            calculate1()
        elif select == 2:
            gugudan()
        elif select == 3:
            program_exit()
        else:
            print('잘못된 입력')

