'''
In the course material, there is an example for week 4 of an algorithm using a dictionary for counting the rounds needed to collect numbers from a list. 
Earlier in an exercise for week 2, the same task was solved using a list instead of a dictionary.
The auxiliary data structure used in the task can be either a list or a dictionary, because a number can be used either as a list index or as a dictionary key. 
How does the choice of the data structure affect the efficiency of the algorithm?
Compare the efficiency of the two implementations for an input list containing the numbers 1,2,...,10^7 in a random order.
In this task you get a point automatically, when you fill in your results and the code you used, and press the submit button.
'''

import random 
import time

def usingList(numbers): 
    n = len(numbers)
    pos = [0] * (n+1)

    for i in range(n):
        pos[numbers[i]] = i

    rounds = 1
    for number in range(2, n+1):
        if pos[number] < pos[number - 1]:
            rounds += 1

    return rounds

def usingDict(numbers): 
    n = len(numbers)
    
    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i
        
    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

random.seed(42)
numbers = random.sample(range(1, 10**7 + 1), 10**7)

print('time start. calling usingList')
start_time = time.time()
result = usingList(numbers)
end_time = time.time()
print('time end. stopped usingList')

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")

print('time start. calling usingDict')
start_time = time.time()
result = usingDict(numbers)
end_time = time.time()
print('time end. stopped usingDict')

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")