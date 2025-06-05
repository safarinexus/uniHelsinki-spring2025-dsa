'''
You are given a grid, where each square is a floor square or a wall square.
The symbol . means a floor square and the symbol # means a wall square.
All boundary squares are wall squares.

Your task is to count the number of rooms in the grid. 
Two floor squares belong to the same room if they are adjacent horizontally or vertically.

In a file rooms.py, implement the function count_rooms, whose parameter is the description of a grid as a list of strings.
The function should return the number of rooms in the grid.
'''

def count_rooms(grid):
    rows = len(grid)
    cols = len(grid[0])
    res = 0
    visited = set()
    queue = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def bfs():
        if not queue:
            return
    
        curr = queue.pop(0)
        for dir in directions:
            x = curr[0] + dir[0]
            y = curr[1] + dir[1]
            if (x, y) not in visited and x >= 0 and x < rows and y > 0 and y < cols and grid[x][y] == ".":
                visited.add((x, y))
                queue.append((x, y))
        bfs()

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited and grid[row][col] == ".":
                visited.add((row, col))
                queue.append((row, col))
                bfs()
                res += 1

    return res

if __name__ == "__main__":
    grid = ["########",
            "#.#..#.#",
            "#####..#",
            "#...#..#",
            "########"]
    print(count_rooms(grid)) # 4

    grid = ["########",
            "#......#",
            "#.####.#",
            "#......#",
            "########"]
    print(count_rooms(grid)) # 1

    grid = ["########",
            "######.#",
            "##.#####",
            "########",
            "########"]
    print(count_rooms(grid)) # 2