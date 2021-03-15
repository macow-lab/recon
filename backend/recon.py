import logging
from flask import Flask, request, render_template, Response
from flask_login import LoginManager, login_required, login_user
from faker import Faker
from user import User
from database import Database
import json
import re

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'Secret101'

user = User("Sukuna", "pass", "admin@recon.com")


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route("/", methods=["GET"])
def home():
    return render_template("base.html")


@app.route("/auth/register", methods=["GET", "POST"])
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
            return ('User created successfully.', 201)
        else:
            return ('Failed to create', 409)
    else: # Handling GET
        return render_template("auth/register.html")


@app.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return "Placeholder"
    elif request.method == "GET":
        return render_template("auth/login.html")



@app.route('/dash/<username>/budget', methods=['GET', 'POST'])
# @login_required
def budget_page(username):
    # TODO: Fix så username-param opretter User objekt, og erstatter den oprettede 'user'
    
    if request.method == "POST":
        if user.updateIncomeExpenses(request.get_json()):
            return ('Created', 200)
        else:
            return ('Failed to update', 400)

    elif request.method == "GET":
        return "<h1>Hey {username}</h1>"


@app.route('/dash/<username>/networth', methods=['GET', 'POST'])
# @login_required
def networth_page(username):
    return "<h1>moshi moshi</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
