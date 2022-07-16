import sqlite3

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor() #connection 객체를 통해서 cursor를 받아온다.

data = [('2006-03-28', 'BUY', 'IBM', 300.0, 45.14),
        ('2006-04-05', 'BUY', 'MSFT', 1000.0, 76.00),
        ('2006-04-06', 'SELL', 'IBM', 500.0, 290.14)] #리스트 안에 리스트로 해도 상관없다. 현재는 튜플로!
sql = 'insert into stocks values(?,?,?,?,?)'

cur.executemany(sql,data) #동작을 여러번 실행시킬 경우에 executemany 사용
conn.commit()
conn.close()