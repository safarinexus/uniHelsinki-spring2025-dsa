'''
You are given an object that contains a list consisting of the integers 1,2,...,n in some order.
You task is to reconstruct the list in the correct order, but you are not allowed to directly access a given position in the list.
You can only use queries asking which of the elements at given two positions is the smaller one.
You are allowed at most n⌊log_2 n⌋ such queries, and after those queries you should know the exact order of the list.
Here ⌊...⌋ means rounding down to the nearest integer. For example when n=6, you can do at most 6 x ⌊log_2 6⌋ = 12 queries.
In a file comparisons.py, implement a function find_list that takes the object as a parameter and returns the reconstructed list.
The object has a method list_size that returns the length of the list, and a method smaller(a,b) that returns True if the number at the position a is smaller than the number at the position b.
The function will be tested in various situations, where n is in the range 1...20. The function should be efficient in all such cases.
The code template includes an example implementation of the class Comparator. You can test your code using this class, but the implementation on the server is different.
You can only use the methods described here and may not try to determine the contents of the object in any other way.
'''

import math

class Comparer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = 0
        n = len(self.numbers)
        self.bound = n * math.floor(math.log2(n))

    def list_size(self):
        return len(self.numbers)

    def smaller(self, a, b):
        self.counter += 1
        #if self.counter > self.bound:
        #    raise RuntimeError("too many comparisons")
        return self.numbers[a] < self.numbers[b]

def find_list(comparer):
    size = comparer.list_size()

    if size == 1: 
        return [1]
    
    indices = list(range(size))

    def merge_sort(arr, start, end):
        if end - start <= 1:
            return arr[start:end]
        
        mid = (start + end) // 2
        left = merge_sort(arr, start, mid)
        right = merge_sort(arr, mid, end)
        
        return merge(left, right)
    
    def merge(left, right):
        res = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if comparer.smaller(left[i], right[j]):
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        res.extend(left[i:])
        res.extend(right[j:])
        
        return res
    
    sorted_indices = merge_sort(indices, 0, size)
    res = [0] * size
    
    for rank, original_index in enumerate(sorted_indices):
        res[original_index] = rank + 1
    
    return res

if __name__ == "__main__":
    comparer = Comparer([3, 1, 2, 4])
    numbers = find_list(comparer)
    print(numbers) # [3, 1, 2, 4]

    comparer = Comparer([1, 6, 2, 5, 3, 4])
    numbers = find_list(comparer)
    print(numbers) # [1, 6, 2, 5, 3, 4]