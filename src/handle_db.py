# Basic code to show how handling the database is easy
# Casey Staples
# Version .1
import sqlite3

# connect to the database
conn = sqlite3.connect('Cost_DB.db')
print("This connected to the database successfully")

# Create a cursor, this allows us to execute SQL commands
cursor = conn.execute(
    "SELECT id, vulnerability, risk_level, cost_hour, hours, recommendation from Vul_Cost")
# Print the data from the database
for row in cursor:
    print("ID = ", row[0])
    print("Vulnerability = ", row[1])
    print("Risk ", row[2],)
    print("Total Cost = ", round(row[3]*row[4], 2))
    print("We recommend you", row[5], "\n")

print("Operation done successfully")
# Close the connection like scanner.close() in java
conn.close()
