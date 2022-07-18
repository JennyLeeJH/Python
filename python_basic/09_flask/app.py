from flask import Flask, redirect, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return '유저 호출!'

#url 값으로 보내는 것
@app.route('/user/<username>/<int:age>') #url에서 선언한 함수는 반드시 안에서 호출해줘야한다. 기본 String으로 리턴!
def user_1(username,age): #() 안은 매개변수 선언
    return f'{username} 고객님의 나이는 {age+1}살 입니다.'

#get 방식의 request 쿼리 방식, get방식으로 한다는게 디폴트값이다. ? 적고 쿼리 적어서 주소 완성 -> /customer?user=jeong&age=27
@app.route('/customer')
def customer():
    print('user:',request.args.get('user'))
    print('age:',request.args.get('age'))
    return "customer 호출!"

@app.route('/login',methods=['GET','POST']) # get 과 post 방식 둘 다 사용 하기에 적어줘야 함! 안적으면 위와 같이 디폴트값인 get!
def login():
    # GET 방식 agrs에서 찾고
    if request.method == 'GET':
        return render_template("form_input.html")
    # POST 방식 from에서 찾는다.
    else:
        #return f"로그인: {request.form['username']} {request.form['password']}"
        return render_template("form_result.html",result = request.form)

@app.route('/fileupload',methods=['GET','POST'])
def fileupload():
    if request.method == 'GET':
        return render_template('fileupload.html')
    else:
        f = request.files['file']
        path = os.path.dirname(__file__) + '/upload/' + f.filename #__file__ 현재 파일이라는 뜻, f.filename f에 넣는 file 객체의 이름
        print(path)
        f.save(path)
        return redirect('/') #실행 후 루트로 이동

if __name__ == '__main__': # __ 는 해당 파일이 실행될 대 main이 들어가 있다. 누군가 import 했을시 실행되지 않도록 하는 것
    app.run(host="0.0.0.0",port=80,debug=True)