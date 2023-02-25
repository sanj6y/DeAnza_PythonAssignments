#Sanjay Chandrasekar
#Exercise C
#4/22/21

import copy

list1 = [2, 4.1, 'hello']
list2 = list1
list3 = copy.deepcopy(list1)

print(list1 == list2)
print(list1 == list3)
print(list2 == list3)

print(list1 is list2)
print(list1 is list3)
print(list2 is list3)

print(id(list1))
print(id(list2))
print(id(list3))

list1.append(8)
list2.insert(1, 'goodbye')
list3.remove(list3[0])

print(list1)
print(list2)
print(list3)

#list1 and list2 are practically the same list with two different names, 
#so all operations under list1 and list2 are done to the same list

'''
Execution Results:
True
True
True
True
False
False
140193881675136
140193881675136
140193881619712
[2, 'goodbye', 4.1, 'hello', 8]
[2, 'goodbye', 4.1, 'hello', 8]
[4.1, 'hello']
'''