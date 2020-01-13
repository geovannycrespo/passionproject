from spartanrace import app,db 
from flask import render_template,request, redirect, url_for   
from spartanrace.forms import SignupForm,LoginForm,PostForm

# From Werkzeug for Security import
from werkzeug.security import check_password_hash

# Import for flask-login
from flask_login import login_user, current_user, login_required

# User Model Import
from spartanrace.models import User,Post

#home route
@app.route("/")
def home():
    # Display posts for logged in user
    posts = Post.query.all()
    return render_template("home.html", post = posts)

 # Sing up Route
@app.route("/signup",methods=["GET","POST"])
def signup():
    signupForm = SignupForm()
    if request.method == 'POST':
        username = signupForm.username.data
        email = signupForm.email.data
        password = signupForm.password.data
        print(username,email,password)

        # Add Form data to user Model Class(AKA DATABASE)
        # First - Import User Model(Above)
        # Second - open a database session, then add our data
        # Last - Commit data and close the session for the database

        user = User(username,email,password)
        db.session.add(user) # Start Communication with database
        db.session.commit() # Save Data to database and close session


    return render_template("signup.html", signupform = signupForm)

# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if request.method == "POST":
        user_email = loginForm.email.data
        password = loginForm.password.data
        # find out who the logged in user currently is
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))
        else:
            print("Not Valid Method")
    return render_template("login.html", loginform = loginForm)

@app.route("/post", methods = ["GET", "POST"])
@login_required
def post():
    postForm = PostForm()
    title = postForm.title.data
    content = postForm.content.data
    user_id = current_user.id 
    print(title,content,user_id)

    # saving post data to database
    post = Post(title = title, content = content, user_id = user_id)
    db.session.add(post)
    db.session.commit()

    return render_template('create_post.html', postform = postForm)

@app.route("/signup",methods=["GET","POST"])
def fivek():
    signupForm = SignupForm()
    if request.method == 'POST':
        username = signupForm.username.data
        email = signupForm.email.data
        password = signupForm.password.data
        print(username,email,password)

        # Add Form data to user Model Class(AKA DATABASE)
        # First - Import User Model(Above)
        # Second - open a database session, then add our data
        # Last - Commit data and close the session for the database

        user = User(username,email,password)
        db.session.add(user) # Start Communication with database
        db.session.commit() # Save Data to database and close session


    return render_template("signup.html", signupformtwo = signupForm)

