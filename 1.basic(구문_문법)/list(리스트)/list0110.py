# list : 배열은 없고 리스트가 배열 역활
# 크기가 정해지지 않은 저장소
# 1차원 리스트
name = ['홍길동', '김길동', '박길동', '최길동']
print('타입확인:', type(name))
print(name)
print(name[0])  # 배열과 동일하게 사용

list_data = ['이순신', 100, '남자', '충남 아산']
age = []  # 비어있는 리스트 생성
print(type(list_data))

# indexing
print(f'name 첫번째 요소:{name[0]}')
print(name[2])

# slicing
# [start:end-1]
print(name[0:2])  # 0 ~ 1
print(name[:2])  # 0 ~ 1
name_s1 = name[2:]  # 2 ~ 끝까지
print(name_s1)
name_s2 = name[1:3]  # 김길동, 박길동
name_s3 = name[1:-1]  # 김길동, 박길동
print(name_s2, name_s3)

# [start:end-1:증가치]
name_s4 = name[::2]  # 홍길동, 박길동
name_s5 = name[::-1]  # 데이터 반전
print(name_s5)

# 오름차순 정렬
name.sort()
print('오름차순 정렬:', name)

# 내림차순 정렬
name.sort(reverse=True)
print('내림차순 정렬:', name)

# 마지막 data 삭제
name.pop()
print('1번째 데이터 삭제:', name)

# list 마지막에 추가
name.append('이순신')
print('마지막에 추가:', name)

# list 내의 데이터 개수 확인
cnt = name.count('홍길동')
print('list내의 홍길동 수:', cnt)

# 데이터 삭제
name.remove('홍길동')
print('데이터 삭제:', name)

# 입력을 받아서 list에서 삭제
name = ['홍길동', '김길동', '박길동', '최길동', '마길동']
delName = input('리스트에서 삭제할 이름 입력:')
# if delName in name:
#     name.remove(delName)
#     print(f'{delName} 삭제!')
# else:
#     print(f'{delName} 데이터가 없습니다.')

try:
    name.remove(delName)
    print(f'{delName} 삭제!')
except ValueError:
    print(f'{delName} 데이터가 없습니다.')

print('원하는 이름 삭제:', name)

# list 특정 위치에 추가
name.insert(2, '김유신')
print(name)

# unpacking
name1, name2, name3, name4, name5, name6 = name
print('unpacking:', name1, name2, name3)

# name1, name2, name3 = name 오류발생
name1, name2, name3, _, _, _ = name
print('unpacking:', name1, name2, name3)

# list 축약형식 (comprehension)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
event_num = [n for n in nums if n % 2 == 0]
print(event_num)

# and 조건문 생략
num2 = [i for i in range(20) if i%2==0 if i%3==0 if i%4==0]
print(num2)

# 2차원 리스트
# 3행 x 2열
name = [['홍길동', '남'], ['황진이', '여'],
        ['성춘향', '여']]
print(name)
print(name[0][0])   # 홍길동
print(name[2][0])   # 성춘향

# 3x2 name 출력
for i in range(3):
    for j in range(2):
        print(name[i][j], end='\t')
    print()
print()

for i in name:
    for j in i:
        print(j, end='\t')
    print()
print()

emptyList = []  # 빈 리스트
for i in [1, 2, 3]:
    for j in [4, 5, 6]:
        emptyList.append(i+j)
print(emptyList)

# 1줄 축약
emptyList = [i+j for i in [1,2,3] for j in [4,5,6]]
print(emptyList)

# 비어있는 2차원 리스트 생성
row, col = 3, 4
arrList = [[0 for j in range(col)] for i in range(row)]
print(arrList)

# 튜플(tupple) - 수정, 삭제 불가
# list: [], tupple: (), dictionary: {}
my_num = (1, 2, 3, 4, 5)
print(type(my_num))
print('튜플 첫번째 데이터:', my_num[0])







