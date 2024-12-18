# Anand Basu and Maddy Fung
# Project Phase 5

import mariadb

dbName = 'proj_bf'

dbUser = 'abasu'

dbPass = 'pass3607'

# Selects player names who have strength greater than a number 1-9
query1_str = 'SELECT pname FROM Player WHERE strength > ?'

#-- Selects users who have players with high magic
query2_str = 'SELECT DISTINCT uname FROM User U, Player P WHERE (U.player1 = P.pname OR U.player2 = P.pname OR U.player3 = P.pname) AND P.magic > ?'

# -- Selects matches in which the challenger had strength >= a number 1-10
query3_str = 'SELECT pname FROM Player WHERE strength >= ? AND intelligence >= ?;'

# -- Counts the number of matches involving a specific player
query4_str = 'SELECT COUNT(*) AS Player_Matches FROM Matches WHERE challenger = ? OR opponent = ?'

# -- Returns the average intelligence of each users 3 players, where the average is greater than a number 1-9
query5_str = 'SELECT U.uname, avg(P.intelligence) AS avg_intelligence FROM Player P, User U WHERE U.player1 = P.pname OR U.player2 = P.pname OR U.player3 = P.pname GROUP BY (U.uname) HAVING AVG(P.intelligence) > ? '

# -- Select Users with players that participated in tournament matches
query6_str = '(SELECT uname FROM User WHERE player1 IN (SELECT challenger FROM Matches WHERE match_id IN (SELECT match_id FROM Tournament)))'
query6_str += ' UNION (SELECT uname FROM User WHERE player2 IN (SELECT challenger FROM Matches WHERE match_id IN (SELECT match_id FROM Tournament)))'
query6_str += ' UNION (SELECT uname FROM User WHERE player3 IN (SELECT challenger FROM Matches WHERE match_id IN (SELECT match_id FROM Tournament)))'
query6_str += ' UNION (SELECT uname FROM User WHERE player1 IN (SELECT opponent FROM Matches WHERE match_id IN (SELECT match_id FROM Tournament)))'
query6_str += ' UNION (SELECT uname FROM User WHERE player2 IN (SELECT opponent FROM Matches WHERE match_id IN (SELECT match_id FROM Tournament)))'
query6_str += ' UNION (SELECT uname FROM User WHERE player3 IN (SELECT opponent FROM Matches WHERE match_id IN (SELECT match_id FROM Tournament)))'

class EverythingFantasyAPI:

    # init function creates the database connection and creates a cursor object
    # for each query that is part of this API   
    def __init__(self):
        print('connecting to db')
        try:
            self.conn = mariadb.connect(
            user = dbUser,
            password = dbPass,
            host="cslab.skidmore.edu",
            port=3306,
            database=dbName)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            exit(1)


        # creating DB cursors for each query 
        # setting to True so that the same query is run each time the cursor executes
        self.query1_cur = self.conn.cursor(prepared=True)
        self.query2_cur = self.conn.cursor(prepared=True)    
        self.query3_cur = self.conn.cursor(prepared=True)
        self.query4_cur = self.conn.cursor(prepared=True)
        self.query5_cur = self.conn.cursor(prepared=True)
        self.query6_cur = self.conn.cursor(prepared=True)

    # closes DB connection
    def close(self):
        self.query1_cur.close()
        self.query2_cur.close()
        self.query3_cur.close()
        self.conn.close()
        print('Database connection is closed')


    # runs query 1 using the provided number for the strength
    def run_q1(self, num):
        self.query1_cur.execute(query1_str,(num,))
        players = []
        for row in list(self.query1_cur):
            players.append(row)
        
        return players
    
    # runs query 2 using the provided number for the magic
    def run_q2(self, num):
        self.query2_cur.execute(query2_str,(num,))
        users = []
        for row in list(self.query2_cur):
            users.append(row)

        return users
    
    # runs query 3 using the provided number for the strength of the challenger
    def run_q3(self, num, num2):
        self.query3_cur.execute(query3_str, (num, num2))
        players = []
        for row in list(self.query3_cur):
            players.append(row)

        return players
    
    # runs query 4 using the player name provided 
    def run_q4(self, name):
        self.query4_cur.execute(query4_str, (name, name))

        return list(self.query4_cur)[0][0]
        
    # runs query 5 using the number provided for the average intelligence
    def run_q5(self, num):
        self.query5_cur.execute(query5_str, (num,))
        users = []
        for row in list(self.query5_cur):
            users.append(row)

        return users
        
    # runs the query to find users with players that participated in tournament matches
    def run_q6(self):
        self.query6_cur.execute(query6_str)

        return list(self.query6_cur)