'''
You are given a list of n integers. Your task is to count how many longest increasing subsequences the list has.
For example, in the list [4,1,5,6,3,4,3,8], a longest increasing subsequence contains 4 numbers.
The possible subsequences are [1,3,4,8], [1,5,6,8] and [4,5,6,8]. Thus the answer is 3 in this case.
In a file countlis.py, implement the function count_sequences that takes a list of integers as a parameter.
The function should return the number of longest increasing subsequences.
The function should be efficient when 1 ≤ n ≤ 100.
'''

def count_sequences(numbers):
    dp = {}

    max_len = 0
    for i in range(len(numbers)):
        dp[i] = []
        for j in range(i):
            if numbers[j] < numbers[i]:
                for l in dp[j]:
                    copy = l[:] 
                    copy.append(numbers[i])
                    if len(copy) > max_len:
                        max_len = len(copy)
                    if dp[i] and len(copy) > len(dp[i][0]):
                        dp[i] = []
                    dp[i].append(copy)

        if len(dp[i]) == 0:
            dp[i] = [[numbers[i]]]
            if max_len == 0:
                max_len = 1
            
    count = 0
    for k in dp:
        for m in dp[k]:
            if len(m) == max_len:
                count += 1

    return count

if __name__ == "__main__":
    print(count_sequences([1, 2, 3])) # 1
    print(count_sequences([3, 2, 1])) # 3
    print(count_sequences([1, 1, 1, 1, 1])) # 5

    print(count_sequences([1, 8, 2, 7, 3, 6])) # 1
    print(count_sequences([1, 1, 2, 2, 3, 3])) # 8
    print(count_sequences([4, 1, 5, 6, 3, 4, 3, 8])) # 3

    print(count_sequences([6, 2, 8])) # 2
    print(count_sequences([9, 2, 9, 1])) #1