'''
Modify the class TreeSet described in the course material so that it can contain the same element multiple times.
This requires modifications to the methods given in the material. Also, implement the method count that returns the number of occurrences of a given element.

Implement the changes so that the class Node has a new member variable count that stores the number of occurrences of that element.
The methods in the class TreeSet should use this variable appropriately.

In a file treemany.py, implement the class TreeSet according to the following code template. You may add other methods if needed, for example the method traverse.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        itr = self.root 

        if not itr: 
            self.root = Node(value)

        while itr:
            if value < itr.value:
                if not itr.left:
                    itr.left = Node(value)
                    return 
                itr = itr.left
            elif value > itr.value:
                if not itr.right:
                    itr.right = Node(value)
                    return
                itr = itr.right 
            else:
                itr.count += 1
                return

    def __contains__(self, value):
        itr = self.root 

        if not itr:
            return False 
        
        while itr: 
            if value < itr.value:
                if not itr.left:
                    return False
                itr = itr.left
            elif value > itr.value:
                if not itr.right:
                    return False
                itr = itr.right 
            else:
                return True

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)
    
    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        if node.count > 1:
            for _ in range(node.count):    
                items.append(node.value)
        else:
            items.append(node.value)
        self.traverse(node.right, items)

    def locate(self, value):
        itr = self.root 

        if not itr:
            return None 
        
        while itr:
            if value < itr.value:
                if not itr.left:
                    return None
                itr = itr.left
            elif value > itr.value:
                if not itr.right:
                    return None
                itr = itr.right 
            else:
                return itr

    def count(self, value):
        found = self.locate(value)

        return found.count if found else 0

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(4)
    numbers.add(1)
    numbers.add(2)
    numbers.add(1)

    print(numbers) # [1, 1, 2, 4]

    print(1 in numbers) # True
    print(2 in numbers) # True
    print(3 in numbers) # False
    print(4 in numbers) # True

    print(numbers.count(1)) # 2
    print(numbers.count(2)) # 1
    print(numbers.count(3)) # 0
    print(numbers.count(4)) # 1