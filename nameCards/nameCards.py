# 명함관리 프로그램
# - 명함등록 (일련번호, 이름, 전화번호, fax, 회사명)
# - 명함 수정
# - 명함 삭제
# - 리스트 출력
# 종료

import nameCards_func as nf


nf.create_table()
while True:
    menu = input('''
======================================================
  1. 등록   2. 수정   3. 삭제   4. 리스트   5. 종료
======================================================
>>>''')

    if menu == '1':
        nf.insert_card()
    elif menu == '2':
        nf.update_card()
    elif menu == '3':
        nf.delete_card()
    elif menu == '4':
        nf.list_card()
    elif menu == '5':
        break
    else:
        print('정확한 메뉴를 선택하세요')