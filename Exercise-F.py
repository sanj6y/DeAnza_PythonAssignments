'''
Sanjay Chandrasekar
Exercise F
Spring 2021
'''

# Part One - Using a main function, Docstrings
def hello():
    '''Prints "Hello World"'''
    print("Hello World")

# Part Two - Error Handling
def printListElement(list, listIndex):
    '''prints element in list, throws error if list index out of range'''
    try:
        print(list[listIndex])
    except IndexError:
        print("Error: invalid index number")
        
# Part Three - How Python function arguments are treated
def byVal(num):
    '''prints ID of argument, adds 7 to it, then prints ID again'''
    print(id(num))
    num += 7
    print(id(num))
    
def byRef(list):
    '''prints ID of last element in list, adds 7 to it, prints ID again'''
    print(id(list[-1]))
    list[-1] += 7
    print(id(list[-1]))

# Main method
def main():
    # Part one stuff
    hello()
    print(hello.__doc__)
    
    # Part two stuff
    myList = [*range(0, 3)]
    printListElement(myList, 3)
    
    # Part three stuff
    myInt = 3
    myList2 = [*range(0, 3)]
    print(id(myInt))
    print(id(myList2))
    print(id(myList2[-1]))
    byVal(myInt)
    byRef(myList2)
    print(id(myInt))
    print(id(myList2))
    print(id(myList2[-1]))

#Calling main method
if __name__ == "__main__":
    main()
    
'''
Execution Results:
Hello World
Prints "Hello World"
Error: invalid index number
4314687904
140281152870656
4314687872
4314687904
4314688128
4314687872
4314688096
4314687904
140281152870656
4314688096
'''