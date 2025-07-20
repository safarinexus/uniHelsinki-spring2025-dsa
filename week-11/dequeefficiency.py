'''
Implement a test using Python deque, where the numbers 1,2,...,n are added to the end of the deque one at a time.
Then the first element of the deque is removed n times.
Perform the test for n=10^5. Measure two times: the time for adding the elements to the deque, and the time for removing the elements from the deque.
In this task, you get a point automatically, when you report your results and the code you used, and press the submit button.
'''

import collections 
import time 

n = 10**5
q = collections.deque()

print('Append to Deque Test')
print(f'time start. appending {n}')
start_time = time.time()
for i in range(1, n + 1):
    q.append(i)
end_time = time.time()
print('time end. finished appending')

print("queue:", q)
print("time:", round(end_time - start_time, 4), "s")

print('Removing first element of Deque Test')
print(f'time start. emptying {len(q)}')
start_time = time.time()
while q:
    q.popleft()
end_time = time.time()
print('time end. finished removing')

print("queue:", q)
print("time:", round(end_time - start_time, 4), "s")
