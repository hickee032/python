# package(패키지): 연관성이 있는 파일 모음
# module(모듈): 연관성이 있는 함수들 모음

import calculator
res = calculator.plus(10, 20)
print('덧셈 결과:', res)

from calculator import minus, multi
print('뺄셈 결과:', minus(100, 50))
print('곱셈 결과:', multi(100, 50))

# 모든 모듈의 내용을 import
#from calculator import *

import calculator as ca
print(ca.plus(10, 30))

# 패키지 1 - 1개의 파일만 존재
from mypackage import calculator as c
res = c.plus(10, 20)
print('패키지 덧셈:', res)

from mypackage2 import module1, module2
module1.show_mod_info()
module2.show_mod_info()

