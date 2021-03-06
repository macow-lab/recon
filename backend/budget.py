from database import Database

class budget:
    
    def __init__(self):
        self.__incomes = {}
        self.__expenses = {}
        self.__savings = None
        self.__invested = None

    def getIncomes(self):
        return self.__incomes
    
    def setIncomes(self, incomes: dict):
        self.__incomes = incomes
        return self.__incomes

    def getExpenses(self):
        return self.__expenses
    
    def setExpenses(self, expenses: dict):
        self.__expenses = expenses
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
    
    def updateBudget(self, budget: dict):
        for key, value in budget.items():
            if value < 0: 
                return "how"