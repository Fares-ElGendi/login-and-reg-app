import mysql.connector
from flask import Flask,request,render_template,session,redirect,url_for,flash
app=Flask(__name__)
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='PROJECT')
mycursor=mydb.cursor()
app.secret_key='k'
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['passwd']
        mycursor.execute('SELECT * FROM ACCOUNTS WHERE email=%s AND password=%s', (email, password))
        account=mycursor.fetchone()
        if account:
            username=account[1]
            session['username']=username
            return redirect(url_for('home'))
        else:
            flash('incorrect email or password')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')
@app.route('/register',methods=['GET','POST'])
def register():
        if request.method=='POST':
            username=request.form['username']
            email=request.form['email']
            password=request.form['password']
            mycursor.execute('SELECT * FROM ACCOUNTS WHERE email=%s AND password=%s ;',(email,password))
            account=mycursor.fetchone()
            if account:
                flash('email already exists')
                return redirect(url_for('register'))
            else:
                mycursor.execute('INSERT INTO ACCOUNTS(username,email,password) VALUES(%s,%s,%s)',(username,email,password))
                flash('registeratin done,please login now')
                return redirect(url_for('login'))
        else:
            return render_template('register.html')
@app.route('/')
def home():
    if 'username' in session:
        username=session['username']
        return render_template('home.html',username=username)
    else:
        return redirect(url_for('login'))

if __name__=='__main__':
    app.run()

