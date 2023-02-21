# 반복문

# 0~4까지 1씩 증가
# range(시작값 , 범위 , 증가값)
for i in range(0, 5, 1):
    print(i, end=' ')
print()

# 0~4까지 1씩 증가
for i in range(0, 5):
    print(i, end=" ")
print()

# 0~4까지 1씩 증가
for i in range(5):
    print(i, end=' ')
print()

# 0~4까지 1씩 증가
cnt = 0
while cnt < 5:
    print(cnt, end=" ")
    cnt += 1
print()

# continue
cnt = 1
while cnt < 50:
    cnt += 1
    if cnt % 2 == 0:
        continue
    print(cnt, end=" ")
print()

# break
cnt = 0
# while True : 무한루프
while True:
    if cnt == 20:
        print("무한 루프 탈출")
        break;
    cnt += 1
    print(cnt)
print()

# 이중반복문
# 3X4
num = 1
for i in range(3):  # 행
    for j in range(4):  # 열
        print(num,end=' ')
        num += 1
    print()
print()

# 동전 교환 O
# 국영수 O
# 블로그 if 3,4,5 switch문제3 if
# 블로그 반복문 4,6



