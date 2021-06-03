from app import app,db
from flask import render_template, request, redirect, url_for, flash
from app.forms import UserInfoForm
from app.models import User
from .forms import UserInfoForm, LoginForm 

# @app.route('/')
# def hello_world():
#     #'posts' = Post.query.all(),
#     return  render_template('index.html', items=items)

@app.route('/', methods=['GET', 'POST'])  
def PhoneNumbs():
    title = 'PhoneNumbs'
    form = UserInfoForm()
    info = User.query.all()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        number = form.number.data
        #password = form.password.data
        existing_user = User.query.filter((User.name == name) | (User.number == number)).all()
        if existing_user : 
            flash('That username or email already exists. Please try again', 'danger')
            return redirect(url_for('PhoneNumbs'))

        
        new_user = User(name, number)
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered your phone number!','success')
        return redirect(url_for('PhoneNumbs' ))  

    return render_template('register.html', title=title, form=form, info=info)



@auth.route('/login', methods=['GET', 'POST'])
def login():
    title = 'LOGIN'
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password, password):
            flash('Incorrect Username/Password', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        flash('Success!',)
        return redirect(url_for('main.index'))

    return render_template('login.html', title=title, form=form)

    