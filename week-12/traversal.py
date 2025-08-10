'''
The binary search tree implementation in the course material has the method __repr__ that calls the recursive function traverse to construct a list of all the elements from the smallest to the largest in linear time.

Your task is to reimplement the method __repr__ without using recursion. The method should produce the same output as before, and still run in linear time.

You are not allowed to compare the element values. You must construct the list in the correct order based on only the element locations in the tree.

In a file traversal.py, implement the class TreeSet according to the following code template. You are not allowed to add methods other than the ones in the code template.
'''
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def __repr__(self):
        res = []
        stack = []
        curr = self.root
    
        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            
            res.append(curr.value)
            
            curr = curr.right
            
        return str(res)



if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(4)
    numbers.add(1)
    numbers.add(2)
    numbers.add(5)
    numbers.add(8)
    numbers.add(7)

    print(numbers) # [1, 2, 4, 5, 7, 8]