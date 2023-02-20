'''
# 1. 과일이름 3개를 가지는 리스트 생성.
fruit = ['사과', '배', '수박']
# 2. 음식이름 3개를 가지는 리스트 생성.
food = ['샐러드', '생선구이', '라면']
# 3. 1번과 2번 리스트를 하나로 합치는 hap 리스트 생성.
hap = fruit + food
print(hap)
# 4. hap 리스트에서 마지막 과일을 '멜론' 으로 변경.
hap[len(hap)-1] = '멜론'
print(hap)
# 5. hap에서 마지막 음식을 삭제하기.
hap.remove(hap[len(hap)-1])
print(hap)

student = ['홍길동', '김길동', '전우치']
print(student)
# 1. 학생이 3명인 컴퓨터과에 '이황'이 편입
student.append('이황')
print(student)
# 2. 동명이인 전우치가 편입하여 전우치 뒤에 추가됨.
student.append('전우치')
print(student)
# 3. '전우치'가 몇명인지 확인하기
count = student.count('전우치')
print(f'전우치는 {count} 명입니다')
# 4. '홍길동'이 자퇴했음. 홍길동 삭제
student.remove('홍길동')
print(student)
# 5. 현재 출석부 리스트에서 2번째 학생 삭제.
student.remove(student[1])
print(student)
# 6. 출석부를 내림차순으로 정렬
student.sort(reverse=True)
print(student)

# 1. {'강감찬':'귀주대첩', '이순신':한산대첩', '세종대왕':'집현전'}
dic_great = {'강감찬': '귀주대첩', '이순신': '한산대첩', '세종대왕': '집현전'}
print(dic_great)
# 위의 딕셔너리 생성하고 '이성계':'조선건국' 추가
dic_great['이성계'] = '조선건국'
print(dic_great)
# 2. 세종대왕:집현전을 세종대왕:한글로 수정
dic_great['세종대왕'] = '한글'
print(dic_great)

# 3. 이순신 key를 검색하여 있으면 삭제, 없으면 김유신:황산벌 추가
if dic_great.get('이순신') is not None:
    del dic_great['이순신']
    print(dic_great)
else:
    dic_great['김유신'] = '황산벌'

# 리스트의 합과 평균
numList = [20, 34, 22, 14, 36, 23, 67]
result = 0
for i in range(len(numList)-1):
    result = result + numList[i]

print(f'합은 {result} 평균은 {int(result / len(numList))} ')

# 1~100까지 리스트에 저장 5의 배수만 출력
numList2 = []
for i in range(101):
    numList2.append(i)

for i in range(len(numList2)):
    if numList2[i] % 5 == 0:
        print(numList2[i], end=' ')


numList3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numList3.sort(reverse=True)
print(numList3)


# 이차원 리스트의 출력
numlist4 = [[1, 2], [2, 4, 6], [3, 6], [4, 8, 10, 12], [10]]
for i in range(len(numlist4)):
    for j in range(len(numlist4[i])):
        print(f'numlist4[{i}][{j}] = {numlist4[i][j]}', end=' ')
    print()


# 이차원 리스트의 덧셈
numlist5 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numlist6 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
numlist7 = [[0 for j in range(3)]for i in range(3)]
for i in range(len(numlist5)):
    for j in range(len(numlist5)):
        numlist7[i][j] = numlist5[i][j]+numlist6[i][j]

print(numlist7)
'''
import random

# 로또 번호를 출력
lotto = []
for i in range(7):
    lotto.append(random.randint(1,37))
print(lotto)



