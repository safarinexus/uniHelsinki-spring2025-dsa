'''
You are given the price of a stock during a period of n days. 
As in the earlier task, your task is to compute for each day the largest profit you could have achieved by selling the stock on that day.
The difference to the earlier task is that in addition to the sales profit you can gain a dividend on each day.
When you buy on the day a and sell on the day b, the dividend is b-a.
For example, when the prices are [3,2,3,5,1,4], the list of profits is [0,0,2,5,2,6]. 
For example, when selling on the fifth day, the largest profit is 2, because you could have bought the stock on the second day at the price 2 and then sold it at the price 1. 
Thus the sales profit is 1-2=-1 and the dividend is 5-2=3 for a total profit of -1+3=2.
In a file dividend.py, implement the function find_profits that takes a list of prices as a parameter, and returns the list of profits. 
As before, you need an efficient solution with a time complexity O(n).
'''

def find_profits(prices):
    res = [0 for _ in prices]
    ptr = 0 

    for i in range(1, len(prices)): 
        curr = prices[i] - prices[ptr] + i - ptr
        res[i] = max(curr, 0)

        if prices[i] < prices[ptr]: 
            if i - ptr < prices[ptr] - prices[i]:
                ptr = i
    
    return res

if __name__ == "__main__":
    print(find_profits([1, 2, 3, 4])) # [0, 2, 4, 6]
    print(find_profits([4, 3, 2, 1])) # [0, 0, 0, 0]
    print(find_profits([1, 1, 1, 1])) # [0, 1, 2, 3]
    print(find_profits([2, 4, 1, 3])) # [0, 3, 1, 4]
    print(find_profits([1, 1, 5, 1])) # [0, 1, 6, 3]
    print(find_profits([3, 2, 3, 5, 1, 4])) # [0, 0, 2, 5, 2, 6]
    print(find_profits([9, 6, 10, 10, 3, 6, 7, 6, 5, 7])) # [0, 0, 5, 6, 0, 4, 6, 6, 6, 9]

    prices = list(range(1, 10**5+1))
    print(find_profits(prices)[:5]) # [0, 2, 4, 6, 8]