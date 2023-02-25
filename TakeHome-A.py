'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Unit A Take-home Assignment
'''

import math

# Basic math and string operations
a = 3 ** 2.5
print(a)

b = 2
b += 3
print(b)

c = 12
c /= 4
print(c)

d = 5 % 3
print(d)

# Built-in functions abs, round, and min
print(abs(5-7))

print(round(3.14159, 4))

print(round(186282, -2))

print(min(6, -9, -3, 0))

# Functions from the math module
num = float(input("Enter a number: "))

print(round(math.sqrt(num), 2)) #calculating square root of num, rounding to two decimal places

print(round(math.log10(num), 2)) #calculating base-10 log of num, rounding to two decimal places

# Complex Numbers
z1 = 4 + 3j
z2 = 2 + 2j
z3 = z1 * z2
print(z3)

'''
Execution Results:
15.588457268119896
5
3.0
2
2
3.1416
186300
-9
Enter a number: 7.6
2.76
0.88
(2+14j)
'''