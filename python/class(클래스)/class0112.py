# 클래스 - 객체지향 프로그래밍(OOP)
# class Car1:
#     def carInfoShow(self):
#         print('회사:', '현대')
#         print('모델:', '그랜저')
#         print('색상:', '회색')
#         print('가격:', '4천만원')
#
# if __name__ == '__main__':
#     ca = Car1() # Car1 클래스 객체 생성
#     ca.carInfoShow()

# class Car2:
#     def __init__(self): # 생성자 역활
#         self.company = '현대' # public 인스턴스 변수 선언
#         self.model = '그랜저'
#         self.color = '흰색'
#         self.price = '4천만원'
#
# if __name__ == '__main__':
#     ca = Car2() # Car2 클래스 객체 생성
#     print('회사:', ca.company) # 캡슐화 위배
#     print('모델:', ca.model)

# class Car3:
#     def __init__(self):  # 기본 생성자 역활
#         self.__company = '현대' # private
#         self.__model = '그랜저'
#         self.__color = '흰색'
#         self.__price = '4천만원'
#
#     def carInfoShow(self):
#         print('회사:', self.__company)
#         print('모델:', self.__model)
#         print('색상:', self.__color)
#         print('가격:', self.__price)
#
# if __name__ == '__main__':
#     ca = Car3()
#     ca.carInfoShow()

# class Car4:
#     def __init__(self, company, model, color, price):
#         self.__company = company
#         self.__model = model
#         self.__color = color
#         self.__price = price
#
#     def carInfoShow(self):
#         print('회사:', self.__company)
#         print('모델:', self.__model)
#         print('색상:', self.__color)
#         print('가격:', self.__price)
#
# if __name__ == '__main__':
#     ca = Car4('현대', '그랜저', '검정', '4천만원')
#     ca.carInfoShow()

# class CarEx:
#     # python 오버로딩(중복정의) 지원 X
#     def __init__(self, company='기아',
#                  color='블랙', model='K7', price='사천만원'):
#         self.__company = company
#         self.__color = color
#         self.__model = model
#         self.__price = price
#
#     def showCarInfo(self):
#         print('제조사:', self.__company)
#         print('모델:', self.__model)
#         print('색상:', self.__color)
#         print('가격:', self.__price)
#
#     def setModel(self, model):
#         self.__model = model
#
#     def getModel(self):
#         return self.__model
#
#     # getter : decorator
#     @property
#     def price(self):
#         return self.__price
#
#     # setter
#     @price.setter  # @price.setter 와 함수 price 의 이름은 일치 시켜야한다
#     def price(self, new_price):
#         self.__price = new_price
#
# if __name__ == '__main__':
#     ca = CarEx()
#     ca.showCarInfo()
#     ca2 = CarEx('현대', '그랜저', '검정', '4천만원')
#     ca2.showCarInfo()
#     ca2.setModel('제네시스')
#     print('변경된 모델:', ca2.getModel())
#     ca2.price = '6천만원'
#     print('변경된 가격:', ca2.price)


from functools import reduce
class ArrHap:
    def __init__(self, arr_n):
        self.__hap = reduce(lambda x, y: x + y, arr_n)
        self.__avg = self.__hap / len(arr_n)

    def getHap(self):
        return self.__hap

    def getAvg(self):
        return self.__avg

if __name__ == '__main__':
    arr = [n for n in range(10, 110, 10)]
    ar = ArrHap(arr)
    print(f'합:{ar.getHap()}, 평균:{ar.getAvg()}')
