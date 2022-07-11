from genericpath import exists
import pstats
import sqlite3

# 회원 테이블 생성
def create_tbl01():
    con = sqlite3.connect('pythonProject/hotelBooking.db')
    cur = con.cursor()

    cur.execute('''
        create table if not exists customers(
            idx integer primary key,
            cid text,
            pw text,
            name text,
            tel integer,
            birth text,
            gender text
        )
    ''')

    con.commit()
    con.close()

# 객실타입 테이블 생성
def create_tbl02():
    con = sqlite3.connect('pythonProject/hotelBooking.db')
    cur = con.cursor()

    cur.execute('''
        create table if not exists roomType(
            tid text primary key,
            tname text,
            tfull_name text,
            tinfo text,
            price integer
        )
    ''')

    con.commit()
    con.close()

# 객실 리스트 테이블 생성
def create_tbl03():
    con = sqlite3.connect('pythonProject/hotelBooking.db')
    cur = con.cursor()

    cur.execute('''
        create table if not exists roomList(
            lid text primary key,
            lnum_name text,
            tid text,
            status text
        )
    ''')

    con.commit()
    con.close()

# 예약 테이블 생성
def create_tbl04():
    con = sqlite3.connect('pythonProject/hotelBooking.db')
    cur = con.cursor()

    cur.execute('''
        create table if not exists reservation(
            ridx text primary key,
            lidx text,
            cid text,
            cnt_people integer,
            cnt_room integer,
            rdate text,
            tprice integer
        )
    ''')

    con.commit()
    con.close()

# 요청 테이블 생성
def create_tbl05():
    con = sqlite3.connect('pythonProject/hotelBooking.db')
    cur = con.cursor()

    cur.execute('''
        create table if not exists request(
            qidx text primary key,
            cid text,
            ridx text,
            comments text
        )
    ''')

    con.commit()
    con.close()

# 가입 함수
def insert_customer():
    con = sqlite3.connect('pythonProject/hotelBooking.db')
    cur = con.cursor()

    select = input('''
관리자 -> 1  회원 -> 2
>>>''')

    # 관리자
    if select == '1':
        confirm_num = input('관리자 번호 >>>') #관리자 번호는 123 으로 통용

        if confirm_num == '123':
            menuSel = input('''
==========================================================
                    고객 관리 페이지
    1. 리스트   2. 수정    3. 삭제    5. 종료 시 Enter
==========================================================
>>>''')
            # 리스트
            if menuSel == '1':
                showData = input('전체 리스트 -> 1  상세 검색 -> 2 >>>')
                
                # 전체 리스트
                if showData == '1':
                    cur.execute('select idx, cid, pw, name, tel, birth, gender from customers')
                    data = cur.fetchall()
                    for list in data:
                        print(f'회원이름 : {list[3]} || 회원아이디 : {list[1]} || 비밀번호 : {list[2]} || 전화번호 : {list[4]} || 생년월일 : {list[5]} || 성별 : {list[6]}')

                # 상세 검색
                elif showData == '2':
                    col = input('''
항목 검색 (회원아이디 : cid, 이름 : name, 전화번호 : tel)
>>>''')
                    value = input('검색 내용 >>>')
                    
                    sql = f'select idx, cid, pw, name, tel, birth, gender from customers where {col} like ?'
                    data = cur.execute(sql,('%' + value + '%',))
                    
                    for list in data:
                        print(f'회원이름 : {list[3]} || 회원아이디 : {list[1]} || 비밀번호 : {list[2]} || 전화번호 : {list[4]} || 생년월일 : {list[5]} || 성별 : {list[6]}')

            # 수정
            elif menuSel == '2':
                cid = input('수정할 회원 아이디 >>>')

                # 회원 아이디 존재 확인
                cur.execute('select exists(select cid from customers where cid = ?)',(cid,))
                if cur.fetchone()[0]:
                    col = input('수정할 항목(pw, name, tel) >>>')
                    value = input('수정할 내용 >>>')

                    sql = f'update customers set {col} = ? where cid = ?'
                    cur.execute(sql,(value,cid))
                    print(cid + ' 님의 데이터가 수정되었습니다.')

                    con.commit()
                else:
                    print('존재하지 않는 회원 아이디입니다.')

            # 삭제
            elif menuSel == '3':
                cid = input('삭제할 회원 아이디 >>>')
                # 회원 아이디 존재 확인
                cur.execute('select exists(select cid from customers where cid = ?)',(cid,))
                if cur.fetchone()[0]:
                    
                    confirm = input('영구적으로 삭제 됩니다. 삭제하시겠습니까? Y/N >>>')
                    a = confirm.upper()
                    
                    if a == 'Y':
                        sql = f'delete from customers where cid = ?'
                        cur.execute(sql,(cid,))
                        print(cid + ' 님의 정보가 성공적으로 삭제됐습니다.')
                        
                        con.commit()

                    elif a == 'N':
                        print('삭제 실패')
                    
                    else:
                        print('선택이 완료되지 않았습니다.')
                else:
                    print('존재하지 않는 회원 아이디입니다.')
                    

            else:
                print('항목을 선택하세요.')
        
        else:
            print('관리자 권한이 없습니다. 문의 051-222-2222')

    # 고객 회원가입
    elif select == '2':
        cid = input('아이디 : ')
        #chkID = f'select cid from customers where cid = ?'
        
        #for a in cur.execute(chkID,(cid,)):
            #b = a[0]
            #if b is True:
        cur.execute('select exists(select cid from customers where cid = ?)',(cid,))
        if cur.fetchone()[0]:
            print('이미 존재하는 아이디입니다.')
        else:
            pw = input('비밀번호 : ')
            name = input('이름 : ')
            tel = input('전화번호 : ')
            birth = input('생년월일 (0000-00-00) : ')
            gender = input('성별 (남 - M, 여 - F) : ')
            inGender = gender
            inGender.upper()

            data  = (cid, pw, name, tel, birth, gender)
            sql = '''insert into customers(cid, pw, name, tel, birth, gender) 
                    values(?, ?, ?, ?, ?, ?)
            '''

            print('''
   ᕱ ᕱ
♡ (•ˬ•) ♡ 반갑습니다. ''' + name + ' 님!')

            cur.execute(sql, data)
            con.commit()
            

    else:
        print('항목을 선택하세요.')

    
    con.close()

# 객실 리스트 함수
def show_room():
    con = sqlite3.connect('pythonProject/hotelBooking.db')
    cur = con.cursor()

    select = input('''
관리자 -> 1  회원 -> 2
>>>''')

    if select == '1':
        confirm_num = input('관리자 번호 >>>') #관리자 번호는 123 으로 통용

        if confirm_num == '123':
            sel_menu = input('''
==========================================================
                객실 관리 페이지
        1. 객실 타입     2. 객실 리스트
==========================================================
>>>''')
            #객실 타입 메뉴
            if sel_menu == '1':
                type_menu = input('''
==========================================================
                객실 타입 관리 페이지
  1. 리스트   2. 추가    3. 수정    4. 삭제    5. 종료 시 Enter
==========================================================
                ''')
                # 객실 타입 리스트
                if type_menu == '1':
                    cur.execute(tid, tname, tfull_name, tinfo, price)
                    data = cur.fetchall()
                    for list in data:
                        print(f'객실 타입 번호 : {list[0]} || 객실 타입 : {list[1]} || 풀 네임 : {list[2]} || 객실 정보 : {list[3]} || 객단가 : {list[4]}')
                
                # 객실 타입 추가
                if type_menu == '2':
                    tid = input('객실타입 번호 >>>')
                    tname = input('객실 타입 >>>')
                    tfull_name = input('객실 타입 풀네임 >>>')
                    tinfo = input('객실 정보 >>>')
                    price = input('객단가 >>>')

                    data = (tid, tname, tfull_name, tinfo, price)
                    sql = 'insert into roomType values(?, ?, ?, ?, ?)'

                    cur.execute(sql, data)

                    con.commit()
                
                #객실 타입 수정
                if type_menu == '3':
                    tid = input('객실타입 번호 >>>')
                    cur.execute('select exists(select tid from roomType where tid = ?)',(tid,))
                    if cur.fetchone()[0]:
                        col = input('수정할 항목(tname, tfull_name, tinfo, price) >>>')
                        value = input('수정할 내용 >>>')

                        sql = f'update roomType set {col} = ? where tid = ?'
                        cur.execute(sql,(value,tid))

                        con.commit()

                # 객실 타입 삭제
                if type_menu == '4':
                    tid = input('객실타입 번호 >>>')
                    cur.execute('select exists(select tid from roomType where tid = ?)',(tid,))
                    if cur.fetchone()[0]:
                        confirm = input('영구적으로 삭제 됩니다. 삭제하시겠습니까? Y/N >>>')
                        a = confirm.upper()
                        
                        if a == 'Y':
                            sql = f'delete from roomType where tid = ?'
                            cur.execute(sql,(tid,))
                            print('해당 정보가 성공적으로 삭제됐습니다.')
                            
                            con.commit()

                        elif a == 'N':
                            print('삭제 실패')
                        
                        else:
                            print('선택이 완료되지 않았습니다.')
            
            #객실 리스트 추가
            elif sel_menu == '2':
                lid = input('객실리스트 번호 >>>')
                lnum_name = input('객실 번호 >>>')
                tid = input('객실타입 번호 >>>')
                status = input('객실 상태(입실O, 정비전NH, 정비후FH) >>>')
                # O - occupied, NH - needHouseKeeping, FH - finishHouseKeeping

                data = (lid, lnum_name, tid, status)
                sql = 'insert into roomList values(?, ?, ?, ?)'

                cur.execute(sql, data)

                con.commit()
                con.close()

            else:
                print('항목을 선택해주세요.')
        else:
            print('관리자 권한이 없습니다. 문의 051-222-2222')
        
    elif select == '2':
        
        cur.execute('select tname, tfull_name, tinfo, price from roomType')
        data = cur.fetchall()
        for list in data:
            print(f'객실 타입 : {list[1]} || 소개 : {list[2]} || 가격 : {list[3]}')
                

    else:
        print('항목을 선택해주세요.')

    con.close()