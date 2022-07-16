import cx_Oracle

#print(cx_Oracle.version)
conn = cx_Oracle.connect('jdbc:oracle:thin:@DB20220609093520_medium?TNS_ADMIN=/Users/jeonghwalee/Wallet_DB20220609093520')
cur =conn.cursor()
sel = 'select * from user_tbl'
cur.execute(sql)
conn.close()