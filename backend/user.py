from database import Database
from networth import networth
from budget import budget

database = Database()

class User:


    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        self.budget = budget()
        self.networth = networth()


    def createUser(self):
        return database.createUser(self.__username, self.__password, self.__email)