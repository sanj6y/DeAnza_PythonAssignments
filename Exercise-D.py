'''
Sanjay Chandrasekar
Exercise D
5/1/21
'''

# 1. Dictionary Basics

dessert = {
    "apple" : "sauce",
    "peach" : "cobbler",
    "carrot" : "cake",
    "strawberry" : "sorbet",
    "banana" : "cream pie"
}

dessert["mango"] = "sticky rice"

dessert["strawberry"] = "shortcake"

del dessert["carrot"]

print(dessert["apple"])

print("banana" in dessert)

print("pear" in dessert)

print(dessert.keys())

print(dessert.values())

print(dessert.items())
    
# 2. Combining Dictionaries

capitols1 = {
    "Alabama" : "Montgomery",
    "Alaska" : "Juneau",
    "Arizona" : "Phoenix",
    "Arkansas" : "Little Rock",
    "California" : "Sacramento"
}

capitols2 = {
    "California" : "Sac.",
    "Colorado" : "Denver",
    "Connecticut" : "Hartford"
}

capitols1.update(capitols2)

print(sorted(capitols1.values()))

# 3. Sets Basics

class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}

class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}

class1.add("John")

print(sorted(class1.intersection(class2)))
print(sorted(class1.union(class2)))
print("Sasha" in class1)

'''
Execution Results:
sauce
True
False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', 'cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
['Audry', 'Migel', 'Tanya']
['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
False
'''