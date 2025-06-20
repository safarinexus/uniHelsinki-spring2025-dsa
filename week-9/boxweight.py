'''
Your task is to pack a set of products into boxes. You are given the weights of the products and a maximum weight that can be packed into one box.
How many boxes do you need at least?
For example, if the product weights are [2,3,3,5] and the maximum weight in a box is 7, at least two boxes is needed:

Box 1: products of weight 2 and 5 (total weight 7)
Box 2: products of weight 3 and 3 (total weight 6)

In a file boxweight.py, implement the function min_count that takes the list of product weights and the maximum box weight as parameters.
The function should return the smallest number of boxes needed. If no packing is possible, the function should return -1.
You may assume that the number of products is in the range 1...8. The function should be efficient in all such cases.
'''

def min_count(weights, max_weight):
    res = 0
    visited = set()

    for i in range(len(weights) - 1, 0, -1):
        if weights[i] > max_weight:
            return -1

        if (max_weight - weights[i]) in weights:
            for idx, j in enumerate(weights):
                if j == max_weight - weights[i] and idx not in visited:
                    res += 1
                    visited.add(i)
                    visited.add(idx)
        
    return res
            


if __name__ == "__main__":
    print(min_count([2, 3, 3, 5], 7)) # 2
    print(min_count([2, 3, 3, 5], 6)) # 3
    print(min_count([2, 3, 3, 5], 5)) # 3
    print(min_count([2, 3, 3, 5], 4)) # -1

    print(min_count([], 1)) # 0
    print(min_count([1], 1)) # 1
    print(min_count([1, 1, 1, 1], 1)) # 4
    print(min_count([1, 1, 1, 1], 4)) # 1

    print(min_count([3, 4, 1, 2, 3, 3, 5, 9], 10)) # 3