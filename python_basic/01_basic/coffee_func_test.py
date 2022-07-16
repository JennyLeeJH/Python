# # 커피자판기
# 1. 커피자판기 2. 메뉴추가 3.메뉴삭제 4.메뉴목록 5.종료
# - 프로그램이 시작될때 필요한 정보를 읽어서 시작합니다.
# - 커피자판기 무한반복하면서 돈을 입력받고, 메뉴를 선택해서 처리
# - 메뉴추가 자판기에서 판매하는 메뉴를 추가하는 기능(메뉴명,가격)
# - 메뉴삭제는 전체 목록을 보여주고 삭제하고자하는 항목을 선택하도록 해서 삭제 처리
# - 메뉴목록은 메뉴이름순,메뉴가격순으로 정렬해서 보여줌.
# - 종료는 메뉴 정보를 저장하고 종료합니다.

import coffee_func as cf

item = cf.data_load('python_basic/01_basic/item.json')
menu_display = '''
----------------------------------------------------------
1. 커피자판기    2. 메뉴추가    3. 메뉴삭제   4. 메뉴목록    5. 종료
==========================================================
>>> '''

#무한반복 되도록
while True:
    menu = input(menu_display)
    if menu == '1':
        cf.coffe_m(item)
    elif menu == '2':
        cf.ins_m(item)
    elif menu == '3':
        cf.del_m(item)
    elif menu == '4':
        cf.list_m(item)
    elif menu == '5':
        cf.data_save('python_basic/01_basic/item.json', item)
        break
    else:
        print('정확한 메뉴를 선택해주세요')