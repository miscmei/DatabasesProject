# Anand Basu and Maddy Fung
# Project Phase 5

import mariadb
import sys

dbName = 'proj_bf'

dbUser = 'abasu'

dbPass = 'pass3607'

query1_str = 'SELECT pname FROM Player WHERE strength > ?'

query2_str = 'SELECT DISTINCT uname FROM User U, Player P WHERE (U.player1 = P.pname OR U.player2 = P.pname OR U.player3 = P.pname) AND P.magic > ?'

query3_str = 'SELECT M.challenger AS strong_challenger, P.strength AS challenger_strength, M.opponent, M.time_stamp FROM Player P, Matches M WHERE strength >= ? AND P.pname = M.challenger'

query4_str = 'SELECT COUNT(*) AS Player_Matches FROM Matches WHERE challenger = ? OR opponent = ?'

query5_str = 'SELECT U.uname, avg(P.intelligence) AS avg_intelligence FROM Player P, User U WHERE U.player1 = P.pname OR U.player2 = P.pname OR U.player3 = P.pname GROUP BY (U.uname) HAVING AVG(P.intelligence) > ? '



class EverythingFantasyAPI:

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

        self.query1_cur = self.conn.cursor(prepared=True)
        self.query2_cur = self.conn.cursor(prepared=True)
        self.query3_cur = self.conn.cursor(prepared=True)
        self.query4_cur = self.conn.cursor(prepared=True)
        self.query5_cur = self.conn.cursor(prepared=True)
        self.query6_cur = self.conn.cursor(prepared=True)

    def close(self):
        self.query1_cur.close()
        self.query2_cur.close()
        self.query3_cur.close()
        self.conn.close()
        print('Database connection is closed')


    # def run_q1
    def run_q1(self, attribute, num):
        self.query1_cur.execute(query1_str,(num,))
        players = []
        for row in list(self.query1_cur):
            players.append(row)
        
        return players
    
    def run_q2(self, num):
        self.query2_cur.execute(query2_str,(num,))
        users = []
        for row in list(self.query2_cur):
            users.append(row)

        return users
    
    def run_q3(self, num):
        self.query3_cur.execute(query3_str, (num,))
        players = []
        for row in list(self.query3_cur):
            players.append(row)

        return players
    
    def run_q4(self, name):
        self.query4_cur.execute(query4_str, (name, name))

        return list(self.query4_cur)[0][0]
        
    def run_q5(self, num):
        self.query5_cur.execute(query5_str, (num,))
        users = []
        for row in list(self.query5_cur):
            users.append(row)

        return users
        