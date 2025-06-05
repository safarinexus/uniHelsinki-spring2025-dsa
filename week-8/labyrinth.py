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

def find_route(grid):
    pass

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