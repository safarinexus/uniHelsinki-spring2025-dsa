'''
Your task is to design a rule set for the robot of the previous task. 
The goal is to find out if the input string consists of two copies of the same string back to back.
For example, the robot should accept the following input strings:

00
001001
10111011

The robot should reject the following example inputs:

01
00100
10111101

You may assume that the length of the input string is 1 ... 10 symbols.
In a file robosame.py, implement the function create_rules that returns the rule set in the same form as in the preceding task.
The rule set should satisfy the same requirements as in the preceding task.
'''

def calculate(input, rules):
    # previous function
    # map structure = { (symbol, state): (new_symbol, new_state, action) }

    state = 1
    counter = 0
    ptr = 0
    parsedInput = "L" + input + "R"
    hashMap = {}

    for i in rules:
        hashMap[(i[0], i[1])] = (i[2], i[3], i[4])

    while counter < 1000:
        if ptr < 0 or ptr >= len(parsedInput): 
            return False 
        
        curr = (parsedInput[ptr], state)
        
        if curr not in hashMap:
            return False
        
        rule = hashMap[curr]

        parsedInput = parsedInput[:ptr] + rule[0] + parsedInput[ptr + 1:]
        state = rule[1]

        if rule[2] == "LEFT":
            ptr -= 1
        elif rule[2] == "RIGHT":
            ptr += 1
        elif rule[2] == "ACCEPT":
            return True
        elif rule[2] == "REJECT":
            return False
        
        counter += 1

    return False

def create_rules():
    rules = []
    # Rule format: ("L", 1, "L", 2, "RIGHT")

    rules.append(("L", 1, "L", 2, "RIGHT"))



    rules.append(("R", 3, "R", 3, "REJECT"))
    rules.append(("R", 5, "R", 5, "REJECT"))
    rules.append(("R", 7, "R", 7, "REJECT"))
    rules.append(("R", 9, "R", 9, "REJECT"))



    return rules

if __name__ == "__main__":
    rules = create_rules()

    print(calculate("00", rules)) # True
    print(calculate("001001", rules)) # True
    print(calculate("10111011", rules)) # True
    print(calculate("01", rules)) # False
    print(calculate("00100", rules)) # False
    print(calculate("10111101", rules)) # False