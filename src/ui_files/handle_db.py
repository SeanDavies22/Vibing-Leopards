# Class to handle database operations
# Casey Staples
# Version .2
import sqlite3


class HandleDB():
    def __init__(self):
        # Connect to the database
        self.conn = sqlite3.connect('Cost_DB.db')
        # Create a cursor to send SQL commands to database
        self.cursor = self.conn.cursor()

    # On deletion of object, close the connection to the database
    def __del__(self):
        self.conn.close()

    def pull_vuln_data(self):
        # Pull the vulnerability name from the database
        vuln_data = []
        self.cursor.execute("SELECT vulnerability FROM Vul_Cost")
        for row in self.cursor:
            vuln_data.insert(0, row[0])
        return vuln_data

    def pull_risk_data(self):
        # Pull the vulnerability risk from the database
        risk_data = []
        self.cursor.execute("SELECT risk_level FROM Vul_Cost")
        for row in self.cursor:
            risk_data.insert(0, row[0])
        return risk_data

    def push_cost_data(self, vuln, cost):
        # Push the vulnerability cost to the database
        self.cursor.execute(
            "UPDATE Vul_Cost SET cost_hour = ? WHERE vulnerability = ?", (cost, vuln))
        self.conn.commit()


# HandleDB = HandleDB()
# print(HandleDB.pull_vuln_data())
#data = []
#data = HandleDB.pull_vuln_data()
# for x in data:
#    print(x)
# data = HandleDB.pull_risk_data()
# for x in data:
#   print(x)
# for row in HandleDB.cursor.execute("SELECT * FROM Vul_Cost"):
#    print(row)
#input("Press Enter to continue...")
#cost = input("Enter the cost: ")
#vuln = input("Enter the vulnerability: ")

#HandleDB.push_cost_data(vuln, cost)
# for row in HandleDB.cursor.execute("SELECT * FROM Vul_Cost"):
#    print(row)

#del HandleDB
