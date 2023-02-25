'''
Sanjay Chandrasekar
Exercise H
Spring 2021
'''

# Part 1 - A Basic Class - State Data
class StateData:
    def __init__(self, name, abbreviation, region, population):
        self.name = name
        self.abbreviation = abbreviation
        self.region = region
        self.population = population
    
    def __str__(self):
        return self.name
    
    def displayState(self):
        print(f"{self.name} ({self.abbreviation}) is in the {self.region} region and has population of {str(self.population)}.")

s1 = StateData("California", "CA", "West", 39250000)
print(s1.__str__())
s1.displayState()

# Part 2 - Different ways of working with Attributes
class StateData2:
    def __init__(self, name):
        self.name = name
    
    def setRegion(self, region):
        self.region = region
    
    def getRegion(self):
        return self.region
    
s2 = StateData2("California")
s2.setRegion("West")
s2.pop = 39250000
print(s2.name)
print(s2.getRegion())
print(s2.region)
print(s2.pop)

# Part 3 - Data Hiding
class StateData2:
    public = ""
    _protected = ""
    __private = ""
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

test = StateData2()
print(test.public)
print(test._protected)
print(test.__private)

'''
Execution Results:
California
California (CA) is in the West region and has population of 39250000.
California
West
West
39250000
Public
Protected

'''