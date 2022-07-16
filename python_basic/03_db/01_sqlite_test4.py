import sqlite3

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor() #connection 객체를 통해서 cursor를 받아온다.

keyword = input('검색어 >>>')
sql = 'select * from stocks where symbol = ?'

cur.execute(sql,(keyword,))

data = cur.fetchall() #fetchall 로 해당되는 것들을 data에 저장
for i in data :
        print(i)
conn.close()