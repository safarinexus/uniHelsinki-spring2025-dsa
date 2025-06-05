'''
Your task is to compute all the components of a given graph as lists.
For example, the graph below has three components: [1,2,3], [4,5,6,7] and [8].

Each component is represented by a list that contains the nodes of the component in order from the smallest to the largest.
The desired output is a list that contains the component lists ordered by the first element of each list.
In a file components.py, implement the function find_components, whose parameters are the lists of the nodes and the edges of a graph.
The function should return the list of components.
'''

def find_components(nodes, edges):
    graph = { node: [] for node in nodes }

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    visited = {}
    component = 0

    def dfs(node):
        if node in visited:
            return
        visited[node] = component

        if node not in graph:
            return
        
        for next_node in graph[node]:
            dfs(next_node)

    for node in nodes:
        if node not in visited:
            component += 1
            dfs(node)

    res = [[] for _ in range(component)]

    for node in visited:
        res[visited[node] - 1].append(node)
        res[visited[node] - 1].sort()

    return sorted(res)

if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5, 6, 7, 8]
    edges = [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 7), (6, 7)]
    print(find_components(nodes, edges)) # [[1, 2, 3], [4, 5, 6, 7], [8]]

    nodes = [1, 2, 3, 4, 5]
    edges = []
    print(find_components(nodes, edges)) # [[1], [2], [3], [4], [5]]

    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (1, 4), (1, 5)]
    print(find_components(nodes, edges)) # [[1, 2, 3, 4, 5]]