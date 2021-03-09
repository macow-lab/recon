import mysql.connector
from mysql.connector import cursor
import json


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

    def createUser(self, username, password, email): # COMPLETE AND WORKS
        dbConnector = self.__getConnector()
        cursor = self.__getPreparedCursor()
        try:
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

    def updateIncomeExpenses(self, budget: dict, username: str):
        # Example for insert in database
        dbConnector = self.__getConnector()
        cursor = self.__getPreparedCursor()

        try:
            fuck["Entered-Try"] = True
            for item in budget.items():
                key = item[0]
                value = item[1]
                
                if value > 0:
                    dice = "incomes"
                else:
                    dice = "expenses"
                    
                cursor.execute(
                    """
                    SELECT EXISTS(SELECT * FROM budget WHERE username= '{}' AND categories='{}');
                    """.format(username, key)
                )
                search = cursor.fetchone()
                
                if search[0]:
                    updateQuery = f"""
                                        UPDATE budget SET {dice} = %s, categories = '%s' WHERE username = '%s' AND categories = '%s'
                                    """.format(dice)
                    insertTuple = (value, key, username, key)
                    cursor.execute(updateQuery, insertTuple)
                    self.__dbConnector.commit()
                else:
                    insertQuery = f"""
                                        INSERT into budget (
                                            username,
                                            {dice},
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

# TODO: Opret og returner user objekt ud fra username
    def getUsername(self):
        return NotImplemented
