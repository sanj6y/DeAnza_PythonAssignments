'''
Sanjay Chandrasekar
CIS 41A   Spring 2021
Unit E take-home assignment
Third Script
'''

# Part One - Looping with String Methods

quote = "Believe you can and you're halfway there."
for i in range(len(quote)):
    if (quote[i] == 'a'):
        print(f"a found at index {i}")
        
# Part Two - Nested Loops

rows = int(input("enter number of rows: "))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(i*j, end = ' ')
    print()