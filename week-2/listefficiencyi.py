'''
Implement a test, where the numbers 1,2,...,n are added to the end of the list one at a time. 
Then the last element of the list is deleted n times.
Implement the test with n=10^5. 
Make two time measurements: How much time it takes to do all the additions, and how much time to do all the deletions.
In this task you get a point automatically when you fill in your measurement results and the code used in the test, and press the submit button.
'''

import time

list = []
n = 10**5

def listAdd(list, n): 
    for i in range(1, n + 1):
        list.append(i)
    
def listDelete(list, n): 
    for _ in range(n):
        list.pop()

start_time = time.time()
print("Adding elements to the list...")
listAdd(list, n)
print("listAdd finished.")
end_time = time.time()
print(list)
print("listAdd time:", round(end_time - start_time, 4), "s")

start_time = time.time()
print("Deleting elements from the list...")
listDelete(list, n)
print("listDelete finished.")
end_time = time.time()
print(list)
print("listDelete time:", round(end_time - start_time, 4), "s")
