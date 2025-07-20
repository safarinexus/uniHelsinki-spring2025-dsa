'''
The list has n integers. Implement a test, where the sum of the n/10 smallest elements of the list is computed.
Implement the test in three different ways:

Sort the list and compute the sum of the first n/10 elements.
Create an empty heap and move the elements of the list into the heap one at a time using the function heapq.heappush. Then extract n/10 elements from the heap and add them up.
Turn the list into a heap in linear time using the function heapq.heapify. Then extract n/10 elements from the heap and add them up.

Perform the test using n=10^7 with each element chosen randomly from the range 1 ... 10^9. Check that each implementation returns the same answer.
In this task, you get a point automatically, when you report your results and the code you used, and push the submit button.
'''

import heapq
import time 
import random

random.seed(42)
n = 10**7
input = [random.randint(1, 10**9) for _ in range(n)]

print('time start. begin algo 1 test')
start_time = time.time()    
a = sorted(input)
result = 0
for i in range(n//10):
    result += a[i]
end_time = time.time()
print('time end. stopped algo 1 test')

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")

print('time start. begin algo 2 test')
start_time = time.time()
result = 0
b = []
for i in input:
    heapq.heappush(b, i)
for i in range(n//10):
    result += heapq.heappop(b)
end_time = time.time()
print('time end. stopped algo 2 test')

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")

print('time start. begin algo 3 test')
start_time = time.time()
heapq.heapify(input)
result = 0
for i in range(n//10):
    result += heapq.heappop(input)
end_time = time.time()
print('time end. stopped algo 3 test')

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")
