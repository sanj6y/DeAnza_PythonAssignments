'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Unit D Take-home Assignment
'''

from collections import namedtuple

# Part One - Sets

class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}
class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"}
print(sorted(class1 & class2 & class3))
print(sorted(class1 | class2 | class3))
print(sorted(class1 - (class2 | class3)))

# Part Two - Swap

numbers = [1, 2, 3]
numbers[1], numbers[2] = numbers[2], numbers[1]
print(numbers)

# Part Three - Tuple Basics
tuple1 = ("Casablanca", 1942, "romantic drama")
(title, year, genre) = tuple1
print(title)

# Part Four - Named Tuple
Movie = namedtuple('Movie', 'title year genre')
movie1 = Movie("Casablanca", '1942', "romantic drama")
print(movie1.title)


# Part Five - Named Tuple Containing a List
Moviestars = namedtuple('Moviestars', ["title", "year", "genre", "stars"])
favoritemovie = Moviestars("Casablanca", "1942", "romantic drama", ["Humphrey Bogart", "Ingrid Bergman"])
favoritemovie.stars.append("Claude Rains")
print(favoritemovie.stars[1])
print(favoritemovie)

'''
Execution Results:
['Migel']
['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
['Li']
[1, 3, 2]
Casablanca
Casablanca
Ingrid Bergman
Moviestars(title='Casablanca', year='1942', genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])
'''