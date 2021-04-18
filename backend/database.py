import mysql.connector
from mysql.connector import cursor
import simplejson as json


class Database:
    # dbConnector is the attribute that allows connection to the database
    def __init__(self):
        self.__db = "recondb"
        self.__dbHost = "database"
        self.__dbPort = "3306"
        self.__dbUser = "root"
        self.__dbPassword = "pass"
        self.__dbConnector = None
        self.__connect()

    def __connect(self):
        self.__dbConnector = mysql.connector.connect(
            host=self.__dbHost,
            port=self.__dbPort,
            user=self.__dbUser,
            password=self.__dbPassword,
            database=self.__db
        )

    def __getConnector(self):
        if self.__dbConnector.is_connected() is False:
            self.__connect()
        return self.__dbConnector

    def __getPreparedCursor(self):
        connector = self.__getConnector()
        return connector.cursor(prepared=True)

    def __getDictionaryCursor(self):
        connector = self.__getConnector()
        return connector.cursor(dictionary=True)

# CRUD Operations

    def createUser(self, username, password, email):  # COMPLETE AND WORKS
        try:
            dbConnector = self.__getConnector()
            cursor = self.__getDictionaryCursor()
            insertQuery = """
                            INSERT INTO user (
                                username,
                                password,
                                email
                            ) VALUES (%s, %s, %s);
                        """

            insertTuple = (username, password, email)
            cursor.execute(insertQuery, insertTuple)

            self.__dbConnector.commit()
            return True
        except mysql.connector.IntegrityError as err:
            return False
        finally:
            if dbConnector.is_connected:
                cursor.close()
                dbConnector.close()

    def ifCategoryExists(self, category: str, username: str):
        try:
            dbConnector = self.__getConnector()
            cursor = self.__getDictionaryCursor()
            cursor.execute(
                """
                        SELECT EXISTS(SELECT * FROM budget WHERE username= '{}' AND categories='{}');
                        """.format(username, category)
            )
            search = cursor.fetchone()
            cursor.close()
            result = search.values()
            return result
        except mysql.connector.IntegrityError as err:
            return False
        finally:
            if dbConnector.is_connected:
                cursor.close()
                dbConnector.close()

    
    def ifUserExists(self, username: str):
        try:
            dbConnector = self.__getConnector()
            cursor = self.__getDictionaryCursor()
            cursor.execute(
                """
                        SELECT * FROM user WHERE username= '{}';
                        """.format(username)
            )
            search = cursor.fetchone()
            
            if search == None:
                return False
            
            cursor.close()
            return search
        except mysql.connector.IntegrityError as err:
            return False
        finally:
            if dbConnector.is_connected:
                cursor.close()
                dbConnector.close()

    def updateIncomeExpenses(self, budget: dict, username: str):
        # Example for insert in database

        try:  # Set wether expense or income, and check if key already exists.
            dbConnector = self.__getConnector()
            cursor = self.__getDictionaryCursor()
            for item in budget.items():
                key = item[0]
                value = item[1]

                if value > 0:
                    dice = "incomes"
                else:
                    dice = "expenses"

                search = self.ifCategoryExists(key, username)
                
                if 1 in search:
                    updateQuery = None                   
                    if dice == "incomes":
                        updateQuery = """
                                        UPDATE budget SET incomes = %s WHERE username = %s AND categories = %s
                                    """
                    else: 
                        updateQuery = """
                                        UPDATE budget SET expenses = %s WHERE username = %s AND categories = '%s
                                    """

                    insertTuple = (value, username, key)
                    cursor.execute(updateQuery, insertTuple)
                else:
                    insertQuery = None
                    if dice == "incomes":
                        insertQuery = """
                                        INSERT into budget (
                                            username,
                                            incomes,
                                            categories
                                        ) VALUES (%s, %s, %s);
                                    """
                    else: 
                        insertQuery = """
                                        INSERT into budget (
                                            username,
                                            expenses,
                                            categories
                                        ) VALUES (%s, %s, %s);
                                    """

                    insertTuple = (username, value, key)
                    cursor.execute(insertQuery, insertTuple)
            self.__dbConnector.commit()
            return True
        except mysql.connector.IntegrityError as err:
            rejectedInsert = {
                "Error": err,
                "Status": False
            }
            return rejectedInsert
        finally:
            if dbConnector.is_connected:
                cursor.close()
                dbConnector.close()

    def getUsers(self):
        dbConnector = self.__getConnector()
        cursor = self.__getCursor()

        cursor.execute(
            """
            SELECT * FROM user;
        """
        )
        # Converts SQL resul to JSON
        result = json.dumps(cursor.fetchall())
        return result

    def loadByID(self, id: int):
        """ 
        Used by login manager, to completely load a user with all related table entries.
        """
        dbConnector = self.__getConnector()
        cursor = self.__getDictionaryCursor()
        try:
            
            selectQuery = """SELECT * FROM user where id = %s"""
            
            cursor.execute(selectQuery, (id, ))
            
            foundUser = cursor.fetchone()
            # TODO load budget table
            selectQuery = """
                                SELECT * FROM budget WHERE username = %s
                            """
            insertTuple = foundUser.get("username")
            
            cursor.execute(selectQuery, (insertTuple, ))

            budget = cursor.fetchall()
            foundUser['budget'] = []
            foundUser['investments'] = []
            foundUser['savings'] = []
            for item in budget:
                foundUser['budget'].append(item)  

            #TODO Handle rest of user loading
            
            return foundUser
        except mysql.connector.IntegrityError as err:
            rejectedInsert = {
                "Error": err,
                "Status": False
            }
            return rejectedInsert
        finally:
            if dbConnector.is_connected:
                cursor.close()
                dbConnector.close()