# 1 ~ 2 자동차 클래스 작성 - 제조사 색상 가격 모델명
"""
class Car:
    def __init__(self, company='기아', model='K7', color='블랙', price='사천'):
        self.__company = company
        self.__model = model
        self.__color = color
        self.__price = price

    def car_info(self):
        print('회사 : ', self.__company, end=' ')
        print('모델 : ', self.__model, end=' ')
        print('색상 : ', self.__color, end=' ')
        print('가격 : ', self.__price, end=' ')

    def car_name(self, name):
        self.__model = name

    #getter
    @property
    def price(self):
        return self.__price

    #setter
    @price setter
    def price(self,new_price):
        self.__price = new_price

if __name__ == '__main__':
    ca1 = Car('현대', '그랜저', '흰색', '4천')
    ca1.car_info()
    ca2 = Car()

    ca2.car_info()
    ca3 = Car()

    ca3.car_name('몰라')
    ca3.car_info()

    ca3.price = '3천만'
"""
import random

# 3 배열의 합과 평균
"""
class Sumavr:
    def __init__(self, arr):
        self.__arr = arr

    def printlist(self):
        print(self.__arr)

    def sumavrarr(self):
        reslist = []
        total = 0
        avr = 0
        for i in range(len(self.__arr)):
            total += self.__arr[i]

        avr = int(total / len(self.__arr))
        reslist.append(total)
        reslist.append(avr)

        return reslist


if __name__ == '__main__':
    numlist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    sa = sumavr(numlist)
    result = sa.sumavrarr()
    print(f'총합은 {result[0]} 평균은 {result[1]}')
"""


# 4 학점을 출력하는 클래스
"""
class Student:
    def __init__(self, scorelist):
        self.__scorelist = scorelist
        self.__totallist = []
        self.__avrlist = []
        self.__gradelist = []

    # 총합
    def total(self):
        total = 0

        for i in range(len(self.__scorelist)):  # 5
            for j in range(len(self.__scorelist[i])):
                total += self.__scorelist[i][j]
            self.__totallist.append(total)
            total = 0
        return self.__totallist

    def avr(self):
        avr = 0
        for i in range(len(self.__totallist)):
            avr = self.__totallist[i] / 3

            self.__avrlist.append(avr)
        return self.__avrlist

    def grade(self):
        for i in range(len(self.__avrlist)):
            if 90 < self.__avrlist[i] <= 100:
                self.__gradelist.append('A')
            elif 80 < self.__avrlist[i] <= 90:
                self.__gradelist.append('B')
            elif 70 < self.__avrlist[i] <= 80:
                self.__gradelist.append('C')
            elif 60 < self.__avrlist[i] <= 70:
                self.__gradelist.append('D')
            else:
                self.__gradelist.append('F')
        return self.__gradelist


if __name__ == '__main__':
    row, col = 3, 5
    jumsulist = [[random.randint(50, 101) for i in range(row)] for j in range(col)]

    print(jumsulist)

    st = Student(jumsulist)
    totallist = st.total()
    avrlist = st.avr()
    gradelist = st.grade()

    for i in range(len(totallist)):
        print(f'학생 {i+1} 의 총합은 {totallist[i]} 평균은 {avrlist[i]:.2f} 학점은 {gradelist[i]}')
    """

# 5 ~ 7 랜덤하게 이름을 생성 파일에 쓰고 읽기
"""
class NameData:
    def __init__(self, first, mid, last):
        self.__first = first
        self.__mid = mid
        self.__last = last
        self.__numList = []
        self.__namelist = []
        self.__name = ''

    # 랜덤 이름 생성
    def createname(self, num):

        for j in range(num + 1):
            self.__namelist.append(self.__first[random.randint(0, len(self.__first) - 1)]
                                   + self.__mid[random.randint(0, len(self.__first) - 1)]
                                   + self.__last[random.randint(0, len(self.__first) - 1)])

        return self.__namelist

    def writefile(self, nmlist):
        lines = nmlist
        try:
            with open('name.txt', 'w') as f:
                for line in lines:
                    f.write(line+'/')
        except FileNotFoundError as err:
            print('파일 쓰기 오류')

    def readfile(self, fileroute):
        try:
            with open(fileroute, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    print(line)
        except FileNotFoundError as err:
            print('파일 읽기 오류')


if __name__ == '__main__':
    fir = ['김', '나', '박', '이', '최']
    sec = ['가', '나', '다', '라', '마']
    thr = ['바', '사', '아', '자', '차']

    nd = NameData(fir, sec, thr)
    namelist = nd.createname(50)
    print(namelist)
    nd.writefile(namelist)
    nd.readfile('name.txt')
"""

# 학생 클래스
"""
class Student:
    def __init__(self, name, age, gender, addr):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__addr = addr

    def std_info(self):
        print('이름 : ', self.__name, end='\n')
        print('나이 : ', self.__age, end='\n')
        print('성별 : ', self.__gender, end='\n')
        print('주소 : ', self.__addr, end='\n')


if __name__ == '__main__':
    name = ['홍길동', '김길동', '박길동', '이길동', '최길동']
    age = [20, 25, 30, 35, 40]
    gender = ['남', '여']
    addr = ['서울', '부산', '대구', '인천', '전주']

    stud = [Student(name[random.randint(0, len(name) - 1)],
                    age[random.randint(0, len(age) - 1)],
                    gender[random.randint(0, len(gender) - 1)],
                    addr[random.randint(0, len(addr) - 1)]) for i in range(11)]

    for i in range(len(stud)):
        print(f'{i}번 학생')
        stud[i].std_info()
        print('-----------')
"""


# 고객 차량 관리 서비스
class Car:
    def __init__(self, model1, color1, year1, company1):
        self.__model = model1
        self.__color = color1
        self.__year = year1
        self.__company = company1

    def print_carinfo(self):
        print('모델 : ', self.__model)
        print('색상 : ', self.__color)
        print('연도 : ', self.__year)
        print('제조 : ', self.__company)


class Customer:
    def __init__(self, name1, tel1, addr1, car):
        self.__name = name1
        self.__tel = tel1
        self.__addr = addr1
        self.Car = car

    def print_costomerinfo(self):

        print('이름 : ', self.__name)
        print('연락처 : ', self.__tel)
        print('주소 : ', self.__addr)
        self.Car.print_carinfo()


if __name__ == '__main__':
    name = ['홍길동', '김길동', '박길동', '이길동', '최길동']
    tel = ['1234', '5678', '91011', '1213', '1415']
    addr = ['서울', '부산', '대구', '인천', '전주']

    model = ['SM6', '소나타', '산타페', 'K7', '그랜저']
    color = ['blue', 'red', 'white', 'black', 'gray']
    year = [1700, 1800, 1900, 2000, 2100]
    company = ['야쿠르트', '디즈니', '뽀로로', '짱구', '모닝글로리']

    customerlist = [Customer(name[random.randint(0, len(name) - 1)],
                             tel[random.randint(0, len(tel) - 1)],
                             addr[random.randint(0, len(addr) - 1)],
                             Car(
                                 model[random.randint(0, len(model) - 1)],
                                 color[random.randint(0, len(color) - 1)],
                                 year[random.randint(0, len(year) - 1)],
                                 company[random.randint(0, len(company) - 1)]))for i in range(11)]

    for i in range(len(customerlist)):

        customerlist[i].print_costomerinfo()
        print('-----------------------')