from flask import Flask, request, render_template, Response, Blueprint, flash
from flask_login import login_required, current_user
from database import Database
import simplejson as json
import decimal

budgetBP = Blueprint('budget', __name__,
                    url_prefix='/dash', static_folder="static")

database = Database()


@budgetBP.route('/budget', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == "POST":
        if 2 == 2:
            # GET REQUEST DATA 
            
            # UPDATE INCOMES EXPENSES FOR CURRENT USER
            
            # POST TO Database
            
            return ('Created', 200)
        else:
            return ('Failed to update', 400)
    elif request.method == "GET":
    #PASS DATA TO TEMPLATE
        return render_template("dashboard/dashbase.html", 
                            segment="budget",
                            incomes = current_user.budget.getIncomesSummary(), 
                            expenses = current_user.budget.getExpenesSummary(),
                            savings = current_user.budget.getSavingsSummary(),
                            investments = current_user.budget.getInvestmentsSummary(),
                            )
        


class Budget:
    def __init__(self):
        self.__incomes = {"summary": 0}
        self.__expenses = {"summary": 0}
        self.__savings = {"summary": 0}
        self.__investments = {"summary": 0}

    def getIncomes(self):
        return self.__incomes

    def getIncomesSummary(self):
            # TODO Loop over Dicts i Incomes, sum af values for "incomes" key
        return self.__incomes["summary"]

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
        return self.__savings["summary"]

    def getAll(self):
        combined = {**self.__incomes, **self.__expenses}
        return combined

    def updateIncomeExpenses(self, incomingUpdate: dict): 
        '''
        The list of dicts are iterated over, and dicts are added to their respective lists.
            Parameter:
            incomingUpdate (list): A list of dictionaries with entries that are either incomes or expenses
        '''
        flash("INCOMING UPDATE")
        flash(incomingUpdate)
        for item in incomingUpdate:
            flash("current Dict")
            flash(item)
            for key in list(item): # TODO For hver KV
                flash("Current Key: %s Value: %s" % (key, item.get(key)))
                if item.get(key) is None:
                    del item[key]
                    
            if item.get("incomes"):
                flash("Current Key: %s Value: %s | ADDED TO INCOMES" % (key, item.get(key)))
                self.__incomes[item.get("id")] = item
                self.__incomes["summary"] += item.get("incomes")
            elif item.get("expenses"):
                flash("Current Key: %s Value: %s | ADDED TO EXPENSES" % (key, item.get(key)))
                self.__expenses[item.get("id")] = item
                self.__expenses["summary"] -= item.get("expenses")
            elif item.get("savings"):
                flash("Current Key: %s Value: %s | ADDED TO SAVINGS" % (key, item.get(key)))
                self.__savings[item.get("id")] = item
                self.__savings["summary"] += item.get("savings")
            elif item.get("investments"):
                flash("Current Key: %s Value: %s | ADDED TO SAVINGS" % (key, item.get(key)))
                self.__investments[item.get("id")] = item
                self.__investments["summary"] -= item.get("investments")

            # TODO Expand T
            flash("POST UPDATE: ")
            flash(item)

                
        return self.getAll()
            
