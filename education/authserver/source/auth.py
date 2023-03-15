from flask import Blueprint, render_template, request, redirect, url_for, flash
from education.authserver.models import User, UserInfo
from werkzeug.security import generate_password_hash, check_password_hash
from education.authserver import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Nu yopta', category='success')
                login_user(user, remember=True)
                return redirect(url_for('view.index'))
            else:
                flash('Pshol nah', category='error')
        else:
            flash('Email doesnot exist!')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        second_name = request.form.get('secondName')
        password = request.form.get('password')
        conformation = request.form.get('conformation')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Uje bil email', category='error')
        elif len(email) < 4:
            flash('Heroviy email', category='error')
        elif len(first_name) < 2:
            flash('Herovoe imya', category='error')
        elif password != conformation:
            flash('Vtoroy password luchshe nabiray, loshara', category='error')
        elif len(password) < 7:
            flash('Heroviy password, loshara', category='error')
        else:
            # add user to databese
            new_user = User(email=email, password=generate_password_hash(password, method='sha256'))

            db.session.add(new_user)

            db.session.commit()
            login_user(new_user, remember=True)

            print(current_user.id)
            new_user_info = UserInfo(first_name=first_name, second_name=second_name, user_id=current_user.id)
            db.session.add(new_user_info)
            db.session.commit()
            print('ya ya zer gut!')

            flash('Nu yopt, goda ne proshlo', category='success')
            return redirect(url_for('view.index'))
    return render_template("signup.html", user=current_user)

