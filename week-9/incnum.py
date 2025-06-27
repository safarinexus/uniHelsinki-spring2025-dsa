'''
An integer is ascending if each digit is greater than or equal to the preceding digit.
For example, the integers 2, 347 and 25568 are ascending.
Your task is to count how many ascending integers of a given length can be formed using a given set of digits.
For example, when the length is 3 and the allowed digits are 1, 2 and 3, the desired answer is 10, because in this case the valid ascending integers are 111, 112, 113, 122, 123, 133, 222, 223, 233 and 333.
In a file incnum.py, implement the function count_numbers that takes the length and the allowed digits as parameters.
The function should return the number of ascending integers.
The function should be efficient when the length of the integer is in the range 1...10.

Notice that an ascending integer may not have leading zeros if the length is two or more.
For example, 00 and 012 are not valid ascending integers, but 0 is an ascending integer.
'''
import itertools 

def count_numbers(length, numbers):
    count = 0

    for seq in itertools.combinations_with_replacement(numbers, length):
        if seq[0] == '0' and len(seq) > 1:
            continue
        else:
            count += 1

    return count

if __name__ == "__main__":
    print(count_numbers(3, "123")) # 10
    print(count_numbers(5, "1")) # 1
    print(count_numbers(2, "137")) # 6
    print(count_numbers(8, "25689")) # 495
    print(count_numbers(1, "0")) # 1
    print(count_numbers(2, "0")) # 0
    print(count_numbers(10, "12")) # 11
    print(count_numbers(10, "123456789")) # 43758

