'''
In a game of cards, you are holding a certain set of cards and your task is to find a subset with a given sum.
How many such card combinations there are?
In this task, the set of cards is represented as a list of numbers.
For example, the list [2,1,4,6] means that your hand contains four cards with the values 2, 1, 4 and 6.
The suit of a card (e.g., clubs) does not matter here.
For example, when the cards are [2,1,4,6] and the desired sum is 6, there are two valid combinations.
One consists of the cards 2 and 4, and the other of the single card 6.
In a file cardgame.py, implement the function count_combinations that takes the list of cards and the desired sum as parameters.
The function should return the number of valid combinations.
You may assume that the number of cards is in the range 1...10.
The function should be efficient in all such cases.
'''
import itertools

def count_combinations(cards, target):
    count = 0

    for i in range(1, len(cards) + 1):
        for combination in itertools.combinations(cards, i):
            if sum(combination) == target: 
                count += 1

    return count

if __name__ == "__main__":
    print(count_combinations([2, 1, 4, 6], 6)) # 2
    print(count_combinations([1, 1, 1, 1], 2)) # 6
    print(count_combinations([2, 1, 4, 6], 15)) # 0
    print(count_combinations([1], 1)) # 1
    print(count_combinations([1, 2, 3, 4, 5], 5)) # 3
    print(count_combinations([1, 1, 4, 1, 1], 4)) # 2
    print(count_combinations([1] * 10, 5)) # 252