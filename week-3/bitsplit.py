'''
You are given a string where each character is 0 or 1.
Your task is to count how many ways the string can be split into two parts so that in both parts the number of 0s is equal to the number of 1s.
For example, the string 010101 has two valid splits: 01+0101 and 0101+01. 
In the part 01, both 0 and 1 occur once, and in the part 0101, both 0 and 1 occur twice.
In a file bitsplit.py, implement the function count_splits that takes the list of numbers as a parameter and returns the count of valid splits.
You must implement an efficient solution with a time complexity O(n).
For example, you cannot afford to test each possible split position separately.
In the last test case of the following code template, the string contains 10^5 copies of the string 01.
Your function should finish quickly in this test case too.
'''

def count_splits(sequence):
    res = 0
    
    if len(sequence) < 2:  
        return res

    zeroCount = sequence.count("0")
    oneCount = sequence.count("1")
    
    zeroCurr = 0
    oneCurr = 0

    for i in range(len(sequence) - 2):
        if sequence[i] == '0':
            zeroCurr += 1
        else:
            oneCurr += 1

        if zeroCurr == oneCurr and abs(zeroCount - zeroCurr) == abs(oneCount - oneCurr):
            res += 1

    return res

if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999