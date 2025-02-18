#wb_ui.py

from member_control import MemberControl

class WbUI:
    mc = MemberControl()

    def __init__(self):
        pass

    def member_insert(self):
        number = int(input("회원번호 : "))
        name = input("회원이름 : ")
        phone = input("회원전화번호 : ")

        if self.mc.insert(number, name, phone):
            print("회원가입 성공")
        else:
            print("회원가입 실패")

    def member_select(self):
        number = int(input("회원번호 : "))

        member = self.mc.select(number)
        member.println()



    def member_update(self):
        number = int(input("회원번호 : "))
        phone = input("전화번호 : ")

        self.mc.update(number, phone)
        print("전화번호 수정 성공")

    def member_delete(self):
        number = int(input("회원번호 : "))
        self.mc.delete(number)
        print("회원 삭제")

    def member_printall(self):
        members = self.mc.members
        for member in members:
            member.print()
