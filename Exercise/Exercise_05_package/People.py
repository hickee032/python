class People:
    def __init__(self, name, gender, addr):
        self.__name = name
        self.__gender = gender
        self.__addr = addr

    def print_pinfo(self):
        print('이름 : ', self.__name)
        print('성별 : ', self.__gender)
        print('주소 : ', self.__addr)

    # setter
    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_addr(self, addr):
        self.__addr = addr

    # getter
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_addr(self):
        return self.__addr


class Student(People):
    def __init__(self, job, name, gender, addr, grade, room):
        self.__job = job
        super().__init__(name, gender, addr)
        self.__grade = grade
        self.__room = room

    def print_pinfo(self):
        super().print_pinfo()
        print(f'{ self.__grade}  {self.__room} ')

    def set_grade(self, grade):
        self.__grade = grade

    def set_room(self, room):
        self.__room = room

    def get_grade(self):
        return self.__grade

    def get_room(self):
        return self.__room


class Teacher(People):
    def __init__(self, job, name, gender, addr, subject):
        self.__job = job
        super().__init__(name, gender, addr)
        self.__subject = subject

    def print_pinfo(self):
        super().print_pinfo()
        print('담당 과목 : ', self.__subject)

    def set_subject(self, subject):
        self.__subject = subject

    def get_subject(self):
        return self.__subject
