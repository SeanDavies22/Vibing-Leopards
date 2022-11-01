# Class to handle database operations
# Casey Staples
# Version .2
import sqlite3


class HandleDB():
    def __init__(self):

        # Connect to the database
        self.conn = sqlite3.connect('Cost_DB.DB')
        # Create a cursor to send SQL commands to database
        self.cursor = self.conn.cursor()

    def pull_vuln_data(self):
        # Pull the vulnerability name from the database
        vuln_data = []
        self.cursor.execute("SELECT vulnerability FROM Vul_Cost")
        for row in self.cursor:
            vuln_data.insert(0, row[0])
        return vuln_data


HandleDB = HandleDB()
# print(HandleDB.pull_vuln_data())
data = []
data = HandleDB.pull_vuln_data()
for x in data:
    print(x)
