from database import Database
from networth import Networth
from budget import Budget
from flask_login import UserMixin

database = Database()


class User(UserMixin):


    def __init__(self, username, password, email):
        self.__id = None
        self.__username = username
        self.__password = password
        self.__email = email
        self.budget = Budget()
        self.networth = Networth()

    def getUsername(self):
        return self.__username
    
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
        '''
        Updates the budget instance for the user.
            Parameter:
            budget (dict): A dictionary of incomes and expenses.
        '''
        self.budget.updateIncomeExpenses(budget)
        # update db
        return database.updateIncomeExpenses(budget, self.__username)
    
    @staticmethod
    def loadUser(self, id: int):
        result = database.loadByID(id = id)
        
        user = User(
            username=result.get('username'), password=result.get('password'), email=result.get('email')
        )
        user.setID(result.get('id'))
        
        #TODO Handle rest of result, load budget ETC.
        
        return user

    def get_id(self):
        return self.__id