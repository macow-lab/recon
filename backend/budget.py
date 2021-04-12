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
        incomes = current_user.budget.getIncomesValue()
        list = []
        list.get("")
        return render_template("dashboard/dashbase.html", 
                            segment="budget",
                            incomes = current_user.budget.getIncomesValue(), 
                            expenses = current_user.budget.getExpenesValue(),
                            savings =current_user.budget.getSavings(),
                            investments =current_user.budget.getInvested()
                                )
        


class Budget:
    def __init__(self):
        self.__incomes = {}
        self.__expenses = {}
        self.__savings = 0
        self.__invested = 0

    def getIncomes(self):
        return self.__incomes
    
    def getIncomesValue(self):
        return sum(self.__incomes.values())

    def addIncomes(self, incomes: dict):
        for key, value in incomes.items():
            self.__incomes[key] = value
        return self.__incomes

    def getExpenses(self):
        return self.__expenses
    
    def getExpenesValue(self):
        return sum(self.__expenses.values())

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

    def updateIncomeExpenses(self, incomingUpdate: list): 
        '''
        The list of dicts are iterated over, and dicts are added to their respective lists.
            Parameter:
            incomingUpdate (list): A list of dictionaries with entries that are either incomes or expenses
        '''
        for item in incomingUpdate:
            for key, value in item.items(): # TODO For hver KV
                if value is None:
                    del item[key]
                    
                if value < 0 and key is "incomes":
                    self.__expenses[key] = json.dumps(value, use_decimal=True)
                elif value > 0 and key is "expenses":
                    self.__incomes[key] = json.dumps(value, use_decimal=True)
        return self.getAll()
            
