import hotelBooking_func as hf

hf.create_tbl01()
hf.create_tbl02()

while True:
    menu = input('''
                                  ! Welcome to JH HOTEL !
=============================================================================================
    1. 가입  2. 객실 리스트  3. 예약하기  4. 예약확인  5. 예약취소  6. 요청사항  7. 종료
=============================================================================================
>>>''')

    if menu == '1':
        hf.insert_customer()
    elif menu == '2':
        hf.show_room()
    elif menu =='3':
        pass
    elif menu == '4':
        pass
    elif menu == '5':
        pass
    elif menu == '6':
        pass
    elif menu == '7':
        break
    else:
        print('메뉴를 선택해주세요.')