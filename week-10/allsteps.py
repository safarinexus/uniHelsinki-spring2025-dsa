'''
Consider again the machine of the preceding task. How many different ways there are to produce a number x?
For example, x=17 can be produced in the following ways:

1 -> 2 -> 4 -> 7 -> 14 -> 17
1 -> 2 -> 4 -> 8 -> 11 -> 14 -> 17
1 -> 2 -> 5 -> 8 -> 11 -> 14 -> 17
1 -> 4 -> 7 -> 14 -> 17
1 -> 4 -> 8 -> 11 -> 14 -> 17

In this case, the answer is 5.
In a file allsteps.py, implement the function count_steps that returns the number of ways to produce the number x.
The function should be efficient when x is in the range 1 ... 1000.
'''

def count_steps(x):
    res = {}

    res[1] = 1
    for i in range(2 , x + 1):
        res[i] = 0

        if i - 3 > 0:
            res[i] += res[i - 3]

        if i % 2 == 0:
            res[i] += res[i / 2]
        
    return res[x]


if __name__ == "__main__":
    print(count_steps(1)) # 1
    print(count_steps(2)) # 1
    print(count_steps(3)) # 0
    print(count_steps(4)) # 2
    print(count_steps(5)) # 1
    print(count_steps(17)) # 5
    print(count_steps(42)) # 0
    print(count_steps(100)) # 242
    print(count_steps(1000)) # 2948311