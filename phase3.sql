DROP TABLE IF EXISTS Tournament;
DROP TABLE IF EXISTS PlaysIn;
DROP TABLE IF EXISTS Matches;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Player;

-- Changed durability to durabil due to SQL keyword 'durability'
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
CREATE TABLE Matches (
    match_id integer NOT NULL,
    time_stamp datetime,
    PRIMARY KEY(match_id)
);

CREATE TABLE PlaysIn (
    meeting_num integer NOT NULL,
    challenger varchar(40) NOT NULL,
    opponent varchar(40) NOT NULL,
    match_id integer NOT NULL,
    PRIMARY KEY(meeting_num, challenger, opponent, match_id),
    FOREIGN KEY (challenger) REFERENCES Player (pname),
    FOREIGN KEY (opponent) REFERENCES Player (pname),
    FOREIGN KEY (match_id) REFERENCES Matches (match_id)
);

CREATE TABLE Tournament (
    tournament_match_id integer NOT NULL,
    round_num integer,
    match_id integer NOT NULL,
    PRIMARY KEY (tournament_match_id),
    FOREIGN KEY (match_id) REFERENCES Matches (match_id)
);

-- Insert a few players
INSERT INTO Player (pname, strength, intelligence, durabil, battle_iq, speed, tech, magic, genre) VALUES
    ('Master Chief', 8, 4, 9, 10, 5, 8, 1, 'Fantasy'), 
    ('Julius Caesar', 3, 8, 3, 10, 4, 0, 0, 'Historical Figure'),
    ('A Brick', 10, 0, 10, 0, 0, 0, 0, 'Object'),
    ('Bill Gates', 1, 9, 2, 4, 1, 6, 0, 'Historical Figure'),
    ('Iron Man', 7, 9, 9, 8, 5, 10, 1, 'Fantasy'),
    ('Mario', 2, 6, 4, 6, 4, 3, 9, 'Fantasy');

-- Insert two users
INSERT INTO User (uname, points, player1, player2, player3) VALUES
    ('Anand', 0, 'Master Chief', 'A Brick', 'Julius Caesar'),
    ('Maddy', 0, 'Bill Gates', 'Iron Man', 'Mario');

-- Insert times for two matches
INSERT INTO Matches (match_id, time_stamp) VALUES
    (1, "2022-10-16 14:00:00"),
    (2, "2022-10-17 12:00:00");

INSERT INTO PlaysIn (meeting_num, challenger, opponent, match_id) VALUES
    (1, 'Master Chief', 'Iron Man', 1),
    (1, 'A Brick', 'Bill Gates', 2);

