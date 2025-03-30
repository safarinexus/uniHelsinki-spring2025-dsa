'''
You are given a list of numbers and your task is to compute the sum of every sublist of a given size from left to right.
For example, when the list is [1,2,3,4,5] and the sublist size is 3, the sublists are [1,2,3], [2,3,4] and [3,4,5]. 
The sums of the sublists are 6, 9 and 12.
In a file listsum.py, implement the function find_sum that returns the sublist sums as a list.
The function takes a list of numbers and the sublist size as a parameter.
You need to design an efficient algorithm that does not compute each sublist sum separately.
A better way is to utilize to the preceding sum when computing the next sum.
The last test case of the following code template has 10^5 numbers and the sublist size is 10^4.
Your function should work quickly in this test case too.
'''

def find_sums(numbers, size):
    if size == 1:
        return numbers
    
    res = [sum(numbers[:size])]
    ptr = 0
    total = res[0]
 

    for i in range(size, len(numbers)):
        total = total - numbers[ptr] + numbers[i]
        ptr += 1
        res.append(total)


    return res
        


if __name__ == "__main__":
    print(find_sums([1], 1)) # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6)) # [27, 30, 27]

    print(find_sums([1, 2, 3, 4, 5], 1)) # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2)) # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3)) # [6, 9, 12]
    print(find_sums([1, 2, 3, 4, 5], 4)) # [10, 14]
    print(find_sums([1, 2, 3, 4, 5], 5)) # [15]

    numbers = list(range(10**5))
    sums = find_sums(numbers, 10**4)
    print(sums[5]) # 50045000
    print(sums[42]) # 50415000
    print(sums[1337]) # 63365000