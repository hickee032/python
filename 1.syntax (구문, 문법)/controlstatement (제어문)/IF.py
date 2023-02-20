# 제어문
# switch 없음

# if 조건 :

num = 100
if num > 0:
    print(f'{num}은 0보다 크다')  # 반드시 tap(들여쓰기) 필요하다

# if문은 구문은 tap안에서 사용 한다
if num > 0:
    print(f'1.{num}은 0보다 크다')
    print(f'2.{num}은 0보다 크다')

# 한줄로도 가능하다

if num > 0: print(f'한줄 1.{num}은 0보다 크다'); print(f'한줄 2.{num}은 0보다 크다')

# if 조건 : - else
if num > 10:
    print(f"if : {num}은 0보다 크다")
else:
    print(f"else:  {num}은 0보다 작다")

# if 조건 : -elif 조건 : -else
day = input("요일을 입력하세요")
if day == '월':
    print("월요일")
elif day == '화':
    print("화요일")
elif day == '수':
    print("수요일")
elif day == '목':
    print("목요일")
elif day == '금':
    print("금요일")
elif day == '토':
    print("토요일")
elif day == '일':
    print("일요일")
else:
    print("잘못된 입력!")

# if 한줄 표현식
avg = 65

# \는 한줄이라는 것을 알려줌
hak1 = 'A학점' if avg >= 90 else 'B학점' if avg >= 80 else 'C학점' if avg >= 70 else 'D학점' if avg >= 60 else 'F학점'

print('학점 : ', hak1)

hak2 = 'A학점' if avg >= 90 else 'B학점' if avg >= 80 \
    else 'C학점' if avg >= 70 else 'D학점' \
    if avg >= 60 else 'F학점'

print('학점 : ', hak2)

# 점수 계산기
korScore = int(input("국어 점수 입력 :"))
mathScore = int(input("수학 점수 입력 :"))
engScore = int(input("영어 점수 입력 :"))
sciScore = int(input("과학 점수 입력 :"))

total = korScore + mathScore + engScore + sciScore
avr = total / 4

if 90 < avr <= 100:
    grade = "A"
elif 80 < avr <= 90:
    grade = "B"
elif 70 < avr <= 80:
    grade = "C"
elif 60 < avr <= 70:
    grade = "D"
else:
    grade = "F"

print(f"점수의 총합은 {total} 평균 점수는 {avr} 학점은 {grade}")
