'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Exercise B
'''

# String Methods
name = input("Enter a name: ")

print(name.upper())

print(len(name))

print(name[3])

name2 = name.replace("o", "x")

print(name2)

print(name)

# Counting and Finding
quote = "Believe you can and you're halfway there."

print(quote.count('a'))

index = quote.find('a')
print(index)
index = quote.find('a', index+1, )
print(index)
index = quote.find('a', index+1, )
print(index)
index = quote.find('a', index+1, )
print(index)


'''
Execution Results:
Enter a name: George Washington
GEORGE WASHINGTON
17
r
Gexrge Washingtxn
George Washington
4
13
16
28
32
'''