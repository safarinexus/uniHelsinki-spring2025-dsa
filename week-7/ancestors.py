'''
Your task is to find out if a node a is an ancestor of a node b in a given tree.
This means that one can get from the node a to the node b by going downwards in the tree, i.e., the node b is in the subtree of the node a.
For example, in the tree below, the node 1 is an ancestor of the node 3 and the node 2 is an ancestor of the node 6.

In a file ancestors.py, implement the function ancestor, whose parameters are a reference to the root of a tree and the node identifiers a and b. The function returns True or False.
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

def ancestor(node, a, b):
    aFlag = False

    def find(node, aFlag):
        if node.value == a:
            aFlag = True 

        if node.value == b and not aFlag:
            return False 
        
        if node.value == b and aFlag: 
            return True 
        
        if not node.children and not aFlag and node.value != b:
            return False 

        for i in node.children:
            if find(i, aFlag):
                return True
    
        return False

    return find(node, aFlag)


if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(ancestor(tree1, 1, 3)) # True
    print(ancestor(tree1, 2, 6)) # True
    print(ancestor(tree1, 3, 1)) # False
    print(ancestor(tree1, 5, 6)) # False
    print(ancestor(tree1, 3, 3)) # True

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(ancestor(tree2, 1, 4)) # True
    print(ancestor(tree2, 3, 2)) # False

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(ancestor(tree3, 1, 2)) # True
    print(ancestor(tree3, 1, 1)) # True
    print(ancestor(tree3, 2, 1)) # False
    print(ancestor(tree3, 5, 5)) # False