'''
Sanjay Chandrasekar
Exercise G
Spring 2021
'''

# Part One - Working with Files
file1 = open("ZenOfPython.txt", "x")
file1 = open("ZenOfPython.txt", "w")
file1.write("Beautiful is better than ugly.\n")
file1.write("Explicit is better than implicit.\n")
file1.close()

file1 = open("ZenOfPython.txt", "a")
file1.write("Readability counts.\n")
file1.write("If the implementation is hard to explain, it's a bad idea.\n")
file1.close()

file1 = open("ZenOfPython.txt", "r")
print(file1.read())
file1.close()

# Part Two - CSV Files
import csv
citiesDict = {}

with open("Cities.csv", mode = "r") as readObj:
    reader = csv.reader(readObj)
    next(reader)
    for rows in reader:
        stateCityTuple = (rows[0], rows[1])
        citiesDict[stateCityTuple] = rows[2]

for i in citiesDict:
    print(i[0], i[1], citiesDict[i])
    
city = input("Please enter a city: ")
state = input("Please enter a state: ")
population = citiesDict[(city, state)]
print(f"{city} {state} has a population of {population}.")


'''
Execution Results:
Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.

Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064
Please enter a city: Dublin
Please enter a state: California
Dublin California has a population of 46036.
'''