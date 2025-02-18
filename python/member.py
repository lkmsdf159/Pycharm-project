#member.py

class Member:
    def __init__(self, number, name, phone):
        self.__number = number
        self.__name = name
        self.__phone = phone

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone= phone

    def print(self):
        print(f"{self.__number} - {self.__name} - {self.__phone}")

    def println(self):
        print(f"회원번호 : {self.__number}")
        print(f"이름 : {self.__name}")

