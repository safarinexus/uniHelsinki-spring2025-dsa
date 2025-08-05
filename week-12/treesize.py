'''
Implement the binary search tree as described in the course material, but with the addition of the method __len__ that returns the number of elements stored in the tree. 
Then the function len can be used for finding the size of the set.

Start with the implementation in the course material and add the member variable size to the class.
The value of the variable is updated each time a new element is added to the tree using the method add.
Then the method __len__ can simply return the value of the variable.

In a file treesize.py, implement the class TreeSet according to the following code template.
The template already contains the variable size and the method __len__.
Your task is to fill in the method add. You can take the implementation in the course material and modify it appropriately.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.size += 1
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    self.size += 1
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    self.size += 1
                    return
                node = node.right

    def __len__(self):
        return self.size

if __name__ == "__main__":
    numbers = TreeSet()
    print(len(numbers)) # 0
    numbers.add(1)
    print(len(numbers)) # 1
    numbers.add(2)
    print(len(numbers)) # 2
    numbers.add(3)
    print(len(numbers)) # 3
    numbers.add(2)
    print(len(numbers)) # 3