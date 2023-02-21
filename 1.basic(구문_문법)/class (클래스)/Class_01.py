# 클래스 - 객테 지향 프로그래밍 oop
"""
class Car1:
    # 클래스 멤버 메소드 ( 인스턴스 메소드 )
    def carinfoshow(self):  # self 반드시 명시 해야한다 C# 에서의 this 의 개념 C#에서는 생략가능 하지만 파이썬은 생략 불가
    # 인스턴스 메소스는 self가 반드시 필요 (Car1 객체를 생성할때 Car1 객체의 주소값(?))
        print('회사 : ', '현대')
        print('모델 : ', '그랜저')
        print('색상 : ', '회색')
        print('가격 : ', '4천')


if __name__ == '__main__':
    ca = Car1()  # 클래스 객체 생성  !!주의 new가 생략됨  생성자가 없고 생성자 역활을 하는 것이 별도로 존재
    # 내부 가비지 컬렉터 존재
    ca.carinfoshow()


class Car2:
    def __init__(self):  # 생성자 역활
        self.company = '현대'  # 인스턴스 변수 선언
        self.model = '그랜저'
        self.color = '검정'
        self.price = '4천'


if __name__ == '__main__':
    ca = Car2()  # Car2 클래스 객체 생성
    print('회사 :', ca.company)  # 캡슐화에 위배  public 상태
    print('모델 :', ca.model)
    print('색상 :', ca.color)
    print('가격 :', ca.price)

# 위 코드는 캡슐화 위배된다 (객체 지향 의미)



class Car3:
    # 앞에 __ 두개가 붙으면 private _ 한개면 protected 없으면 public
    def __init__(self):
        self.__company = '현대'
        self.__model = '그랜저'
        self.__color = '검정'
        self.__price = '4천'

    def carinfoshow(self):
        print('회사 : ', self.__company)
        print('모델 : ', self.__model)
        print('색상 : ', self.__color)
        print('가격 : ', self.__price)


if __name__ == '__main__':
    ca = Car3()
    ca.carinfoshow()
"""


class Car4:
    # 매개변수가 있는 생성자 -> 첫번째 매개변수는 반드시 self 여야만 한다
    # 오버로딩을 지원하지 않는 다 -> 가변인자 디폴트 인자 를 사용한다
    def __init__(self, company, model, color, price):
        self.__company = company
        self.__model = model
        self.__color = color
        self.__price = price

    def carinfoshow(self):
        print('회사 : ', self.__company)
        print('모델 : ', self.__model)
        print('색상 : ', self.__color)
        print('가격 : ', self.__price)


if __name__ == '__main__':
    ca = Car4('현대', '그랜저1', '흰색', '4천')
    ca.carinfoshow()
