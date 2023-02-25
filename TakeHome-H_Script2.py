'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Unit H Take-home Assignment
Script 2
'''

# Second Script - Operator Overloading
import math

class BritCoins():
    __coinValues = {"pound":240, "shilling":12, "penny":1}
    
    def __init__(self, **kwargs):
        self.totalPennies = 0
        for coinType in kwargs:
            self.totalPennies += (self.__coinValues[coinType]*kwargs[coinType])
    def __add__(self, otherVal):
        total = self.totalPennies + otherVal.totalPennies
        return BritCoins(penny = total)
    def __sub__(self, otherVal):
        total = self.totalPennies - otherVal.totalPennies
        return BritCoins(penny = total)
    def __str__(self):
        resultString = ""
        remainingPennies = self.totalPennies
        pound = remainingPennies // self.__coinValues["pound"]
        if pound != 0:
            resultString += (" " + str(pound) + " pounds")
            remainingPennies -= (pound * self.__coinValues["pound"])
        shilling = math.floor(remainingPennies // self.__coinValues["shilling"])
        if shilling != 0:
            resultString += (" " + str(shilling) + " shillings")
            remainingPennies -= (shilling * self.__coinValues["shilling"])
        penny = math.floor(remainingPennies // self.__coinValues["penny"])
        if penny != 0:
            resultString += (" " + str(penny) + " pennies")
            remainingPennies -= (penny * self.__coinValues["penny"])
        return resultString
    
c1 = BritCoins(pound = 4, shilling = 24, penny = 3)
c2 = BritCoins(pound = 3, shilling = 4, penny = 5)
c3 = c1 + c2
c4 = c1 - c2

print(c1)
print(c2)
print(c3)
print(c4)