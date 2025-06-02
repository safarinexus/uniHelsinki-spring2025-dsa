'''
Your task is to count the number of nodes at a given depth in a tree.
For example, in the following tree, the node 1 is at the depth 0, the nodes 4, 5 and 2 are at the depth 1, and the nodes 3, 7 and 6 are at the depth 2.

In a file depths.py, implement the function count_nodes that takes a reference to the root of the tree and the desired depth as parameters and returns the node count.
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

def count_nodes(node, depth):
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children else []
 
    def __repr__(self):
        if self.children == []:
            return f"Node({self.value})"
        else:
            return f"Node({self.value}, {self.children})"
 
def count_nodes(node, depth):
    if depth == 0:
        return 1
    
    count = 0
    for i in node.children:
        count += count_nodes(i, depth - 1)

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(count_nodes(tree1, 0)) # 1
    print(count_nodes(tree1, 1)) # 3
    print(count_nodes(tree1, 2)) # 3
    print(count_nodes(tree1, 3)) # 0

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(count_nodes(tree2, 0)) # 1
    print(count_nodes(tree2, 1)) # 1
    print(count_nodes(tree2, 2)) # 1
    print(count_nodes(tree2, 3)) # 1
    print(count_nodes(tree2, 4)) # 0

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(count_nodes(tree3, 0)) # 1
    print(count_nodes(tree3, 1)) # 3
    print(count_nodes(tree3, 2)) # 0