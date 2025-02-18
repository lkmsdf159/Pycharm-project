#wb_print.py

class wb_print:
    @staticmethod
    def intro():
        print("="* 50)
        print("회원 관리 프로그램")
        print("="* 50)

    @staticmethod
    def ending():
        print("="* 50)
        print("프로그램을 종료합니다.")
        print("="* 50)

    @staticmethod
    def menu():
        print("="* 50)
        print("[1] insert")
        print("[2] select")
        print("[3] update")
        print("[4] delete")
        print("[5] exit")
        print("[6] print all")
        print("="* 50)
