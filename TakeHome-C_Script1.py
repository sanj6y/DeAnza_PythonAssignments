'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Unit C Take-home Assignment
Script 1
'''

#First Script - Working with Lists
list1 = []
for i in range(1, 7, 2):
    list1.append(i)
list2 = [1, 2, 3, 4]
list3 = list1 + list2
print(list3)
print(3 in list3)
print(list3.count(3))
print(list3.index(3))
first3 = list3.pop(list3.index(3))
print(first3)
list4 = sorted(list3)
print(list3)
print(list4)

print(list3[2:-1])
print(len(list3))
print(max(list3))
list3.sort()
print(list3)
list5 = [list1, list2]
print(list5)
print(list5[1][-1])

'''
Execution Results:
[1, 3, 5, 1, 2, 3, 4]
True
2
1
3
[1, 5, 1, 2, 3, 4]
[1, 1, 2, 3, 4, 5]
[1, 2, 3]
6
5
[1, 1, 2, 3, 4, 5]
[[1, 3, 5], [1, 2, 3, 4]]
4
'''