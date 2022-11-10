# SQL-lite testing branch

- This has been made into a class to house the funtionally of dealing with database
- It will return columns from the database as arrays
- Added editing the cost field of vulnerabilities in the DB, the description names must be exact for it to work
- Starting working on connecting GUI with database

  Finding matches between database array and nessus_file xml tag is functional!

  Pushing matched CVE ids found to the database to pull data is now functional!

  All functionally of database is complete, will add more functions to flesh out other niche needs later on in development

- Uses an 'outdated' version of natale's gui, but the functionality of connecting the database to the nesses file remains the same, the look of the gui does not matter currently.

  This is merely used for testing out functionality of the database, which seems to be nearly complete

  The handle_db.py can now be merged to the updated gui made by natele, for intergration into gui output of the data.

- Update.py will 'update' the cve_database.

  It will pull the cve cvs from the website, and push it into the database.
