from flask import Blueprint, render_template, request, redirect, url_for, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

    return render_template("login.html")


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/sign-up', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        second_name = request.form.get('secondName')
        password = request.form.get('password')
        conformation = request.form.get('conformation')

        if len(email) < 4:
            pass
            flash('Heroviy email', category='error')
        elif len(first_name) < 2:
            flash('Herovoe imya', category='error')
        elif password != conformation:
            flash('Vtoroy password luchshe nabiray, loshara', category='error')
        elif len(password) < 7:
            flash('Heroviy password, loshara', category='error')
        else:
            # add user to databese
            print('ya ya zer gut!')
            return redirect(url_for('afisha.index'))
    return render_template("signup.html")

