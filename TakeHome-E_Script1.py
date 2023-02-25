'''
Sanjay Chandrasekar
CIS 41A   Spring 2021
Unit E take-home assignment
First Script
'''

# Decision Making

name = input("Please enter the plant name: ")
type = input("Please enter the plant type: ")
height = int(input("Please enter the plant height: "))

if type.lower() == "vegetable":
    print("A " + name + " can be planted in the Vegetable Garden.")
elif type.lower() == "flower":
    if height >= 3 and height <= 6:
        print("A " + name + " can be planted in the Low Garden or the High Garden.")
    elif height < 3 and height > 0:
        print("A " + name + " can be planted in the Low Garden.")
    elif height > 3 and height <= 6:
        print("A " + name + " can be planted in the High Garden.")
    else:
        print("A " + name + " cannot be planted in any garden.")
else:
    print("A " + name + " cannot be planted in any garden.")
    
'''
Execution Results:
Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in the Low Garden or the High Garden.
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai cannot be planted in any garden.
Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
A Carrots can be planted in the Vegetable Garden.
Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
A Corn can be planted in the Vegetable Garden.
Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in the Low Garden or the High Garden.
Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower cannot be planted in any garden.
'''
