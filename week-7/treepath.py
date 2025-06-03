'''
Your task is to find a path from a node a to a node b in a given tree. 
A path is a route in the tree that follows the connections between the nodes.
For example, in the tree below, the path from the node 3 to the node 2 is [3, 4, 1, 2], and the path from the node 1 to the node 7 is [1, 4, 7].

In a file treepath.py, implement the function find_path, whose parameters are a reference to the root of a tree and the node identifiers a and b. 
The function returns the path as a list, or None if there is no path.
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

def find_path(node, a, b):
    # if im not mistaken, the key to this is finding the smallest subtree that contains both the start and end nodes 
    # once you find that, you know that the route will pass through the root node of the subtree
    # then its just a simple dfs from root to each target node

    if a == b:
        if _find_node_path(node, a):
            return [a]
        else:
            return None
    
    path_to_a = _find_node_path(node, a)
    path_to_b = _find_node_path(node, b)
    
    if not path_to_a or not path_to_b:
        return None
    
    lca_index = 0
    for i in range(min(len(path_to_a), len(path_to_b))):
        if path_to_a[i] == path_to_b[i]:
            lca_index = i
        else:
            break
    
    result = []
    for i in range(len(path_to_a) - 1, lca_index - 1, -1):
        result.append(path_to_a[i])
    
    for i in range(lca_index + 1, len(path_to_b)):
        result.append(path_to_b[i])
    
    return result

def _find_node_path(node, target_value):
    if node.value == target_value:
        return [node.value]
    
    for child in node.children:
        path = _find_node_path(child, target_value)
        if path:
            return [node.value] + path
    
    return None

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_path(tree1, 3, 2)) # [3, 4, 1, 2]
    print(find_path(tree1, 1, 7)) # [1, 4, 7]
    print(find_path(tree1, 5, 5)) # [5]
    print(find_path(tree1, 7, 3)) # [7, 4, 3]
    print(find_path(tree1, 4, 8)) # None

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_path(tree2, 1, 4)) # [1, 2, 3, 4]
    print(find_path(tree2, 4, 1)) # [4, 3, 2, 1]
    print(find_path(tree2, 2, 3)) # [2, 3]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_path(tree3, 2, 3)) # [2, 1, 3]
    print(find_path(tree3, 1, 2)) # [1, 2]
    print(find_path(tree3, 5, 5)) # None