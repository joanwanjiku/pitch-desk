from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
# from .. import db
from .forms import RegistrationForm, LoginForm
from ..email import mail_message

@auth.route('/signup', methods=['GET', 'POST'])
def register():
    title = "Pitches - New Account"
    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        user = User(
            email = reg_form.email.data,
            name = reg_form.username.data,
            password = reg_form.password.data
        )
        User.save_user(user)

        mail_message("Welcome to watchlist","email/welcome_user",user.email,user=user)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', signup_form= reg_form)

@auth.route('/signin', methods= ['GET', 'POST'])
def login():
    title = "Pitches - Login"
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email =login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)

            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', login_form=login_form, title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))