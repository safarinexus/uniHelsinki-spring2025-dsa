'''
Compare the efficiencies of the two implementations using a list that contains 10^7 randomly chosen numbers.
In this exercise, you get a point automatically when you submit the test results and the code that you used.
'''

import random 
import time

# implementation 1
def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# implementation 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

n = 10**7
print("n:", n)
random.seed(3)
numbers = [random.random() for _ in range(n)]

print('time start. calling count_even1')
start_time = time.time()
result = count_even1(numbers)
end_time = time.time()
print('time end. stopped count_even1')

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")

print('time start. calling count_even2')
start_time = time.time()
result = count_even2(numbers)
end_time = time.time()
print('time end. stopped count_even2')

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")