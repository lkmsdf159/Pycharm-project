#start.py
from wb_print import wb_print
from wb_ui import WbUI

data = WbUI()

def init():
    wb_print.intro()
    pass

def exit():
    wb_print.ending()
    pass

def run():
    while True:
        wb_print.menu()
        sel = input("메뉴 선택 : ")
        if sel == "5": break
        elif sel == "1": data.member_insert()
        elif sel == "2": data.member_select()
        elif sel == "3": data.member_update()
        elif sel == "4": data.member_delete()
        elif sel == "6": data.member_printall()
    pass

if __name__ == "__main__":
    init()
    run()
    exit()

