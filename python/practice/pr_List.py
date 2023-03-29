# 리스트 List
'''
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("b의 요소 :", a)
print("b 0번 인덱스 :", a[0])
print("b의 길이 :", a[-1])
print(len(a))
print("a[len(a)-1] : ", a[len(a)-1])
print(a[2:])

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0],a[2][2][1])

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[3][:2])

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
str1 = "번째"

print(str(a[2])+str1)

# 리스트 수정 삭제
c = [1, 2, 3, 4, 5]
print('바뀌기 전 - ', c)
c[0] = 6
print('수정 함 - ', c)
del c[0]
print('삭제 함 - ', c)
del c[2:3]
print('슬라이싱 삭제 함 - ', c)

c.append(1)
print('추가함 - ', c)
c.insert(2, 7)
print('인덱스 추가함 - ', c)
c.sort()
print('정렬 - ', c)
c.reverse()
print('뒤집기 - ', c)
c.pop(len(c)-1)
print('끄집어 내기 - ', c)

print('1 의 개수  - ', c.count(1))
print('7 의 개수  - ', c.count(7))

b = ['김', '이', '박', '최', '김']
print('김 의 개수  - ', b.count('김'))
print('이 의 개수  - ', b.count('이'))

b.extend(['정', '최'])
print('확장 함', b)
'''
# 튜플 Tuple
tu1 = ()
tu2 = (1,)
tu3 = (1, 2, 3)
tu4 = 1, 2, 3
tu5 = ('a', 'b', ('ab', 'cd'))

