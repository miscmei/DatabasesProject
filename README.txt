First run phase3.sql to make the schema and insert a small amount of test data which is used
    in later queries.

The file randdata.py inserts a large list of Players, Users, and Matches, and a few Tournament matches
 into the database, so it can only be run once and the tables must be reset before it can be run again.

If you want to run randdata.py again, rerun phase3.sql to reset the tables back to the small amount
    of test data. All of the data except what is hardcoded in phase3.sql will have different values.

The file apitesting.py prints out a large amount of data to the screen, but each print is separated by a blank line,
    although it might be best to run each test query one at a time.

