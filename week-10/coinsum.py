'''
Your task is to check if a given sum can be made using a given set of coins.
For example, the sum 13 can be made using the coins [1,2,5]   (e.g., 5+5+2+1), but not using the coins [2,4,6].
In a file coinsum.py, implement the function can_create that takes a list of coins and the target sum as parameters.
The function should return True if the sum can be achieved, and False otherwise.
Implement the function efficiently using dynamic programming similarly to the examples in the course material.
'''

def can_create(coins, target):
    pass

if __name__ == "__main__":
    print(can_create([1, 2, 5], 13)) # True
    print(can_create([2, 4, 6], 13)) # False
    print(can_create([1], 42)) # True
    print(can_create([2, 4, 6], 42)) # True
    print(can_create([3], 1337)) # False
    print(can_create([3, 4], 1337)) # True