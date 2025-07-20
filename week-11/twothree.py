'''
Initially the list contains the integer 1.
In each step, the smallest number on the list is removed (denote this number by x), and the numbers 2x and 3x are added to the end of the list if they are not on the list already.
Your task is to determine the smallest number on the list when all the steps have been completed.
For example, when the number of steps is 5, the list changes as follows:
[1] -> [2,3] -> [3,4,6] -> [4,6,9] -> [6,9,8,12] -> [9,8,12,18]
In this case, the smallest number at the end is 8.
In a file twothree.py, implement the function find_smallest that takes the nunber of steps as a parameter.
The function should return the smallest number on the list after the steps.
Implement the function so that every step is executed quickly.
The function should return immediately even with the last test case in the code template.
'''

import heapq

def find_smallest(steps):
    a = [1]

    while steps > 0:
        curr = heapq.heappop(a)
        twox = 2 * curr
        threex = 3 * curr
        if twox not in a: 
            heapq.heappush(a, twox)
        if threex not in a:
            heapq.heappush(a, threex)
        steps -= 1

    return heapq.heappop(a)


if __name__ == "__main__":
    print(find_smallest(0)) # 1
    print(find_smallest(1)) # 2
    print(find_smallest(2)) # 3
    print(find_smallest(3)) # 4
    print(find_smallest(4)) # 6
    print(find_smallest(5)) # 8

    print(find_smallest(42)) # 1296
    print(find_smallest(1337)) # 16210220612075905068
    print(find_smallest(123123)) # 47241633171870338440585357243035120029747450090811731814934867117962334088709324512562801224664331563355142646399182644605958987116029586018592281978123083613432358051028210559768563023872