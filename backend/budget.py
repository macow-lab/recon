class budget:
    
    def __init__(self):
        self.__incomes = {}
        self.__expenses = {}
        self.__savings = None
        self.__invested = None

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
    
    def updateIncomeExpenses(self, budget: dict):
        self.__expenses = {}
        self.__incomes = {}
        
        for key, value in budget.items():
            if isinstance(value, (int, float, complex)):
                print("Value for ", key, " is not a number.")
            elif value < 0: 
                self.__expenses[key] = value
            elif value > 0:
                self.__incomes[key] = value
        return True