'''
Consider the same process as in the previous task, but now the goal is to count the number of rounds efficiently.
For example, when the list is [2,1,4,7,5,3,6,8], the rounds are [1], [2,3], [4,5,6] and [7,8]. Thus the number of rounds is four.
In a file fastrounds.py, implement the function count_rounds that takes the list as a parameter and returns the number of rounds.
In this task, the list may be so long that it would be too slow to go through the whole list in each round. 
Your task is to find a more efficient way of computing the number of rounds.
In the last test case of the code template, the list contains the numbers 1,2,...,10^5 in descending order and the number of rounds is 10^5. 
Your function should be fast in this test case too.
'''

def count_rounds(numbers):
    track = set()
    res = []

    for i in range(len(numbers)):
        track.add((numbers[i], i))
    
    sortedTrack = sorted(track)

    curr = []
    prev = -1
    for i in sortedTrack:
        if i[1] < prev: 
            res.append(curr)
            curr = []

        curr.append(i[0])
        prev = i[1]

    res.append(curr)

    return len(res)

if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000