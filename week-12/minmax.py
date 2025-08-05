'''
Implement the binary search tree as described in the course material, but with the addition of the methods min and max that return the smallest and the largest elements.
Implement the methods as described in the course material.

In a file minmax.py, implement the class TreeSet according to the following code template.
Your task is to fill in the methods min and max.
You are not allowed to add methods other than the ones in the code template.
'''

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

    def min(self):
        curr = self.root
        if not curr:
            return None

        while True: 
            if not curr.left: 
                return curr.value
            curr = curr.left

    def max(self):
        curr = self.root
        if not curr:
            return None

        while True: 
            if not curr.right: 
                return curr.value
            curr = curr.right

if __name__ == "__main__":
    numbers = TreeSet()

    print(numbers.min()) # None
    print(numbers.max()) # None

    numbers.add(3)
    print(numbers.min()) # 3
    print(numbers.max()) # 3

    numbers.add(4)
    print(numbers.min()) # 3
    print(numbers.max()) # 4

    numbers.add(1)
    print(numbers.min()) # 1
    print(numbers.max()) # 4