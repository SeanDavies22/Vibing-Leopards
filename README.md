# SQL-lite testing branch

- This has been made into a class to house the funtionally of dealing with database
- It will return columns from the database as arrays
- currently only returns the vulnerability names from said column in database
- Added editing the cost field of vulnerabilities in the DB, the vulnerability names must be exact for it to work
- Starting working on connecting GUI with database
  Finding matches between database array and nessus_file xml tag is functional!
  Next step is pushing the match back to the database to pull the cost data to display on scree for user..

- Uses an 'outdated' version of natale's gui, but the functionality of connecting the database to the nesses file remains the same, the look of the gui does not matter currently.