from database import Database

class User:
    database = Database()
    
    def __init__(self, username, password, email):
        self.username = username
        self.__password = password
        self.__email = email
        
    def createUser(self):
        return database.insert(self)