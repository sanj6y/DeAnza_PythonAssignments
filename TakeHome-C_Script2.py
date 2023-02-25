'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Unit C Take-home Assignment
Script 2
'''

#Second Script - Bit Operators
a,b = 9,14
print(bin(a))
print(bin(b))
print(bin(a&b))
print(bin(a|b))

'''
Explanation:
The binary value of a is 1001 and for b it's 1110. 
Using the bitwise and operator, &, makes each bit 
of the output 1 if the corresponding bit of a and 
b are both 1, and otherwise 0. This makes 1001 & 
1110 evaluate to 1000. For the bitwise or operator,
|, each bit of the output is 0 if the corresponding
bit of a and b are both 0, and otherwise it's 1. 
This makes 1001 | 1110 evaluate to 1111.
'''

'''
Execution Results:
0b1001
0b1110
0b1000
0b1111
'''