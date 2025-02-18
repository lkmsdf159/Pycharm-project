#member_control.py

from member import Member

class MemberControl:
    def __init__(self):
        self.__members = list()

    @property
    def members(self):
        return self.__members

    def insert(self, number, name, phone):
        member = Member(number, name, phone)
        self.__members.append(member)
        return True

    def select(self, number):
        for member in self.__members:
            if member.number == number:
                return member

    def update(self, number, phone):
        member = self.select(number)
        member.phone = phone
        return True

    def delete(self, number):
        member = self.select(number)
        self.__members.remove(member)
        return True