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

    def __getCursor(self):
        connector = self.__getConnector()
        return connector.cursor(dictionary=True)
    

    def insert(self, User):
        # Example for insert in database
        dbConnector = self.__getConnector()
        cursor = self.__getCursor()
        try:
            cursor.execute(
                """
                    INSERT INTO user (
                        username,
                        password,
                        email
                    ) VALUES ('{}', '{}', '{}');
                """.format(
                    User.username,
                    User.password,
                    User.email
                )
            )
            self.__dbConnector.commit()
            return True
        except mysql.connector.IntegrityError as err:
            rejectedInsert = {
                "Error": err,
                "Status": False
            }
            return rejectedInsert
            

    def get_users(self):
        # Example for select
        dbConnector = self.__getConnector()
        cursor = self.__getCursor()
        
        cursor.execute(
            """
            SELECT * FROM __table;
        """
        )
        # Converts SQL resul to JSON
        result = json.dumps(cursor.fetchall())
        return result