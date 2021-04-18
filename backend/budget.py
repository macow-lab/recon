from flask import Flask, request, render_template, Response, Blueprint, flash
from flask_login import login_required, current_user
from database import Database
import simplejson as json
import decimal

budgetBP = Blueprint('budget', __name__,
                    url_prefix='/dash', static_folder="static")

database = Database()


@budgetBP.route('/budget', methods=['GET'])
@login_required
def index():
        return render_template("dashboard/dashbase.html", 
                            segment="budget",
                            incomes = current_user.budget.getIncomesSummary(), 
                            expenses = current_user.budget.getExpenesSummary(),
                            savings = current_user.budget.getSavingsSummary(),
                            investments = current_user.budget.getInvestmentsSummary(),
                            tableData = current_user.budget.getLatestUpdate(),
                            )
        
@budgetBP.route('/budget/edit', methods=['GET', 'POST'])
@login_required
def edit():
    if request.method == "POST":
        flash("RECEIVED BUDGET POST")
        flash(request.get_json())
        return ('Created', 200)
    elif request.method == "GET":
    #PASS DATA TO TEMPLATE
        return render_template("dashboard/dashbase.html", 
                            segment="budgetEdit",
                            tableData = current_user.budget.getLatestUpdate(),
                            )
class Budget:
    def __init__(self):
        self.__incomes = {"summary": 0}
        self.__expenses = {"summary": 0}
        self.__savings = {"summary": 0}
        self.__investments = {"summary": 0}
        self.__latestUpdate = None

    def getIncomes(self):
        return self.__incomes

    def getIncomesSummary(self):
            # TODO Loop over Dicts i Incomes, sum af values for "incomes" key
        return self.__incomes["summary"]
    
    def getLatestUpdate(self):
        return self.__latestUpdate

    def addIncomes(self, incomes: dict):
        for key, value in incomes.items():
            self.__incomes[key] = value
        return self.__incomes

    def getExpenses(self):
        return self.__expenses
    
    def getExpenesSummary(self):
        return self.__expenses["summary"]

    def addExpenses(self, expenses: dict):
        for key, value in expenses.items():
            self.__expenses[key] = value
        return self.__expenses

    def getSavings(self):
        return self.__savings

    def getSavingsSummary(self):
        return self.__savings["summary"]

    def getInvested(self):
        return self.__investments

    def getInvestmentsSummary(self):
        return self.__investments["summary"]

    def getAll(self):
        combined = {**self.__incomes, **self.__expenses}
        return combined

    def updateIncomeExpenses(self, incomingUpdate: dict): 
        '''
        The list of dicts are iterated over, and dicts are added to their respective lists.
            Parameter:
            incomingUpdate (list): A list of dictionaries with entries that are either incomes or expenses
        '''
        self.__latestUpdate = incomingUpdate
        flash(incomingUpdate)
        for item in incomingUpdate:
            for key in list(item): # TODO For hver KV
                if item.get(key) is None:
                    del item[key]
                    
            if item.get("incomes"):
                self.__incomes[item.get("id")] = item
                self.__incomes["summary"] += item.get("incomes")
            elif item.get("expenses"):
                self.__expenses[item.get("id")] = item
                self.__expenses["summary"] -= item.get("expenses")
            elif item.get("savings"):
                self.__savings[item.get("id")] = item
                self.__savings["summary"] += item.get("savings")
            elif item.get("investments"):
                self.__investments[item.get("id")] = item
                self.__investments["summary"] += item.get("investments")
        flash(self.__incomes)
        flash(self.__investments)
        flash(self.__savings)

            # TODO Expand T


                
        return self.getAll()
            
