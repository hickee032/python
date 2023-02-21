# 클래스 2
"""
class Car5:
    JIJUM = '신암점'  # 클래스 변수

    def __init__(self, company='기아',
                 color='블랙', model='K7', price='사천만원'):
        self.__company = company
        self.__color = color
        self.__model = model
        self.__price = price

    def showcarinfo(self):
        print('지점 : ', Car5.JIJUM)
        print('제조사 : ', self.__company)
        print('모델 : ', self.__model)
        print('색상 : ', self.__color)
        print('가격 : ', self.__price)

    @staticmethod  # static 메서드는 self를 명시 하지 않아도 된다
    def staric_method(model):
        print(Car5.JIJUM, model)

    @classmethod  # 클래스 메서드는 self가 붙지 않고 cls가 붙는 다
    def class_method(cls, model):
        print(cls.JIJUM, model)


if __name__ == '__main__':
    ca = Car5()
    ca1 = Car5()
    ca.showcarinfo()

    Car5.class_method('그랜저')

    print(id(Car5.class_method('1')))
    print(id(ca.class_method('2')))
    print(id(ca1.class_method('3')))

    print(id(Car5.staric_method('1')))
    print(id(ca.staric_method('2')))
    print(id(ca1.staric_method('3')))

    print(id(ca))
    print(id(ca1))

    Car5.staric_method('제네시스')



# 클래스 변수와 인스턴스 변수가 객체 안에서 어떻게 작동하게 되는 지 예시
class Mycount:
    count = 0  # 클래스 변수 -> 다른 언어와 약간 다르다

    def __init__(self):
        self.__count = 0  # 인스턴스 변수
        self.__count += 1
        print('instance 변수 : ', self.__count)

    @classmethod
    def print_count(cls):
        cls.count += 1
        print('class 변수 : ', cls.count)


if __name__ == '__main__':
    for i in range(5):
        Mycount()  # 계속 새로 객체가 생성되면서 1이 됨
        Mycount.print_count()  # 처음 한번만 실행되어 계속 누적됨
"""
from abc import ABCMeta

# 상속 - 부모 클래스로 부터 물려 받아 재 사용
# 부모 클래스
"""
class Car6:
    JIJUM = '신암점'  # 클래스 변수

    def __init__(self, company='기아',
                 color='블랙', model='K7',  price='사천만원'):
        self.__company = company
        self.__color = color
        self.__model = model
        self.__price = price

    def showcarinfo(self):
        print('지점 : ', Car6.JIJUM)
        print('제조사 : ', self.__company)
        print('모델 : ', self.__model)
        print('색상 : ', self.__color)
        print('가격 : ', self.__price)

    @staticmethod  # static 메서드는 self를 명시 하지 않아도 된다
    def staric_method(model):
        print(Car6.JIJUM, model)

    @classmethod  # 클래스 메서드는 self가 붙지 않고 cls가 붙는 다
    def class_method(cls, model):
        print(cls.JIJUM, model)


# Car6 상속
class Truck(Car6):
    def __init__(self, comapny, model, color, price, ton):
        super().__init__(comapny, color, model, price)
        self.__ton = ton  # 오로지 Truck 안에서 사용할수 있다  ( 상속에서 제외됨 )
        # self._ton 재 사용하기 위해서는 언더바 한개 ( _ ) protected

    # 오버라이딩 -> 재정의
    def showcarinfo(self):
        super().showcarinfo()
        print('최대 적재량 : ', self.__ton)


class Suv(Car6):
    def __init__(self, comapny, model, color, price, engine):
        super().__init__(comapny, color, model, price)
        self.__engine = engine

    # 오버라이딩 -> 재정의
    def showcarinfo(self):
        super().showcarinfo()
        print('엔진 : ', self.__engine)


if __name__ == '__main__':
    tr = Truck('현대', '2.5트럭', '파랑', '4천', '2.5')
    tr.showcarinfo()
    su = Suv('기아', '소렌토', '흰색', '4천', '디젤')
    su.showcarinfo()
"""

# 다중 상속
# C# Java 에서는 사용 X -> 인터페이스
# A 클래스에서 상속 받은 정보인지 B 클래스에서 상속 받은 정보인지 모호해지는 경우가 발생할수도 있다

# 사용 문법
# class 클래스명 ( 부모 클래스 1, 부모 클래스 2):
#    pass

# 추상 클래스 -> 설계도면과 같은 역활을 하는 클래스
# 개인적인 작업보다는 큰 프로젝트 또는 협업과정에서 필요
from abc import *


# from 패키지명 import 함수 또는 *


class Person(metaclass=ABCMeta):  # 추상클래스 사용시 metaclass=ABCMeta 모듈이 필요하다
    @abstractmethod  # @abstractmethod는 반드시 오버라이딩 해야한다
    def speak(self):  # 본체는 정의 하지 않는 다 -> 함수명만 정의
        pass

    @abstractmethod
    def work(self):
        pass


# class Student(Person, metaclass=ABCMeta):
class Stuent(Person):

    def speak(self):
        print('질문')

    def work(self):
        print('공부')


class Teacher(Person):

    def speak(self):
        print('가르치다')

    def work(self):
        print('설명하다')


if __name__ == '__main__':
    obj = [Stuent(), Teacher()]
    for i in obj:
        i.speak()
        i.work()
