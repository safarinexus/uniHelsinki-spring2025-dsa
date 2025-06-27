'''
You are given a table of distances between cities. The cities are numbered 1...n.
For example, the distance table might look like this:

0 2 2 1 8
2 0 9 1 2
2 9 0 8 3
1 1 8 0 3
8 2 3 3 0

Here the cities are 1...5. For instance, the distance between the cities 2 and 3 is 9.
In the table, this distance is on the row 2 of the column 3, as well as on the row 3 of the column 2.
Your task is to find the shortest route that starts at the city 1, visits all other cities, and returns back into the city 1.
If there are multiple routes of the same length, the selected route is the one, where the smallest possible city number is chosen at each step.
Given the table above, the shortest route is 1 -> 3 -> 5 -> 2 -> 4 -> 1 with the length 9.
In a file visitall.py, implement the function find_route that takes the distance table as a parameter.
The function should return the length of the route and one route of that length.
You may assume that the number of cities is in the range 2...8.
The function should be efficient in all such cases.
'''
#    2    3    2    1    1   = 9
# 1 -> 3 -> 5 -> 2 -> 4 -> 1 with length 9 is correct because smallest city is chosen at every step (greedy)
#    1    1    2    3    2   = 9
# 1 -> 4 -> 2 -> 5 -> 3 -> 1 with length 9 but wrong because smallest possible city is not chosen at each step (step 2)

import itertools

def find_route(distances):
    cities = len(distances)
    city_order = [i for i in range(1, cities)]
    length = float('inf')
    routes = []

    for order in itertools.permutations(city_order):
        curr_order = [0] + list(order) + [0]
        dist = 0
        for i in range(1, len(curr_order)):
            dist += distances[curr_order[i]][curr_order[i - 1]]
        
        if dist < length:
            routes = []
            length = dist
        
        if dist == length:
            routes.append(curr_order)

    return (length, [i + 1 for i in sorted(routes)[0]])


if __name__ == "__main__":
    distances = [[0, 2, 2, 1, 8],
                 [2, 0, 9, 1, 2],
                 [2, 9, 0, 8, 3],
                 [1, 1, 8, 0, 3],
                 [8, 2, 3, 3, 0]]

    length, route = find_route(distances)
    print(length) # 9
    print(route) # [1, 3, 5, 2, 4, 1]

    distances = [[0, 7, 5, 9, 6, 3, 1, 3],
                 [7, 0, 3, 2, 3, 3, 7, 8],
                 [5, 3, 0, 4, 2, 7, 7, 1],
                 [9, 2, 4, 0, 2, 3, 2, 4],
                 [6, 3, 2, 2, 0, 9, 5, 9],
                 [3, 3, 7, 3, 9, 0, 4, 5],
                 [1, 7, 7, 2, 5, 4, 0, 7],
                 [3, 8, 1, 4, 9, 5, 7, 0]]

    length, route = find_route(distances)
    print(length) # 18
    print(route) # [1, 7, 4, 6, 2, 5, 3, 8, 1]