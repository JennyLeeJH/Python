import hotelBooking_func as hf

hf.create_tbl01()
hf.create_tbl02()
hf.create_tbl03()

while True:
    menu = input('''
                       ! Welcome to JH HOTEL !
====================================================================
        1. 가입  2. 객실 타입  3. 예약  4. 문의  5. 종료
====================================================================
>>>''')

    if menu == '1':
        hf.insert_customer()
    elif menu == '2':
        hf.show_room()
    elif menu =='3':
        hf.reservation()
    elif menu == '4':
        print('''
   ᕱ    ᕱ                                         ᕱ     ᕱ
(  ˵•́ ᴗ •̀˵) 문의 사항은 3333-5555 로 전화주세요. (˵•́ ᴗ •̀˵  )''')
    elif menu == '5':
        break
    else:
        print('메뉴를 선택해주세요.')

        