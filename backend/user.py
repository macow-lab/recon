from database import Database

database = Database()

class User:
    
    
    def __init__(self, username, password, email):
        self.__username = username
        self.__password = password
        self.__email = email
        
    def createUser(self):
        return database.insert(self.__username, self.__password, self.__email)