import sqlite3

# table 생성
def create_table():
    con = sqlite3.connect('pythondata/nameCards/nameCards.db') #nameCard 자체에서 하면 루트가 다르기에 수정필!!!
    cur = con.cursor()

    cur.execute('''
    create table if not exists nameCards(
        idx integer,
        name text,
        tel integer,
        fax integer,
        company text
    )
    ''')

    con.commit()
    con.close()

# 명함 등록
def insert_card():
    con = sqlite3.connect('pythondata/nameCards/nameCards.db')
    cur = con.cursor()
    
    idx = input('일련번호 >>> ')
    name = input('이름 >>> ')
    tel = input('전화번호 (\'-\'을 제외하고 입력하세요) >>> ')
    fax = input('fax번호 (\'-\'을 제외하고 입력하세요) >>> ')
    company = input('회사명 >>> ')

    data = (idx, name, tel, fax, company)
    sql = 'insert into nameCards values(?, ?, ?, ?, ?)'

    cur.execute(sql, data)
    con.commit()
    con.close()

# 명함 수정
def update_card():
    con = sqlite3.connect('pythondata/nameCards/nameCards.db')
    cur = con.cursor()

    choice = '수정 선택'
    while choice:
        # 리스트 보여주기
        cur.execute('select * from nameCards')
        data = cur.fetchall()
        for list in data:
            print(list)

        #수정 진행
        idx = input('수정할 목록 번호 (종료:Enter) >>> ')
        if idx == '':
            break
        col = input('수정할 항목 (name, tel, fax, company) >>> ')
        value = input('수정할 내용 >>> ')

        sql = f'update nameCards set {col} = ? where idx = ?'
        cur.execute(sql,(value,idx))
    
    con.commit()
    con.close()

# 명함 삭제
def delete_card():
    con = sqlite3.connect('pythondata/nameCards/nameCards.db')
    cur = con.cursor()

    choice = '삭제 선택'
    while choice:
        # 리스트 보여주기
        cur.execute('select * from nameCards')
        data = cur.fetchall()
        for list in data:
            print(list)

        #삭제 진행
        col = input('삭제할 컬럼 (종료:Enter) >>> ')
        if col == '':
            break
        value = input('삭제할 데이터 정보 >>> ')

        sql = f'delete from nameCards where {col} like ?'
        cur.execute(sql,('%' + value + '%',))
        
    con.commit()
    con.close()

# 명함 리스트
def list_card():
    con = sqlite3.connect('pythondata/nameCards/nameCards.db')
    cur = con.cursor()

    cur.execute('select * from nameCards')
    data = cur.fetchall()
    for list in data:
        print(f'이름 : {list[1]} | 연락처 : {list[2]} | fax : {list[3]} | 회사명 : {list[4]}')

    con.close()
