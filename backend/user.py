from database import Database
from networth import networth
from budget import budget

database = Database()

class User:


    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__dbID = None
        self.budget = budget()
        self.networth = networth()

    # Mutators
    def setdbID(self, databaseUserId):
        self.__databaseUserId = databaseUserId

    def getdbID(self):
        return self.__databaseUserId
    
    def getUsername(self):
        return self.__username
    
    def getUsername(self):
        return self.__password
    
    def setPassword(self, password):
        self.__password = password
        return self.__password
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email

    # Main methods
    def createUser(self):
        return database.createUser(self.__username, self.__password, self.__email)
    
    def updateIncomeExpenses(self, budget: dict):
        self.budget.updateIncomeExpenses(budget)
        # update db