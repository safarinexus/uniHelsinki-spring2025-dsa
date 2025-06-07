'''
Your task is to design a labyrinth where the length of the shortest route from the square A to the square B is a given integer.
The labyrinth should be of the same form as in the earlier task this week.
In addition, the width and the height of the labyrinth should be at most 10 squares.
In a file design.py, implement the function create_grid that takes a positive integer as a parameter and returns the grid as a list of strings.
You may return any grid with the desired shortest route length.
If no such grid can be formed, the function should return None.

The example labyrinths in the below code template have shortest route lengths 5 and 10.
Your code does not need to return these specific labyrinths.
There is no labyrinth satisfying the constraints with a shortest route length 42.
'''

def create_grid(steps):
    pass

if __name__ == "__main__":
    grid = create_grid(5)
    print("\n".join(grid))
    # ########
    # #.#B...#
    # #.#.##.#
    # #.....A#
    # ########

    grid = create_grid(10)
    print("\n".join(grid))
    # ########
    # #.#A...#
    # #.####.#
    # #B.....#
    # #.####.#
    # #......#
    # ########

    grid = create_grid(42)
    print(grid) # None