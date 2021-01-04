import logging
from flask import Flask, request, render_template, Response
from flask_login import LoginManager, login_required, login_user
from faker import Faker
from user import User
from database import Database
import json

app = Flask(__name__)

fake = Faker()
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/", methods=["GET"])
def home():
    return "<h1>moshi moshi</h1>"

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        userDic = {
            "username": request.form["username"],
            "password": request.form["password"],
            "email": request.form["email"]
        }
        newUser = User(userDic["username"], userDic["password"], userDic["email"])
        newUser = newUser.createUser(newUser)
        if newUser["Status"] == True:
            return ('User created successfully.', 201)
        else:
            app.logger.error(newUser["Error"])
            return ('Failed to create', 409)
    else:
        return  """
                Hello {}! Welcome to Recon :)  
                """.format("Mr Jojo")

@app.route('/budget', methods=['GET', 'POST'])
# @login_required
def budget_page():
    return "<h1>moshi moshi</h1>"


@app.route('/networth', methods=['GET', 'POST'])
# @login_required
def networth_page():
    return "<h1>moshi moshi</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
