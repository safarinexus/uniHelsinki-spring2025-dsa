'''
Using the class TreeSet of the preceding task, implement a test where the elements 1 ... n are added to the tree.
The test has two parts, both with n=1000.
In the first test, the elements are added in the order of their value, and in the second test, they are added in a random order.
In both tests, measure the height of the tree after the additions.
In this task, you get a point automatically, when you report the results and supply the code you used, and press the submit button.
'''

import time
import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.max_depth = -1

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.max_depth = 0
            return

        node = self.root
        count = 0
        while True:
            if node.value == value:
                self.max_depth = max(count, self.max_depth)
                return
            if node.value > value:
                count += 1
                if not node.left:
                    node.left = Node(value)
                    self.max_depth = max(count, self.max_depth)
                    return
                node = node.left
            else:
                count += 1
                if not node.right:
                    node.right = Node(value)
                    self.max_depth = max(count, self.max_depth)
                    return
                node = node.right


    def height(self):
        return self.max_depth
    
n = 1000 
numbers = list(range(1, n + 1))
tree1 = TreeSet()
tree2 = TreeSet()

print('time start. adding numbers to Tree1')
start_time = time.time()
for i in numbers:
    tree1.add(i)
end_time = time.time()
print('time end. finished adding numbers to Tree1')
print("time:", round(end_time - start_time, 4), "s")

random.shuffle(numbers)

print('time start. adding numbers to Tree2')
start_time = time.time()
for j in numbers:
    tree2.add(j)
end_time = time.time()
print('time end. finished adding numbers to Tree2')
print("time:", round(end_time - start_time, 4), "s")