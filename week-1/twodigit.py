'''
Your task is to count how many numbers in the range [a,b] consist of the digits 2 and 5 only.
For example, in the range [1,100] the numbers are 2, 5, 22, 25, 52 and 55, and thus the answer is 6.
In a file twodigit.py, implement the function count_numbers that counts the desired numbers in the range. 
The function is given the parameters a and b representing the end points of the range.
Your function will be tested using many different ranges. In each test, 1 ≤ a ≤ b ≤ 10^9.
You must implement the function efficiently so that the solution is returned quickly even for long ranges.
'''

import re

def count_numbers(a, b):
    res = []
    queue = [2, 5]
    
    while queue and queue[0] <= b:
        curr = queue.pop(0)
        
        if curr >= a:
            res.append(curr)
        
        for digit in [2, 5]:
            next_num = curr * 10 + digit
            if next_num <= b:
                queue.append(next_num)
    
    return len(res)

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512