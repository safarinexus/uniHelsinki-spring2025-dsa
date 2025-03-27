'''
You are given a grid of letters and your task is to find words in the grid. A word can be read horizontally, vertically or diagonally in either direction.
In a file wordgrid.py, implement the class WordFinder with the following methods:

set_grid: sets the contents of the grid as a list, where each element is a string representing a row of the grid
count: counts the number of occurrences of the given word

If a word can be read both forwards and backwards using the same letters, that should count as one occurrence only.
Your class will be tested using many different grids. The height and width of each test grid is at most 20 letters. Each letter is in the range A–Z.
'''

class WordFinder:
    def set_grid(self, grid):
        self.grid = grid

    def count(self, word):
        pass

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0     