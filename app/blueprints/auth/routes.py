import sqlite3
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from nexus import get_user_by_username, create_user
from flask_login import UserMixin

auth = Blueprint('auth', __name__)

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user_by_username(username)
        if user and check_password_hash(user[1], password):
            user_obj = User(user[0], username)
            login_user(user_obj)
            return redirect(url_for('home.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            create_user(username, password)
            flash('Registration successful! You can now log in.')
            return redirect(url_for('auth.login'))
        except sqlite3.IntegrityError:
            flash('Username already exists.')
        except ValueError:
            flash("Username contains invalid characters")
    return render_template('auth/register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
