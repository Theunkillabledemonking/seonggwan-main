menu_list = ['피자', '파스타', '샐러드', '스시', '버거']
sel_menu = int(input("메뉴의 번호를 입력하세요 : "))

while not 0 <= sel_menu <= len(menu_list):
    sel_menu = int(input(f"유효하지 않은 선택입니다. \n(0~{len(menu_list)}) 메뉴 번호를 선택하세요"))
print(F"선택된 메뉴 : {menu_list[sel_menu]}")