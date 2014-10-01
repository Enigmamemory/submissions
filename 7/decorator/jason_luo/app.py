from flask import Flask
from flask import render_template, session, redirect, request
from functools import wraps

app = Flask (__name__)
app.secret_key = "touchmybody"

def auth(func, *args, **kwargs):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return func()
        else:
            return index('please log in with pants')
        return wrapper

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="GET":
        return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == "michael" and password == "jackson":
            session['username'] = username
            return index('success')
        else:
            return index('failure')

@app.route('/secret')
@auth
def secret():
    return render_template('secret.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port = 7000)