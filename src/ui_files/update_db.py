# simple script to pull updated cve data from the cve website and update the database..
import pandas as pd
import sqlite3
from sqlalchemy import create_engine


engine = create_engine('sqlite:///cve_data.db', echo=False)

# Pull the cve cvs from the database
df = pd.read_csv(
    'https://cve.mitre.org/data/downloads/allitems.csv', on_bad_lines='skip', encoding='ansi',
    engine='python', skiprows=10,
    skip_blank_lines=True,
    names=['ID', 'Status', 'Description',
           'References', 'Phase', 'Votes', 'Comments', 'Cost'])

# Drop the columns we don't need, we only need the ID and Description
df.drop(['Status', 'References', 'Phase', 'Votes',
        'Comments'], axis=1, inplace=True)

# Add a dummy row to test the 'update' function
df.loc[len(df.index)] = ['CVE-2024-0001', 'This is a test', '120']

# Update the database
with engine.begin() as connection:
    df.to_sql('cve_table', connection, if_exists='replace', index=False)

conn = sqlite3.connect('cve_data.db')
cursor = conn.cursor()
cursor.execute(
    "UPDATE cve_table SET Cost ='120'")
conn.commit()

# Save as file to check output is correct
df.to_csv('cve_data.csv', index=False)
conn.close()
