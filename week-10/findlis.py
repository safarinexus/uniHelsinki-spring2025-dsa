'''
You are given a list of n integers.
Your task is to find the longest increasing subsequence of the list.
If there are multiple subsequences of equal length, you can choose any of them.
For example, in the list [4,1,5,6,3,4,3,8], the longest increasing subsequence contains 4 numbers.
The valid subsequences are [1,3,4,8], [1,5,6,8] and [4,5,6,8].
In a file findlis.py, implement the function find_sequence that takes a list of integers as a parameter.
The function should return a longest increasing subsequence of the list.
The function should be efficient when 1 ≤ n ≤ 100.
'''

def find_sequence(numbers):
    res = { 0 : [numbers[0]] }

    if len(numbers) < 2:
        return [numbers[0]]
    else:
        max = []
        for i in range(1, len(numbers)):
            res[i] = [numbers[i]]

            j = i - 1
            curr = []
            while j >= 0:
                if numbers[j] < numbers[i]:
                    if len(res[j]) > len(curr):
                        curr = res[j][:]
                j -= 1
            
            curr.append(numbers[i])
            res[i] = curr
            if len(res[i]) >= len(max):
                max = res[i]
        
        return max

if __name__ == "__main__":
    print(find_sequence([1, 2, 3])) # [1, 2, 3]
    print(find_sequence([3, 2, 1])) # [1]
    print(find_sequence([1, 1, 1, 1, 1])) # [1]

    print(find_sequence([1, 8, 2, 7, 3, 6])) # [1, 2, 3, 6]
    print(find_sequence([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find_sequence([4, 1, 5, 6, 3, 4, 3, 8])) # [1, 3, 4, 8]