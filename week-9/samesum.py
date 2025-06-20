'''
You are given a list of integers. 
Your task is to find if the list can be partitioned into two lists so that both lists have the same sum.
For example, the list [1,2,3,4] can be partitioned into the lists [1,4] and [2,3], both of which have the sum 5.
On the other hand, the list [1,2,3,5] cannot be partitioned into two lists with the same sum.
In a file samesum.py, implement the function check_sum that takes a list of integers as a parameter.
The function should return True if a valid partitioning exists, and False otherwise.
You may assume that the length of the list is in the range 1...10.
The function should be efficient in all such cases.
'''

import itertools

def check_sum(numbers):
    total_sum = sum(numbers)
    choices = itertools.product([False, True], repeat=len(numbers))

    for choice in choices:
        choice_sum = 0

        for pos in range(len(numbers)):
            if choice[pos]:
                choice_sum += numbers[pos]

        if choice_sum * 2 == total_sum:
            return True

    return False

if __name__ == "__main__":
    print(check_sum([1, 2, 3, 4])) # True
    print(check_sum([1, 2, 3, 5])) # False
    print(check_sum([0])) # True
    print(check_sum([2, 2])) # True
    print(check_sum([2, 4])) # False
    print(check_sum([1, 5, 6, 3, 5])) # True
    print(check_sum([1, 5, 5, 3, 5])) # False
    print(check_sum([10**9, 2*10**9, 10**9])) # True
    print(check_sum([1, 1, 1, 1, 1, 1, 1, 1, 1, 123])) # False