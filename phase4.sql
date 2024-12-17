
-- Query 1: restricts returned rows from one table
-- Selects player names who have strength greater than 5
SELECT pname FROM Player WHERE strength > 5;

-- Query 2: joins 2 tables and restricts rows
-- Selects users who have players with high magic
SELECT DISTINCT uname FROM User U, Player P WHERE 
    (U.player1 = P.pname OR U.player2 = P.pname OR U.player3 = P.pname) AND 
    P.magic > 7; 

-- Query 3: Complex condition to restrict returned rows
-- Selects players with strength >= 7 and intelligence >= 7
SELECT pname FROM Player WHERE strength >= 7 AND intelligence >= 7;

-- Query 4: Query that uses a SQL aggregate function
-- Counts the number of matches involving master chief
SELECT COUNT(*) AS Master_Chief_Matches FROM Matches WHERE challenger = 'Master Chief' OR opponent = 'Master Chief';

-- Query 5: Query that uses GROUP BY and HAVING 
-- Returns the average intelligence of each users 3 players, where the average is greater than 5
SELECT  U.uname, avg(P.intelligence) AS avg_intelligence
FROM Player P, User U 
WHERE U.player1 = P.pname OR U.player2 = P.pname OR U.player3 = P.pname 
GROUP BY (U.uname) HAVING AVG(P.intelligence) > 5
;

-- Query 6: Query with sub-query of set operators
-- Select Users with players that participated in tournament matches
SELECT uname FROM User WHERE player1 IN (
    SELECT challenger FROM Matches WHERE match_id IN (
        SELECT match_id FROM Tournament
    )
)
UNION
SELECT uname FROM User WHERE player2 IN (
    SELECT challenger FROM Matches WHERE match_id IN (
        SELECT match_id FROM Tournament
    )
)
UNION
SELECT uname FROM User WHERE player3 IN (
    SELECT challenger FROM Matches WHERE match_id IN (
        SELECT match_id FROM Tournament
    )
)
UNION
SELECT uname FROM User WHERE player1 IN (
    SELECT opponent FROM Matches WHERE match_id IN (
        SELECT match_id FROM Tournament
    )
)
UNION
SELECT uname FROM User WHERE player2 IN (
    SELECT opponent FROM Matches WHERE match_id IN (
        SELECT match_id FROM Tournament
    )
)
UNION
SELECT uname FROM User WHERE player3 IN (
    SELECT opponent FROM Matches WHERE match_id IN (
        SELECT match_id FROM Tournament
    )
) 
;
