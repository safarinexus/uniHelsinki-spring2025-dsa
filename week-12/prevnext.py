'''
Implement the binary search tree as described in the course material, but with the addition of the methods prev and next that return the preceding and following elements.
Implement the methods as described in the course material.

The method prev should return the largest element that is smaller than the element given as a parameter.
Similarly, the method next should return the smallest element that is larger than the parameter.
If such an element does not exists, the methods should return None.

In a file prevnext.py, implement the class TreeSet according to the following code template.
Your task is to fill in the methods prev and next.
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

    def prev(self, value):
        curr = self.root
        result = None
        
        while curr:
            if curr.value < value:
                result = curr.value
                curr = curr.right
            else:
                curr = curr.left
        
        return result

    def next(self, value):
        curr = self.root
        result = None
        
        while curr:
            if curr.value > value:
                result = curr.value
                curr = curr.left
            else:
                curr = curr.right
        
        return result

if __name__ == "__main__":
    numbers = TreeSet()

    numbers.add(3)
    numbers.add(2)
    numbers.add(5)
    numbers.add(7)

    print(numbers.prev(5)) # 3
    print(numbers.prev(4)) # 3
    print(numbers.prev(3)) # 2
    print(numbers.prev(2)) # None

    print(numbers.next(4)) # 5
    print(numbers.next(5)) # 7
    print(numbers.next(6)) # 7
    print(numbers.next(7)) # None