from flask import Flask, request, redirect, render_template
import sqlite3, os

app = Flask(__name__)
path = os.path.dirname(__file__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inputform', methods=['GET','POST'])
def inputform():
    if request.method == 'GET':
        return render_template('inputform.html')
    else:
        #db에 데이터 입력
        con = sqlite3.connect(path + '/customer.db')
        cur = con.cursor()
        cur.execute('''
            create table if not exists customer(
                name text,
                email text,
                tel text,
                address text,
                gender text
            )
        ''')
        con.commit()
        data = [request.form['name'],request.form['email'],request.form['tel'],request.form['address'],request.form['gender']]
        cur.execute('insert into customer values(?,?,?,?,?)',data)
        con.commit()
        con.close()
        return redirect('/')

@app.route('/customerlist')
def customerlist():
    con = sqlite3.connect(path + '/customer.db')
    cur = con.cursor()
    cur.execute('select * from customer order by name asc')
    data = cur.fetchall()
    return render_template('customerlist.html', data=data) # data=data data 라는 이름으로 data를 전달

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=80)