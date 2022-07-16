import sqlite3

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor() #connection 객체를 통해서 cursor를 받아온다.

symbol = 'RHAT' #symbol 이라는 변수에 'RHAT' 선언
cur.execute('select * from stocks')
data = cur.fetchall() #fetchall 은 전부 다 ~~!!~!
for item in data:
    print(item)

conn.close()