from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = { "apiKey": "AIzaSyBB7hDFG0Y7IJzzm_rfl0Kj-F0IHth369I",
 "authDomain": "hamza-f5495.firebaseapp.com",
  "projectId": "hamza-f5495",
  "storageBucket": "hamza-f5495.appspot.com",
  "messagingSenderId": "351714997588",
  "appId": "1:351714997588:web:4f1b4d7557a8b3c83f04c1",
 "databaseURL":""}

firebase = pyrebase.initialize_app(config)
auth=firebase.auth()


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error =""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('abb_tweet.html'))
        except:
            error = "Authentication failed"
    return render_template("add_tweet.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
   
   return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)