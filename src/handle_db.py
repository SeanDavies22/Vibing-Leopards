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
        # Pull the vulnerability data from the database
        vuln_data = []
        for row in self.cursor.execute("SELECT vulnerability FROM Vul_Cost"):
            vuln_data = self.cursor.fetchall()
        return vuln_data
        conn.close()

HandleDB = HandleDB()
print(HandleDB.pull_vuln_data())
