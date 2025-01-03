# Database for an All-Purpose Fantasy League
This is a relational database is for an all-purpose fantasy league. It utilizes SQL and Python to build the database and perform queries on it. 

# Content
- SQL files with code to create tables in the database. 
- An API with functions that return sample queries.
- Sample data with 1000 players and code to generate data to fill the Users, Matches, and Tournament tables.

# Running the Application
1. First run phase3.sql to make the tables and insert a small amount of test data which is used in later queries.

2. The file randdata.py inserts a large list of Players, Users, and Matches, and a few Tournament matches
 into the database, so it can only be run once and the tables must be reset before it can be run again.

3. If you want to run randdata.py again, rerun phase3.sql to reset the tables back to the small amount of test data. All of the data except what is hardcoded in phase3.sql will have different values.

4. The file apitesting.py prints out a large amount of data to the screen, but each print is separated by a blank line, although it might be best to run each test query one at a time.

# Acknowledgements
Authors: Maddy Fung and Anand Basu
This project is for the Database Systems course taught by Dr. Christine Reilly at Skidmore College
