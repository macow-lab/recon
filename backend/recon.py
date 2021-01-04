from flask import Flask, request, render_template, Response
from flask_login import LoginManager
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

@app.route("/signup", methods=["POST"])
def signup():
    # username VARCHAR(255) UNIQUE NOT NULL,
	# password VARCHAR(30) NOT NULL,
	# email VARCHAR(255) UNIQUE NOT NULL,
    newUser = {
        "username": request.form["username"],
        "password": request.form["password"],
        "email": request.form["email"]
    }
    
    return "<h1>moshi moshi " + newUser["username"] + " </h1>"

@app.route('/budget', methods=['GET', 'POST'])
def budget_page():
    return NotImplemented


@app.route('/networth', methods=['GET', 'POST'])
def budget_page():
    return NotImplemented

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
