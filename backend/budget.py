from flask import Flask, request, render_template, Response, Blueprint
from flask_login import login_required, current_user

budgetBP = Blueprint('budget', __name__,
                    url_prefix='/dash', static_folder="static")

@login_required
@budgetBP.route('/budget', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if 2 == 2:
            return ('Created', 200)
        else:
            return ('Failed to update', 400)
    elif request.method == "GET":
    

        return render_template("dashboard/dashbase.html", segment="budget",
                                )
        


class Budget:
    def __init__(self):
        self.__incomes = {}
        self.__expenses = {}
        self.__savings = 0
        self.__invested = 0

    def getIncomes(self):
        return self.__incomes

    def addIncomes(self, incomes: dict):
        for key, value in incomes.items():
            self.__incomes[key] = value
        return self.__incomes

    def getExpenses(self):
        return self.__expenses

    def addExpenses(self, expenses: dict):
        for key, value in expenses.items():
            self.__expenses[key] = value
        return self.__expenses

    def getSavings(self):
        return self.__savings

    def setSavings(self, savings: dict):
        self.__savings = savings
        return self.__savings

    def getInvested(self):
        return self.__invested

    def setInvest(self, invested: dict):
        self.__invested = invested
        return self.__invested

    def getAll(self):
        combined = {**self.__incomes, **self.__expenses}
        return combined

    def updateIncomeExpenses(self, incomingUpdate: dict):

        for item in incomingUpdate.items():
            key = item[0]
            value = item[1]
            if not isinstance(value, (int, float, complex)):
                print("Value for ", key, " is not a number.")
            elif value < 0:
                self.__expenses[key] = value
            elif value > 0:
                self.__incomes[key] = value
        return self.getAll()
