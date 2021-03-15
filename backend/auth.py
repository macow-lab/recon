from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from user import User
import re
import recon

auth = Blueprint('auth', __name__, url_prefix='/auth', static_folder="static", template_folder="templates/auth/")

@auth.route("/register", methods=["GET", "POST"])
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
            login_user(newUser)
            return ('User created successfully.', 201)
        else:
            return ('Failed to create', 409)
    else: # Handling GET
        return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        #TODO Lav DB metode der tjekker om REQUEST eksisterer
        user = NotImplemented
        if user:
            flash("Account already exists.")
            return render_template("login.html")
        newUser = User()
    elif request.method == "GET":
        return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('recon.index'))