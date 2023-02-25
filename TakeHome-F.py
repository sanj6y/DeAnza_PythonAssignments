'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Unit F Take-home Assignment
'''

'''
For part 3, I couldn't get the number of rows in the bell triangle
so I just put that in the build function instead for now until I can
find out how to call the number of rows. I still have the working
code with the printing stuff in the build function.
'''

# Part One - Keyword Arguments and Default Values
def invoice(unitPrice, quantity, shipping=10, handling=5):
    total = unitPrice + quantity + shipping + handling
    up, quan, ship, handl, tot = "UNIT PRICE", "QUANTITY", "SHIPPING", "HANDLING", "TOTAL"
    print(f"{up}{quan:>10}{ship:>12}{handl:>12}{tot:>9}")
    print(f"{unitPrice:10}{quantity:>10}{shipping:>12}{handling:>12}{total:>9}")
    
invoice(20, 4, shipping=8)
invoice(15, 3, handling=15)

# Part Two - args (Variable-Length Arguments)
def printGroupMembers(groupName, *studentNames):
    print(groupName + ":")
    for name in studentNames:
        print(name)

printGroupMembers("Group A", "Li", "Audry", "Jia")
groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
printGroupMembers(groupB[0], groupB[1], groupB[2], groupB[3], groupB[4])

# Part Three - Non-rectangular (Ragged) 2D Lists
def buildBell(rows):
    bellTriangle = [[0 for p in range(rows)] for q in range(rows)]
    bellTriangle[0][0] = 1
    
    for i in range(1, rows):
        bellTriangle[i][0] = bellTriangle[i-1][i-1]
        
        for j in range(1, i+1):
            bellTriangle[i][j] = bellTriangle[i-1][j-1] + bellTriangle[i][j-1]
 
    for i in range(0, rows):
        for j in range(0, i+1):
            print(bellTriangle[i][j], end=" ")
        print()

def printBell(bellTriangle):
    for i in range(0, len(bellTriangle)):
        for j in range(0, i+1):
            print(bellTriangle[i][j], end=" ")
        print()

bellTri = buildBell(8)

'''
Execution Results:
UNIT PRICE  QUANTITY    SHIPPING    HANDLING    TOTAL
        20         4           8           5       37
UNIT PRICE  QUANTITY    SHIPPING    HANDLING    TOTAL
        15         3          10          15       43
Group A:
Li
Audry
Jia
Group B:
Sasha
Migel
Tanya
Hiroto
1 
1 2 
2 3 5 
5 7 10 15 
15 20 27 37 52 
52 67 87 114 151 203 
203 255 322 409 523 674 877 
877 1080 1335 1657 2066 2589 3263 4140
'''