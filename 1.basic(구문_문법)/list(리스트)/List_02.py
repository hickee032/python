# 2차원 리스트
name = [['홍길동', '남'], ['황진이', '여'], ['성춘향', '여']]  # 3x2 == 3행 2열
print(name)
print(name[0][0])  # 홍길동
print(name[2][0])  # 성춘향

for i in range(3):
    for j in range(2):
        print(name[i][j], end=' ')
    print()

for i in range(len(name)):
    for j in range(len(name[i])):
        print(name[i][j], end=' ')
    print()

# 향상된 for
for i in name:
    for j in i:
        print(j, end='\t')
    print()
print()

emptyList = []  # 비어있는 리스트
for i in [1, 2, 3]:
    for j in [4, 5, 6]:
        emptyList.append(i+j)
print('emptyList : ', emptyList)

# 한줄로 축약
emptyList2 = [i+j for i in [1, 2, 3] for j in [4, 5, 6]]
print('emptyList2 : ', emptyList2)

# 비어있는 2차원 리스트
row, col = 3, 4
arrList = [[0 for j in range(col)]for i in range(row)]
print('arrList : ', arrList)




