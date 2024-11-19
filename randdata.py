import random

# characters to insert and genres
# each character name is unqiue, so can be used as a dictionary key
characters = {
    'Gandalf':'Fantasy',
    'Frodo':'Fantasy',
    'Ron Weasley':'Fantasy',
    'A Rock':'Object',
    'Gushers':'Object',
    'Noble 6':'Fantasy',
    'Expo Marker':'Object',
    'Anand Basu':'Real Person',
    'Maddy Fung':'Real Person',
    'Moby Dick Hardcover':'Object',
    'Batman':'Fantasy',
    'Spider-Man':'Fantasy',
    'Captain America':'Fantasy',
    'Black Panther':'Fantasy',
    'Pine Tree':'Object',
    'Birch Tree':'Object',
    'Grandfather Clock':'Object',
    'Jude Bellingham':'Real Person',
    'Ace of Spades':'Object',
    'Erling Haaland':'Real Person',
    'Lewis Hamilton':'Real Person',
    'Michael Schumacher':'Real Person',
    'Abraham Lincoln':'Historical Figure',
    'Geroge Washington':'Historical Figure',
    'Gandhi':'Historical Figure',
    'Zeus':'God',
    'God':'God',
    'Poseidon':'God',
    'Socrates':'Historical Figure',
    'Plato':'Historical Figure',
    'Renault R26':'Object',
    'RB19':'Object',
    'Dacia Sandero':'Object'
              }


# generate random vals for each characters stats
stats = []
for i in range(len(characters)):
    indiv_stats = []
    for j in range(7):
        indiv_stats.append(random.randint(0, 10))
    stats.append(indiv_stats)


# combine character and stats into a single tuple
i = 0
all_char = []
for char in characters:
    indiv_char = [char]
    for j in range(7):
        indiv_char.append(stats[i][j])
    indiv_char.append(characters[char])
    indiv_char = tuple(indiv_char)
    all_char.append(indiv_char)
    i += 1

#print out data as a test
print(all_char)