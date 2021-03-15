import logging
from flask import Flask, request, render_template, Response
from flask_login import login_required, current_user, LoginManager
from flask_bootstrap import Bootstrap
from faker import Faker
from budget import Budget
from auth import Auth
from user import User
import json
import auth


app = Flask(__name__)


app.config['SECRET_KEY'] = 'Secret101'
user = None

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
    
app.register_blueprint(Budget)
app.register_blueprint(Auth)

def getUser():
    return user

def setUser(newuser):
    user = newuser
    return user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route('/dash/<username>/networth', methods=['GET', 'POST'])
# @login_required
def networth_page(username):
    return "<h1>moshi moshi</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    Bootstrap(app)
