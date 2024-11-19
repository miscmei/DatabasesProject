
-- Query 1: restricts returned rows from one table
-- Selects player names who have strength greater than 5
SELECT pname FROM Player WHERE strength > 5;

-- Query 2: joins 2 tables and restricts rows
-- Selects users who have players with high magic
SELECT DISTINCT uname FROM User U, Player P WHERE 
    (U.player1 = P.pname OR U.player2 = P.pname OR U.player3 = P.pname) AND 
    P.magic > 7; 

-- Query 3: Complex condition to restrict returned rows
-- Selects matches in which the challenger had strength >= 8
SELECT M.challenger AS strong_challenger, P.strength AS challenger_strength, M.opponent, M.time_stamp FROM Player P, Matches M WHERE strength >= 8 AND P.pname = M.challenger;

-- Query 4: Query that uses a SQL aggregate function


-- Query 5: Query that uses GROUP BY and HAVING 
-- Returns the average intelligence of the players belonging to each user
SELECT  uname, avg(P.intelligence) AS avg_intelligence
FROM Player P, User U 
WHERE U.player1 = P.pname OR U.player2 = P.pname OR U.player3 = P.pname 
GROUP BY (U.uname) HAVING U.points >= 200;
;