'''
A machine has a screen initially displaying the number 1. 
The machine has two buttons: the left button adds 3 to the number and the right button multiplies the number by 2.
Your task is to reach a given number x by pushing the buttons. What is the smallest number of pushes needed?
For example, when x=17, an optimal solution is the following:

The initial number is 1.
Push the left button to get the number 4.
Push the left button to get the number 7.
Push the right button to get the number 14.
Push the left button to get the number 17.

In this case, the smallest number of pushes is 4.
In a file machine.py, implement the function min_steps that finds the smallest number of pushes to reach the number x.
If no sequence of pushes can achieve x, the function should return -1.
The function should be efficient when x is in the range 1 \dots 1000.
'''

def min_steps(x):
    res = {}

    res[0] = -1
    res[1] = 0
    for i in range(2, x + 1):
        res[i] = float('inf')

        if i - 3 > 0 and res[i - 3] != -1:
            res[i] = min(res[i], res[i - 3] + 1)
        
        if i % 2 == 0 and res[i / 2] != -1:
            res[i] = min(res[i], res[i / 2] + 1)

        if res[i] == float('inf'): 
            res[i] = -1

    return res[x]

if __name__ == "__main__":
    print(min_steps(1)) # 0
    print(min_steps(2)) # 1
    print(min_steps(3)) # -1
    print(min_steps(4)) # 1
    print(min_steps(5)) # 2
    print(min_steps(17)) # 4
    print(min_steps(42)) # -1
    print(min_steps(100)) # 7
    print(min_steps(1000)) # 13