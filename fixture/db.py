import mysql.connector

class DBFixture():

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connect(host=host, database=name, user=user, password=password)


    def distroy(self):
        self.connection.close()