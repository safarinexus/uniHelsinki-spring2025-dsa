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
        if not self.grid or not word:
            return 0
        
        rows = len(self.grid)
        cols = len(self.grid[0]) if rows > 0 else 0
        word_len = len(word)
        reverse_word = word[::-1]
        found_positions = set()
        directions = [
            (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)
        ]
        
        if word_len == 1:
            count = 0
            for row in range(rows):
                for col in range(cols):
                    if self.grid[row][col] == word[0]:
                        count += 1
            return count
        
        for row in range(rows):
            for col in range(cols):
                for d_row, d_col in directions:
                    end_row = row + (word_len - 1) * d_row
                    end_col = col + (word_len - 1) * d_col
                    
                    if 0 <= end_row < rows and 0 <= end_col < cols:
                        current_word = ""
                        cell_positions = []
                        
                        for i in range(word_len):
                            curr_row = row + i * d_row
                            curr_col = col + i * d_col
                            current_word += self.grid[curr_row][curr_col]
                            cell_positions.append((curr_row, curr_col))
                        
                        if current_word == word or current_word == reverse_word:
                            position_key = tuple(sorted(cell_positions))
                            found_positions.add(position_key)
        
        return len(found_positions)

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