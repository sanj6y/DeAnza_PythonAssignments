'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Unit H Take-home Assignment
Script 1
'''

# First Script - Variable-Length Keyword Arguments - kwargs
def overseerSystem(**kwargs):
    if "temperature" in kwargs:
        if kwargs["temperature"] > 500:
            print("Warning: temperature is " + str(kwargs["temperature"]))
    if "CO2level" in kwargs:
        print("Warning: CO2level is " + str(kwargs["CO2level"]))
    if "miscError" in kwargs:
        print("Misc error #" + str(kwargs["miscError"]))
        
overseerSystem(temperature = 550)
overseerSystem(temperature = 475)
overseerSystem(temperature = 450, miscError = 404)
overseerSystem(CO2level = .18)
overseerSystem(CO2level = 0.2, miscError = 418)