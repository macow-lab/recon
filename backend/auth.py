from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
from database import Database
from user import User
import re
import json

db = Database()
authBP = Blueprint('auth', __name__, url_prefix='/auth', static_folder="static", template_folder="/auth/")



@authBP.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        requestData = request.get_json()
        
        userDic = {
            "username": requestData["username"],
            "password": requestData["password"],
            "email": requestData["email"]
        }
        # Validation of Email address and username
        if not re.match(r"[^@]+@[^@]+\.[^@]+.", userDic["email"]):
            return ('Invalid email address', 400)
        elif not re.match(r"^(?=[a-zA-Z0-9._]{3,20}$)(?!.*[_.]{2})[^_.].*[^_.]$", userDic["username"]):
            return ('Invalid username', 400)
        
        # TODO  Validate password
        
        # Creating user object and commiting to database if possible
        newUser = User(username = userDic["username"], password = userDic["password"], email = userDic["email"])
        
        if newUser.createUser():
            login_user(newUser, remember = True)
            
            return redirect(url_for("budget.networth_page"))
        else:
            return ('Failed to create', 409)
    else: # Handling GET
        return render_template("auth/register.html")


@authBP.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        fetched = db.ifUserExists(username)
        if not fetched.get("password") == password:
            flash("Passwords are " + password + fetched.get("password"))
            flash(fetched)
            return render_template("auth/login.html")
        flash("User found!")
        newUser = User(username = username, password = password, email = fetched.get("email"))
        newUser.setID(fetched.get("id"))

        login_user(newUser)
    
        return redirect(url_for("index"))
    elif request.method == "GET":
        return render_template("auth/login.html")

@authBP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('recon.index'))

def loadHelper(self, id):
    return db.loadByID(id)