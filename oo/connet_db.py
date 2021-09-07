import mysql.connector

class ConnectionMysql:
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='sistema')
        return self.conn
##use => obj=Connection()