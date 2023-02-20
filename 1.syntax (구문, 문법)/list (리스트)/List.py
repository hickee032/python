# List
# 파이썬에서 배열은 없다 리스트가 배열의 역활
# 크기가 정해지지 않은 저장소

# 1차원 리스트
nameList = ['홍길동', '김길동', '박길동', '최길동']
# 타입을 헷갈릴수 있다
print('타입확인', type(nameList))

print('리스트 요소 : ', nameList)  # ['홍길동', '김길동', '박길동']
print('리스트 0번 : ', nameList[0])  # 홍길동
# 배열과 동일하게 사용

list_data = ['이순신', 100, '남자', '충남 아산']
age = []  # 비어있는 리스트 생성
print('타입확인 : ', type(list_data))

# 리스트 indexing
print(f'namelist 첫번째 요소 : {nameList[0]}')
print(f'namelist 마지막 요소 : {nameList[len(nameList)-1]}')

# 리스트 slicing (start index 포함)
print(f'첫번째 요소를 제외 : {nameList[1:]}')
print(f'마지막 요소를 제외 : {nameList[:2]}')  # 0 ~ 1
name_s1 = nameList[2:]  # 2 ~ 끝
print('name_s1 : ', nameList)

# 김길동 박길동만 잘라내보자
# name_s2 = nameList[1:-1] 이렇게도 가능하다
name_s2 = nameList[1:3]
print(f'문제 : {name_s2}')

# [start index : end index -1 : 증가치]
name_s4 = nameList[::2]  # 2칸씩 출력 (1번 출력 후 3번 출력 이런식)   # ['홍길동', '박길동']
print('name_s4 : ', name_s4)
name_s5 = nameList[::-1]  # 리스트 반전 데이터를 거꾸로
print('name_s5 : ', name_s5)

# 정렬
# 오름차순 정렬
nameList.sort()
print('오름차순으로 정렬 : ', nameList)

# 내림차순 정렬
nameList.sort(reverse=True)
print('내림차순으로 정렬 : ', nameList)

# list 마지막 요소 삭제
nameList.pop()
print('마지막 요소를 제거 : ', nameList)

# list 데이터 추가 ( list 마지막에 추가 )
nameList.append('이순신')
print('마지막에 추가 : ', nameList)

# list내의 데이터 개수확인
count = nameList.count('홍길동')
print('list내의 홍길동의 개수 :', count)

# list 데이터 삭제
nameList.remove('홍길동')
print('홍길동 삭제 함 : ', nameList)

# list 특정 위치에 추가
nameList.insert(2, '김유신')
print('3번째에 추가', nameList)

# unpacking
'''
name1, name2, name3, name4, name5, name6 = nameList
print('unpacking : ', name1, name2, name3)  # not enough values to unpack 오류
'''

name1, name2, name3, _, _, _ = nameList
print('unpacking : ', name1, name2, name3)

# list 축약 comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
event_num = [n for n in nums if n % 2 == 0]
# event_num = [n (3번) for n in nums (1번 반복문)  / if n % 2 == 0 (2번 제어문)]
print(event_num)

# and 조건문을 생략
num2 = [i for i in range(20) if i % 2 == 0 if i % 3 == 0 if i % 4 == 0]
print(num2)  # 2의 배수, 3의 배수, 4의 배수 모두 만족할 경우 0, 12

# 입력을 받아서 리스트에서 삭제
# 첫번째 방법
'''
nameList2 = ['홍길동', '김길동', '박길동', '최길동']
stringName = input('삭제 할 이름을 입력하세요 : ')
count2 = nameList2.count(stringName)
if count2 == 0:
    print(f'{stringName} 이름이 없습니다')
else:
    nameList2.remove(stringName)
    print(f'{stringName} 이름이 삭제 되었습니다')
print(nameList2)
'''
# 두번째 방법
'''
nameList3 = ['홍길동', '김길동', '박길동', '최길동']
stringName1 = input('삭제 할 이름을 입력하세요 : ')
if stringName1 in nameList3:
    nameList3.remove(stringName1)
    print(f'{stringName} 이름이 삭제 되었습니다')
else:
    print(f'{stringName} 이름이 없습니다')
print(nameList3)    
'''

# 세번째 방법 try ~ catch
'''
nameList3 = ['홍길동', '김길동', '박길동', '최길동']
stringName1 = input('삭제 할 이름을 입력하세요 : ')
try:
    nameList3.remove(stringName1)
    print(f'{stringName1} 이름이 삭제 되었습니다')
except ValueError:
    print(f'{stringName1} 이름이 없습니다')
print(nameList3)
'''
# ### sort(reverse=True) 와 reverce 의 차이점
'''
nameList.sort(reverse=True)
print('내림차순으로 정렬 : ', nameList)  # 정렬 후 내림차순
nameList.reverse()
print('뒤집기 : ', nameList)  # 정렬을 하지 않고 단순히 요소를 반전한다
'''



