'''
Your task is to construct a list that contains for each node of a given graph the degree of the node, i.e., the number of neighbors of the node.
The list should be in order from the smallest to the largest.
For example, in the graph below, the desired list is [2,2,3,3,4], because the degree of the nodes 3 and 5 is 2, the degree of the nodes 1 and 2 is 3, and the degree of the node 4 is 4.

In a file degrees.py, implement the function find_degrees, whose parameters are the lists of the nodes and the edges of the graph.
The function should return the list of degrees of the nodes.
'''

def find_degrees(nodes, edges):
    pass

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(find_degrees(nodes, edges)) # [2, 2, 3, 3, 4]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_degrees(nodes, edges)) # [0, 0, 0, 0, 0]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_degrees(nodes, edges)) # [1, 1, 1, 1, 4]