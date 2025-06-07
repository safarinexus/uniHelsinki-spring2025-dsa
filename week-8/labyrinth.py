'''
You are given a grid, where each square is a floor square or a wall square.
The symbol . means a floor square and the symbol # means a wall square. 
All boundary squares are wall squares.
In addition, the grid has a single start square (A) and a single end square (B).

Your task is to find the shortest route from the start square to the end square.
The length of a route is the number of steps on the route.
In each step, you can move horizontally or vertically to an adjacent floor square.

In a file labyrinth.py, implement the function find_route, whose parameter is the description of a grid as a list of strings.
The function should return the length of the shortest route, or None is there is no route.
'''
from collections import deque

def find_route(grid):
    start, end = None, None
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        for j in range(len(grid[i])):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'B':
                end = (i, j)
    
    if not start or not end:
        return None
    
    queue = deque([(start, 0)])
    visited = {start}
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while queue:
        (row, col), distance = queue.popleft()
        
        if (row, col) == end:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] != '#' and 
                (new_row, new_col) not in visited):
                
                queue.append(((new_row, new_col), distance + 1))
                visited.add((new_row, new_col))
    
    return None
    

if __name__ == "__main__":
    grid = ["########",
            "#.#.B..#",
            "#A#.##.#",
            "#......#",
            "########"]
    print(find_route(grid)) # 6

    grid = ["########",
            "#B#...A#",
            "#.#.##.#",
            "#......#",
            "########"]
    print(find_route(grid)) # 9

    grid = ["########",
            "####..B#",
            "#.A#.#.#",
            "#..#...#",
            "########"]
    print(find_route(grid)) # None