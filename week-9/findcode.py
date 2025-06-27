'''
A key code consists of four digits in the range 1...9. 
The code does not contain the same digit twice.
You are given an object ("oracle") that holds a secret key code. 
Your task is to determine the code using queries to the oracle.
Each query is a key code, and the oracle's reply tells how many of the digits are in the correct place, and how many of the digits belong to the key code but are in a wrong place.
For example, if the correct code is 4217 and you make the query 1234, the oracle replies with the numbers 1 and 2.
This means that one of the digits (2) is in the correct place and two of the digits (1 and 4) are part of the code but in a different place.
The challenge of the task is that you are allowed to make at most 16 queries to the oracle.
Then you must be able to determine the secret key code.
Each query to the oracle must be a valid key code. In particular, the query may not contain multiple copies of the same digit.
For example, 1212 is not a valid query.
In a file findcode.py, implement the function find_code that takes the oracle as a parameter.
The function can query the oracle using the method check_code that returns the reply as a pair of integers.
The function may not try to discover the code in any way other than by calling check_code.
The implementation of the oracle on the server may differ from the implementation in the code template.
'''
import re

class Oracle:
    def __init__(self, code):
        self.code = code
        self.counter = 0

    def check_code(self, code):
        self.counter += 1
        if self.counter > 16:
            raise RuntimeError("too many check_code calls")

        if type(code) != str or not re.match("^[1-9]{4}$", code) or len(code) != len(set(code)):
            raise RuntimeError("invalid code for check_code")

        in_place = in_code = 0
        for pos in range(4):
            if code[pos] in self.code:
                if code[pos] == self.code[pos]:
                    in_place += 1
                else:
                    in_code += 1

        return in_place, in_code

def find_code(oracle):
    pass

if __name__ == "__main__":
    # example of using the oracle
    oracle = Oracle("4217")
    print(oracle.check_code("1234")) # (1, 2)
    print(oracle.check_code("3965")) # (0, 0)
    print(oracle.check_code("4271")) # (2, 2)
    print(oracle.check_code("4217")) # (4, 0)

    # example of using the function find_code
    oracle = Oracle("4217")
    code = find_code(oracle)
    print(code) # 4217