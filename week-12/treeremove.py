'''
Implement the binary search tree as described in the course material, but with the addition of the method remove that removes an element from the tree.
Implement the method as described in the course material.

The method should handle the cases, where the node to be removed has no children, where the node has one child, and where the node has two children.
If the element to be removed is not in the tree, the method does nothing.

In a file treeremove.py, implement the class TreeSet according to the following code template.
Your task is to fill in the method remove.
You may add other methods if needed, for example the method next.
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

    def remove(self, value):
        pass

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(3)
    numbers.add(2)
    numbers.add(5)
    numbers.add(7)
    print(numbers) # [2, 3, 5, 7]
    
    numbers.remove(3)
    print(numbers) # [2, 5, 7]

    numbers.remove(7)
    print(numbers) # [2, 5]

    numbers.remove(2)
    print(numbers) # [5]

    numbers.remove(5)
    print(numbers) # []