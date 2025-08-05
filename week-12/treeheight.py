'''
Implement a binary search tree as described in the course material, but with the addition of the method height that returns the height of the tree.
The height of a tree is the largest depth of any node in the tree.
In other words, the height is the number of edges on the longest path from the root to a leaf.
If the tree is empty, the height is -1.
Start with the implementation in the course material and add the member variable max_depth to the class.
The value of the variable is updated if needed with each call to the method add.
The method height can simply return the value of the variable.
In a file treeheight.py, implement the class TreeSet according to the following code template.
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

if __name__ == "__main__":
    numbers = TreeSet()
    print(numbers.height()) # -1
    numbers.add(2)
    print(numbers.height()) # 0
    numbers.add(1)
    print(numbers.height()) # 1
    numbers.add(3)
    print(numbers.height()) # 1
    numbers.add(4)
    print(numbers.height()) # 2