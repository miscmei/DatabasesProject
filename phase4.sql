
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
SELECT PI.challenger AS strong_challenger, P.strength AS challenger_strength, PI.meeting_num,  PI.opponent FROM Player P, PlaysIn PI WHERE strength >= 8 AND P.pname = PI.challenger;

-- Query 4: Query that uses a SQL aggregate function