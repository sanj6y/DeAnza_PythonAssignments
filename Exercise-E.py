'''
Sanjay Chandrasekar
Exercise E
'''

# First Script

# Determining the genre of a movie

scifi = ['Alien', 'Solaris', 'Inception', 'Moon']
comedy = ['Borat', 'Idiocracy', 'Superbad', 'Bridesmaids']
name = input("Please enter a movie title: ")
if (name in scifi):
    print(f'{name} is a scifi movie.')
elif (name in comedy):
    print(f'{name} is a comedy movie.')
else:
    print(f'Sorry, I don\'t know what kind of movie {name} is.')

'''
Execution Results:
Please enter a movie title: Moon
Moon is a scifi movie.
Please enter a movie title: Superbad
Superbad is a comedy movie.
Please enter a movie title: Dunkirk
Sorry, I don't know what kind of movie Dunkirk is.
'''

# Second Script

# Using range with a for loop
for i in range(10, -1, -2):
    print(i)
    
# Looping through Dictionary Items
movies = {
    'The Wizard of Oz': 1939, 
    'The Godfather': 1972,
    'Lawrence of Arabia': 1962,
    'Raging Bull': 1980
    }
movieList = sorted(movies)
movieVals = sorted(movies.values())
for x in movieList:
    print(x + " was made in " + str(movies.get(x)))
    
'''
Execution Results:
10
8
6
4
2
0
Lawrence of Arabia was made in 1962
Raging Bull was made in 1980
The Godfather was made in 1972
The Wizard of Oz was made in 1939
'''