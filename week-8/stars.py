'''
You are given a grid, where each square is a sky square or a star square.
The symbol . means a sky square and the symbol * means a star square.

Your task is to count how many different shapes of constellations there are in the grid.
Two star squares belong to the same constellation if they are adjacent horizontally, vertically or diagonally.

Two constellations are considered to have a different shape even if they can be made the same with rotations and reflections.
The examples in the code template illustrate this.

In a file stars.py, implement the function count_patterns, whose parameter is the description of a grid as a list of strings.
The function should return the number of different constellation shapes.
'''

from collections import deque

def count_patterns(grid):
    def normalised(constel):
        new = []
        normaliser = constel[0]

        for i in constel:
            x = i[0] - normaliser[0]
            y = i[1] - normaliser[1]
            new.append((x, y))
        
        return tuple(new)
    
    shapes = []

    rows = len(grid)
    cols = len(grid[0])

    q = deque()
    visited = set()

    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited: 
                visited.add((r, c))
                if grid[r][c] == "*":
                    constel = [(r, c)]
                    q.append((r, c))
                
                    while q:
                        curr = q.popleft()
                        for dir in directions:
                            x = curr[0] + dir[0]
                            y = curr[1] + dir[1]
                            if x >= 0 and x < rows and y >= 0 and y < cols and grid[x][y] != "." and (x, y) not in visited:
                                visited.add((x, y))
                                q.append((x, y))
                                constel.append((x, y))

                    shapes.append(constel)

    res = set()
    for i in shapes:
        res.add(normalised(i))

    return len(res)

                

if __name__ == "__main__":
    grid = ["..*..*..",
            "**.....*",
            ".....**.",
            "...*....",
            ".**....*"]
    print(count_patterns(grid)) # 2

    grid = ["....*..*",
            "*.......",
            "......*.",
            "..*.....",
            "......*."]
    print(count_patterns(grid)) # 1

    grid = ["***.*.**",
            ".*..*..*",
            ".*.***..",
            ".......*",
            "......**"]
    print(count_patterns(grid)) # 4

    grid = ["***.***.",
            "..*...*.",
            "**..**..",
            "..*...*.",
            "**..**.."]
    print(count_patterns(grid)) # 1