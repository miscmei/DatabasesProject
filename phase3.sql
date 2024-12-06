DROP TABLE IF EXISTS Tournament;
DROP TABLE IF EXISTS PlaysIn;
DROP TABLE IF EXISTS Matches;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Player;

-- Changed durability to durabil due to SQL keyword 'durability'
-- table Player is the stats and descriptions of each player that participates in a match
    -- pname: The player’s name. This is the primary key.
    -- strength: Rating of player’s strength.
    -- intelligence: Rating of player’s intelligence.
    -- durability: Rating of player’s durability.
    -- battle_iq: Rating of player’s battle IQ.
    -- speed: Rating of player’s speed.
    -- tech: Rating of players technology access.
    -- magic: Rating of player’s magic abilities.
    -- genre: The genre from which the player originates.
CREATE TABLE Player (
    pname varchar(40) NOT NULL,
    strength integer,
    intelligence integer,
    durabil integer, 
    battle_iq integer,
    speed integer,
    tech integer,
    magic integer,
    genre varchar(20),
    PRIMARY KEY(pname)
);

-- table User are the stats of each person that participates in the fantasy league tournament
    -- uname: The username of this user. This is the primary key.
    -- points: Point tally accrued by this user from all non-tournament matches.
    -- player1: the first player the user recruits
    -- player2: the second player the user recruits
    -- player3: the third player the user recruits
CREATE TABLE User (
    uname varchar(20) NOT NULL,
    points integer,
    player1 varchar(40) NOT NULL,
    player2 varchar(40) NOT NULL,
    player3 varchar(40) NOT NULL,
    PRIMARY KEY(uname),
    FOREIGN KEY (player1) REFERENCES Player (pname),
    FOREIGN KEY (player2) REFERENCES Player (pname),
    FOREIGN KEY (player3) REFERENCES Player (pname)
);

-- Changed table name to Matches due to SQL keyword 'Match'
-- table Matches is a matchup between two players.
    -- match_id: Number of match taking place. This is the primary key.
    -- timestamp: Time when the match takes place.
CREATE TABLE Matches (
    match_id integer NOT NULL,
    challenger varchar(40) NOT NULL,
    opponent varchar(40) NOT NULL,
    time_stamp datetime,
    PRIMARY KEY(match_id)
);



-- table Tournament is the bracket of a competition.
    -- tournament_match_id: Number of the tournament match taking place. This is the primary key.
    -- round_num: The round number of the tournament match.
    -- match_id: foreign key to the match_id of the Match entity
CREATE TABLE Tournament (
    tournament_match_id integer NOT NULL,
    round_num integer,
    match_id integer NOT NULL,
    PRIMARY KEY (tournament_match_id),
    FOREIGN KEY (match_id) REFERENCES Matches (match_id)
);

-- Insert some players
INSERT INTO Player (pname, strength, intelligence, durabil, battle_iq, speed, tech, magic, genre) VALUES
    ('Master Chief', 8, 4, 9, 10, 5, 8, 1, 'Fantasy'), 
    ('Julius Caesar', 3, 8, 3, 10, 4, 0, 0, 'Historical Figure'),
    ('A Brick', 10, 0, 10, 0, 0, 0, 0, 'Object'),
    ('Bill Gates', 1, 9, 2, 4, 1, 6, 0, 'Real Person'),
    ('Iron Man', 7, 9, 9, 8, 5, 10, 1, 'Fantasy'),
    ('Harry Potter', 3, 6, 4, 8, 5, 1, 10, 'Fantasy'),
    ('Toyota Corolla', 5, 1, 7, 0, 6, 5, 0, 'Object'),
    ('Neil Armstrong', 4, 8, 7, 2, 4, 6, 0, 'Historical Figure'),
    ('Professor Reilly', 10, 10, 10, 10, 10, 10, 10, 'Real Person'),
    ('Lebron James', 7, 4, 6, 3, 8, 4, 1, 'Real Person'),
    ('Mario', 2, 6, 4, 6, 4, 3, 9, 'Fantasy'),
    ('An Anvil', 10, 0, 10, 0, 0, 0, 0, 'Object'),
    ('Steve Jobs', 2, 9, 3, 5, 3, 6, 0, 'Real Person'),
    ('Minecraft Steve', 2, 6, 4, 6, 4, 3, 9, 'Fantasy'),
    ('Link', 6, 6, 4, 6, 4, 7, 9, 'Fantasy'),
    ('Sonic', 6, 6, 5, 5, 10, 7, 3, 'Fantasy'),
    ('Lightning McQueen', 7, 3, 6, 2, 10, 8, 4, 'Fantasy')
    ;


-- Insert three users
INSERT INTO User (uname, points, player1, player2, player3) VALUES
    ('Anand', 100, 'Master Chief', 'A Brick', 'Julius Caesar'),
    ('Maddy', 200, 'Bill Gates', 'Iron Man', 'Mario'),
    ('User3', 300, 'Toyota Corolla', 'Neil Armstrong', 'Lebron James'),
    ('User4', 400, 'Sonic', 'Minecraft Steve', 'An Anvil'),
    ('User5', 500, 'Steve Jobs', 'Lightning McQueen', 'Lightning McQueen');
    -- ('User3', 0, 'Harry Potter', 'Professor Reilly', 'Mario');
        -- the above line throws an error about a duplicate entry for User3 for the primary key, even with different player values

-- Insert times for five matches
INSERT INTO Matches (match_id, challenger, opponent, time_stamp) VALUES
    (1, 'Master Chief', 'Iron Man', "2022-10-16 14:00:00"),
    (2, 'A Brick', 'Bill Gates', "2022-10-17 12:00:00"),
    (3, 'Toyota Corolla', 'Mario', "2022-10-20 10:00:00"),
    (4, 'Master Chief', 'Lebron James', "2022-10-20 11:00:00"),
    (5, 'A Brick', 'Bill Gates', "2002-10-24 12:00:00"),
    (6, 'Steve Jobs', 'Minecraft Steve', "2002-10-21 08:00:00"),
    (7, 'Sonic', 'Master Chief', "2022-10-22 09:00:00")
    ;



-- Insert values for one tournament
INSERT INTO Tournament (tournament_match_id, round_num, match_id) VALUES
    (1, 1, 5),
    (2, 1, 6)
    ;
