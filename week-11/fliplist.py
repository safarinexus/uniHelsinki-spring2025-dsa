'''
Your task is to implement a list data structure that supports efficient addition to the beginning and to the end of the list, and the reversal of the order of the elements.

In a file fliplist.py, implement a class FlipList with the following methods:

add_first(x): add the element x to the beginning of the list
add_last(x): add the element x to the end of the list
flip(): reverse the order of the elements
All the methods above should be efficient. In addition, the method __repr__ should return the contents of the list as a string as shown in the following examples.
'''

import collections

class FlipList:
    def __init__(self):
        self.deque = collections.deque()
        self.flipped = False

    def __repr__(self):
        if not self.flipped:
            return str(list(self.deque))
        else:
            return str(list(reversed(self.deque)))

    def add_first(self, x):
        if not self.flipped:
            self.deque.appendleft(x)
        else:
            self.deque.append(x)

    def add_last(self, x):
        if not self.flipped:
            self.deque.append(x)
        else:
            self.deque.appendleft(x)

    def flip(self):
        self.flipped = not self.flipped

if __name__ == "__main__":
    numbers = FlipList()

    numbers.add_last(1)
    numbers.add_last(2)
    numbers.add_last(3)
    print(numbers) # [1, 2, 3]

    numbers.add_first(4)
    print(numbers) # [4, 1, 2, 3]

    numbers.flip()
    print(numbers) # [3, 2, 1, 4]

    numbers.add_last(5)
    print(numbers) # [3, 2, 1, 4, 5]