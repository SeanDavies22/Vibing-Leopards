# Class to handle database operations
# Casey Staples
# Version .3
import sqlite3


class HandleDB():
    def __init__(self):
        # Connect to the database upon creation of object
        self.connect_to_db()
        self.cursor = self.conn.cursor()

    # On deletion of object, close the connection to the database
    def __del__(self):
        self.disconnect_from_db()

    def connect_to_db(self):
        try:
            self.conn = sqlite3.connect('cost_db.db')
        except sqlite3.Error as e:
            print("Failed to connect to Database, check file path")

    def disconnect_from_db(self):
        # Close the connection to the database
        if (self.conn):
            self.conn.close()

    def pull_cve_id(self):
        # Pull the cve ids from the database
        cve_data = []
        self.cursor.execute("SELECT cve_id FROM cost")
        for row in self.cursor:
            cve_data.insert(0, row[0])
        return cve_data

    def pull_description(self):
        # Pull the vulnerability description from the database
        description_data = []
        self.cursor.execute("SELECT description FROM cost")
        for row in self.cursor:
            description_data.insert(0, row[0])
        return description_data

    def pull_description(self, cve_id):
        # Pull the vulnerability description from the database matching cve_id
        self.cursor.execute(
            "SELECT description FROM cost WHERE cve_id =?", (cve_id,))
        description = self.cursor.fetchone()
        return description[0]

    def push_cost_data(self, description, cost):
        # Push the vulnerability cost to the database
        self.cursor.execute(
            "UPDATE cost SET cost_per_hour = ? WHERE description = ?", (cost, description))
        self.conn.commit()


# Below code is outdated, but can be used to test the database operations..
# I won't update it, but you can still use it.
# You just have to update some of the names to match updates made to the above code

# HandleDB = HandleDB()
# print(HandleDB.pull_cve_id())
# data = []
# data = HandleDB.pull_cve_id()
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
