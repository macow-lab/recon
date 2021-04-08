import logging
from flask import Flask, request, render_template, Response, flash
from flask_login import login_required, current_user, LoginManager
from faker import Faker
from budget import budgetBP
from auth import authBP
from user import User
from database import Database
import json
import auth


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Secret101'

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

db = Database()
app.register_blueprint(budgetBP)
app.register_blueprint(authBP)


@login_manager.user_loader
def load_user(user_id):
    # Load user baseret på id
    try:
        # TODO LAV LOADER SÅ DET VIRKER OG RETURNERE
        result = db.loadByID(user_id)
        flash("RESULT BIG MAN!")
        user = User(
            username=result.get('username'), password=result.get('password'), email=result.get('email'), id = result.get('id')
        )
        #TODO Handle rest of result, load budget ETC.
        user.budget.updateIncomeExpenses(result.get('budget'))
        return user
    except:
        return user


@app.route("/", methods=["GET"])
def index():
    flash(load_user(1))
    return render_template("index.html")


@app.route('/dash/<username>/networth', methods=['GET', 'POST'])
# @login_required
def networth_page(username):
    return "<h1>moshi moshi</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

