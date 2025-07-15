'''
The list game has two players that alternate in removing numbers from a list.
In each turn, a player removes either the first or the last number.
The game ends when all numbers have been removed.
The score of a player is the sum of the numbers removed by that player.
The winner of the game is the player with the higher score.
If both players end up with the same sum, the result is a draw.
Your task is to find if the player with the first turn always wins if they play optimally.
For example, if the list is [2,1,3], the first player always wins. 
The first player can first remove 3 and then 1.
At the end of the game, the first player's sum is 4 and the other player's sum is 2.
On the other hand, if the list is [1,3,1], the first player can lose.
The first player must remove either of the 1's, and then the other player can remove 3.
The first player's final sum is 2 while the other player's sum is 3 giving the win to the other player.
In a file listgame.py, implement the function first_wins that takes a list of integers as a parameter.
The function should return True if the first player always wins, and False otherwise.
The function should be efficient when the length of the list is in the range 1 ... 50.
'''

def first_wins(numbers):
    first_sum = max_sum(numbers)
    second_sum = sum(numbers) - first_sum
    return first_sum > second_sum

def max_sum(numbers, results={}):
    if len(numbers) == 1:
        return numbers[0]

    key = tuple(numbers)

    if key not in results:
        sum_with_first = sum(numbers) - max_sum(numbers[1:])
        sum_with_last = sum(numbers) - max_sum(numbers[:-1])
        results[key] = max(sum_with_first, sum_with_last)

    return results[key]

if __name__ == "__main__":
    print(first_wins([2, 1, 3])) # True
    print(first_wins([1, 3, 1])) # False

    print(first_wins([1])) # True
    print(first_wins([1, 1])) # False
    print(first_wins([1, 5])) # True
    print(first_wins([1, 1, 1])) # True
    print(first_wins([1, 2, 3, 4])) # True
    print(first_wins([1, 3, 3, 7, 4, 2, 1])) # False

    print(first_wins([1] * 50)) # False
    print(first_wins([1, 2] * 25)) # True