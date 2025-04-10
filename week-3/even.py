'''
You are given a list of integers. Your task is to count how many sublists contain only even numbers.
For example, the sublists of the list [2,4,1,6] are:
[2], [4], [1], [6], [2,4], [4,1], [1,6], [2,4,1], [4,1,6], [2,4,1,6]
In this case, the desired answer is 4, because the sublists with only even numbers are [2], [4], [6] and [2,4].
In a file even.py, implement the function count_sublists that takes the list of numbers as a parameter and returns the count of even only sublists.
You must implement an efficient solution with a time complexity O(n).
You cannot afford to go through all sublists separately. Your solution should go through the input list only once.
In the last test case of the following code template, the list contains 10^5 copies of the number 2 and thus all sublists consist of even numbers only.
Your function should finish quickly in this test case too.
'''

def count_sublists(numbers):
    res = 0
    count = 0
    
    for i in numbers:
        if i % 2 == 0:
            count += 1
            res += count
        else:
            count = 0

    return res


if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000