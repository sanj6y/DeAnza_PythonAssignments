
#Sanjay Chandrasekar
#CIS 41A Spring 2021
#Exercise A

width = input('enter width: ')
height = input('enter height: ')
area = float(width) * float(height)

print("width: " + width)
print("height: " + height)
print("area: " + str(area))
print("")

width = float(width)//2
height = float(height)//2
area = height * width

print("width: " + str(width))
print("height: " + str(height))
print("area: " + str(area))

"""
Execution Results:
width: 7.1
height: 2.9
area: 20.59

width: 3.0
height: 1.0
area: 3.0

"""