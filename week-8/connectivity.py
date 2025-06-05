'''
A graph is connected if there is a route between every pair of nodes. 
Your task is to determine if a given graph is connected.
For example, the following graph is connected, because there is a route from any node to any other node.

The graph below is not connected, because there is no route from the node 1 to the node 4.

In a file connectivity.py, implement the function connected, whose parameters are the lists of the nodes and the edges of a graph.
The function should return True if the graph is connected and False otherwise.
'''

def connected(nodes, edges):
    adjacency = {node: [] for node in nodes}

    for edge in edges:
        adjacency[edge[0]].append(edge[1])
        adjacency[edge[1]].append(edge[0])

    visited = set()

    def dfs(node):
        if node in visited:
            return 
        visited.add(node)

        if node in adjacency:
            for i in adjacency[node]:
                dfs(i)
        else:
            return

    dfs(nodes[0])
    return len(visited) == len(nodes)

    


if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (4, 5)]
    print(connected(nodes, edges)) # True

    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(connected(nodes, edges)) # False

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(connected(nodes, edges)) # True