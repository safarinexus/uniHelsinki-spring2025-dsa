'''
In the course material, there is an example for week 4 of an algorithm using a dictionary for finding a mode of a list.
Another efficient way to find a mode is to sort the elements and go through the list from left to right while keeping track of how many times each element is repeated.
Compare the efficiency of the above two solutions for an input list containing 10^7 random numbers in the range 1...1000.
In this task you get a point automatically, when you fill in your results and the code you used, and press the submit button.
'''

import random 
import time 

def usingDict(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1
        
        if count[x] > count[mode]:
            mode = x
 
    return mode

def usingSort(numbers):
    working = sorted(numbers)
    high, count, mode = 0, 0, 0
    prev = numbers[0]

    for i in range(len(working)):
        count += 1

        if working[i] != prev or i == len(working) - 1:
            if count > high:
                high = count 
                mode = prev 
            
        prev = working[i]

    return mode

random.seed(42)
numbers = [random.randint(1, 1000) for _ in range(10**7)]

print('time start. calling usingDict')
start_time = time.time()
result = usingDict(numbers)
end_time = time.time()
print('time end. stopped usingDict')

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")

print('time start. calling usingSort')
start_time = time.time()
result = usingSort(numbers)
end_time = time.time()
print('time end. stopped usingSort')

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")