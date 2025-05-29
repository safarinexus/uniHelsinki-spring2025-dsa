'''
Your task is to count the number of leaves in a given tree.

In a file leaves.py, implement the function count_leaves that takes a reference to the root of the tree as a parameter and returns the number of leaves.
'''

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []

    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"

def count_leaves(node):
    pass

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_leaves(tree1)) # 4

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_leaves(tree2)) # 1

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_leaves(tree3)) # 3