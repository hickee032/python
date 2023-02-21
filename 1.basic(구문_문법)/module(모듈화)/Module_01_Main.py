# 모듈화 1
# 패키지 -> 연관성이 있는 파일들의 모음
# 모듈 -> 연관성이 있는 함수의 모음
# 모듈보다 패키지가 큰 개념이다

# 동일한 폴더 내에 존재해야한다
# 전부 가져오기
import Module_01_Calculate
res = Module_01_Calculate.plus(10, 20)
print('더하기 결과 : ', res)

# 한가지만 가져오기
from Module_01_Calculate import minus
print('빼기 결과 : ', minus(100, 50))

# 이런식으로도 가능
from Module_01_Calculate import minus, multi
print('빼기 결과 : ', minus(100, 50))
print('곱하기 결과 : ', multi(10, 3))

# 모든 모듈의 내용을 import

# 별명으로 사용하기
import Module_01_Calculate as ca
print(ca.plus(10, 20))
