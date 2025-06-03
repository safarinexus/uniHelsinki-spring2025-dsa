'''
You are given a grid that contains a description of a tree. 
Your task is to reconstruct the described tree.
The grid can contain the following symbols:

.: an empty square
1–9: a node of the tree
/: a connection down and left
|: a connection straight down
\: a connection down and right

Each node has at most three children.
Between a node and its child are one or more connection symbols.
The connections are straight lines without bends.
If a node has one child, it is straight down. 
If a node has two children, they are down and left and down and right. 
If a node has three children, they are down and left, straight down, and down and right.
In a file findtree.py, implement the function find_tree whose parameter is a description of the grid as a list of strings. 
The function returns the structure of the depicted tree using the class Node.
You may assume that the size of the grid is at most 20 x 20 and that the grid depicts a tree with at least one node.

Here r"" denotes a string in which the character \ is not treated as an escape character but as a regular character.
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

def find_tree(grid):
    rows = len(grid)
    columns = len(grid[0])
    ptr = Node(-1)

    for row in range(rows):
        curr = ''
        for column in range(columns):
            if grid[row][column].isnumeric():
                curr += grid[row][column]
                if column == columns - 1:
                    ptr.children.append(int(curr))
                    ptr = ptr.children[0]
                    curr = ''
            elif grid[row][column] == "\\":
                
                
            else:
                if curr:
                    ptr.children.append(int(curr))
                    ptr = ptr.children[0]
                    curr = ''

if __name__ == "__main__":
    grid = [r"...........",
            r"...........",
            r"......5....",
            r"...../.\...",
            r"....3...\..",
            r"....|....1.",
            r"....2......"]
    tree = find_tree(grid)
    print(tree)
    # Node(5, [Node(3, [Node(2)]), Node(1)])

    grid = [r"....1.....",
            r".../.\....",
            r"..2...\...",
            r"..|....3..",
            r"..7.../|\.",
            r"./.\.4.5.6",
            r"8...9....."]
    tree = find_tree(grid)
    print(tree)
    # Node(1, [Node(2, [Node(7, [Node(8), Node(9)])]), Node(3, [Node(4), Node(5), Node(6)])])


