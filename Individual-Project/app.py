from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

#Code goes below here
config = {
  "apiKey": "AIzaSyCnAgeMfkX34Q5ifWOoKwcKnT9Pyovl8p0",
  "authDomain": "cs-project-70a34.firebaseapp.com",
  "projectId": "cs-project-70a34",
  "storageBucket": "cs-project-70a34.appspot.com",
  "messagingSenderId": "550123576517",
  "appId": "1:550123576517:web:36e1f4a192f1f3cb0d64ac",
  "measurementId": "G-F8EKFGC9V3",
  "databaseURL" :"https://cs-project-70a34-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        username = request.form['username']
        bio= request.form['bio']
        try:


            login_session['user'] = auth.create_user_with_email_and_password(email, password)
           
            user = {"name": name, "email": email, "password":password,"username":username,"bio":bio}
            db.child("Users").child(login_session['user']['localId']).set(user)



            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            return error
    else:
        return render_template("signup.html")







@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            return  error
    else: 
        return render_template("signin.html")


@app.route('/product')
def product():
    error = ""
    if request.method == 'POST':
        try:
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    else: 
        return render_template("product.html")


@app.route('/cart')
def cart():
    error = ""
    if request.method == 'POST':
        try:
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    else: 
        return render_template("cart.html")

@app.route('/about')
def about():
    error = ""
    if request.method == 'POST':
        try:
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
    else: 
        return render_template("about.html")




@app.route('/home')
def home():
    user=db.child("Users").child(login_session['user']['localId']).get().val() 
    return render_template("index.html",user= user)



if __name__ == '__main__':
    app.run(debug=True)