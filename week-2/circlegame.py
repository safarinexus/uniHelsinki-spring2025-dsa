'''
There is a circle of n players, numbered 1,2,...,n.
Starting with the player 1 and going around the circle, every second player leaves the circle until all players have left.
Your task is to find the order in which the players leave the circle.

The game starts with the player 1 and the first player to leave is the player 2. 
The next one to leave is the player 4 and eventually all players leave in the order [2,4,6,1,5,3,7].
In a file circlegame.py, implement the function find_order that takes the number of players n as a parameter and returns the leaving order as a list.
Your function should be efficient even for large values of n. 
Removing players in the middle of the list would be too slow. 
A better approach is, for example, to add the players remaining in the circle to a new list.
In the last test case of the following code template, n=10^5 and only the last five players to leave the circle are printed out. 
Your function should be fast in this test case too.
'''

def find_order(n):
    players = list(range(1, n + 1))
    
    index = 0
    
    leave_order = []
    
    while players:
        index = (index + 1) % len(players)
        leave_order.append(players.pop(index))
    
    return leave_order

if __name__ == "__main__":
    print(find_order(1)) # [1]
    print(find_order(2)) # [2, 1]
    print(find_order(3)) # [2, 1, 3]
    print(find_order(7)) # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:]) # [52545, 85313, 36161, 3393, 68929]