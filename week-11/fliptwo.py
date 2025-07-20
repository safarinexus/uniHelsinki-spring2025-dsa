'''
Initially the list contains the integers 1,2,...,n in order.
In each step, the first two elements of the list are moved to the end of the list in reverse order.
What is the first element of the list when all steps have been completed?
For example, starting with the list [1,2,3,4] and performing three steps, the list changes as follows:
[1,2,3,4] -> [3,4,2,1] -> [2,1,4,3] -> [4,3,1,2]
After the steps, the first element of the list is 4.
In a file fliptwo.py, implement the function find_first that takes the list size and the number of steps as parameters.
The function should return the first element of the list after the steps.
Implement the function so that each step can be performed quickly.
The function should return an answer immediately even with the last test case in the code template.
'''

import collections

def find_first(size, steps):
    q = collections.deque()

    for i in range(1, size + 1):
        q.append(i)

    while steps > 0:
        first = q.popleft()
        second = q.popleft()
        q.append(second)
        q.append(first)
        steps -= 1

    return q.popleft()

if __name__ == "__main__":
    print(find_first(4, 3)) # 4
    print(find_first(12, 5)) # 11
    print(find_first(2, 1000)) # 1
    print(find_first(99, 555)) # 11
    print(find_first(12345, 10**6)) # 12295