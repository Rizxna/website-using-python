from flask import Blueprint, render_template, url_for, redirect , request, flash 
from . models import User
from werkzeug.security import generate_password_hash , check_password_hash

import sys , os
parent_dir= os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
sys.path.append(parent_dir)


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", )

@auth.route('/logout')
def logout():
    return "<p> logout </p>"

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/marketplace')
def marketplace():
    return render_template("marketplace.html")

@auth.route('/profile')
def profile():
    return render_template("profile.html")


@auth.route('/analytics')
def analytics():
    return render_template("analytics.html")

@auth.route('/allprojects')
def allprojects():
    return render_template("allprojects.html")

@auth.route('/createproject')
def createproject():
    return render_template("project_create.html")

@auth.route('/search')
def search():
    return render_template("search.html")

@auth.route('/profileedit')
def profileedit():
    return render_template("profileedit.html")

@auth.route('/support')
def support():
    return render_template("support.html")

@auth.route('/livestreams')
def livestreams():
    return render_template("video_updates.html")


@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Please enter the correct Email ID', category='error')
        elif len(first_name) < 2:
            flash('firstName should be greater than 1 character', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Please enter a password with at least 7 characters', category='error')
        else:
            flash('Account Successfully Created', category='success')
   
    return render_template("signup.html")


