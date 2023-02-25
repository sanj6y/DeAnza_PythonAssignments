'''
Sanjay Chandrasekar
CIS 41A Spring 2021
Unit G Take-home Assignment
'''

# Part One - Reading a Data File
stateAbr = ""
statePop = 0

with open("States.txt") as f:
    for line in f:
        s = line.split()
        if(s[1] == "Midwest"):
            if(int(s[2]) > int(statePop)):
                stateAbr = s[0]
                statePop = s[2]

print("Highest population state in the Midwest is: " + stateAbr + " " + statePop)

# Part Two - A Dictionary of Lists
presDict = dict()
with open("USPresidents.txt") as f:
    for line in f:
        state = line.split()
        if state[0] in presDict:
            presDict[state[0]].append(state[1])
        else:
            presDict[state[0]] = [state[1]]
keyValPair = ""
length = 0
for state in presDict:
    if(len(presDict[state]) > length):
        length = len(presDict[state])
        keyValPair = state
print("The state with the most presidents is " + keyValPair + " with " + str(length) + " presidents.")
for presList in presDict[keyValPair]:
    print(presList)
    
# Part Three - Dictionary Keys and Sets
presidentDict = dict()
presCount = 1
with open("USPresidents.txt") as f:
    for line in f:
        state = line.split()
        if state[0] in presidentDict:
            presidentDict[state[0]] += 1
        else:
            presidentDict[state[0]] = presCount
States = {"CA","TX","FL","NY","IL","PA","OH","GA","NC","MI"}
populousStates = set()
for state in States:
    if(state in presidentDict):
        populousStates.add(state)
print(str(len(populousStates)) + " of the 10 high population states have had presidents born in them:")
for state in populousStates:
    if(state in presidentDict):
        print(state + " " + str(presidentDict[state]))

'''
Execution Results:
Highest population state in the Midwest is: IL 12802000
The state with the most presidents is VA with 8 presidents.
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor
8 of the 10 high population states have had presidents born in them:
IL 1
NY 5
NC 2
GA 1
OH 7
CA 1
PA 1
TX 2
'''