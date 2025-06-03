'''
Your task is to construct for each level of the tree a list of the nodes on that level in numerical order.
For example, in the tree below, the top level list is [1], the middle level list is [2,4,5], and the bottom level list is [3,6,7].

In a file levels.py, implement the function find_levels that takes a reference to the root of a tree as parameter and returns a list whose elements are the level lists.
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

def find_levels(node):
    res = []
    queue = [(node, 0)]
    
    while queue:
        current_node, level = queue.pop(0)
        
        if len(res) <= level:
            res.append([])
            
        res[level].append(current_node.value)
        
        for child in current_node.children:
            queue.append((child, level + 1))
    
    for level_list in res:
        level_list.sort()
        
    return res

if __name__ == "__main__":
    tree1 = Node(1, [Node(4, [Node(3), Node(7)]),
                     Node(5),
                     Node(2, [Node(6)])])
    print(find_levels(tree1)) # [[1], [2, 4, 5], [3, 6, 7]]

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])
    print(find_levels(tree2)) # [[1], [2], [3], [4]]

    tree3 = Node(1, [Node(2), Node(3), Node(4)])
    print(find_levels(tree3)) # [[1], [2, 3, 4]]