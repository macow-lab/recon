from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from database import Database
from user import User
import re

db = Database()
authBP = Blueprint('auth', __name__, url_prefix='/auth', static_folder="static", template_folder="templates/auth/")

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
        newUser = User(userDic["username"], userDic["password"], userDic["email"])
        
        if newUser.createUser():
            login_user(newUser, remember = True)
            return ('User created successfully.', 201)
        else:
            return ('Failed to create', 409)
    else: # Handling GET
        return render_template("register.html")


@authBP.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        fetched = db.ifUserExists(username)
        if not fetched or not fetched[2] == password:
            flash("Try checking your credentials again!")
            return redirect(url_for("auth.login"))
        
        newUser = User(username, password, fetched[3])
        login_user(newUser)
        return redirect(url_for("budgetBP.budgetIndex"))
    elif request.method == "GET":
        return render_template("login.html")

@authBP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('recon.index'))