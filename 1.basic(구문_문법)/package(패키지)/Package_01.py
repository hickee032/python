# 패키지 1
# 1개의 파일만 존재
# 패키지 폴더안에 __init__ 빈 파이썬 파일이 필요

from mypackage import Package_01_Calculate
res = Package_01_Calculate.plus(10, 20)
print('패키지 덧셈 : ', res)

from mypackage import Package_01_Calculate as ca
res = ca.plus(10, 20)
print('패키지 덧셈 : ', res)

# 패키지 2
# 여러개의 파일만 존재
# 패키지 폴더안에 __init__ 파일 안에 __all__ = ['Package_01_Calculate','Module1','Module2','Module3','Module4'] 필요
# __all__ = [파이선 파일의 이름]
# Module안 __name__ 은 자기자신의 이름을 지칭한다

from mypackage2 import Module1, Module2
Module1.show_mod_info()
Module2.show_mod_info()
