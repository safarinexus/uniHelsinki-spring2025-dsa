'''
A robot moves vertically and horizontally in a grid. 
Initially the robot moves upwards, and whenever the robot encounters an obstacle, it turns right.
If the robot eventually moves beyond the edge of the grid, it exits the grid.
Otherwise, it continues moving in the grid in an infinite loop.
Your task is to find out, how many different squares of the grid are visited by the robot, and whether the robot eventually exits the grid or if it stays in an infinite loop.
In a file roboroute.py, implement the function analyze_route that takes a description of the grid as a parameter.
The description is a list of strings, where the character '.' is a floor square, the character '#' is an obstacle, and the character 'R' is the initial position of the robot. 
You may assume that there is only one character R.
The function returns a tuple, where the first element is the number of squares on the robot's route, and the second element is True (the robot exits the grid) or False (the robot stays in an infinite loop).
The function will be tested in various situations, where the size of the grid is at most 20 x 20 squares. The function should be efficient in all such test cases.
'''

def analyze_route(grid):
    visited  = set()
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] # Up, Right, Down, Left
    direction = 0 # Start moving up
    rows = len(grid)
    cols = len(grid[0])
    currX, currY = -1 , -1

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'R':
                currX, currY = row, col

    move = True

    while move: 
        print(visited)
        currX += directions[direction][0]
        currY += directions[direction][1]

        if currX < 0 or currX >= rows or currY < 0 or currY >= cols:
            return (len(visited), True)

        elif grid[currX][currY] == '#':
            currX -= directions[direction][0]
            currY -= directions[direction][1]
            if direction < 3:
                direction += 1
            else: 
                direction = 0

        else: 
            visited.add((currX, currY))

if __name__ == "__main__":
    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1)) # (14, True)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2)) # (12, False)