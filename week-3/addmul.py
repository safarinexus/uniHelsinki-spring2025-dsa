'''
You are given a string that contains mathematical expressions of the following forms:

add(x,y): sum of the numbers x and y
mul(x,y): product of the numbers x and y

The numbers x and y are positive integers. You should only process expressions of this precise form.
Your task is to create a new string where each expression has been replaced with the result of evaluating the expression. 
For example, the string abadd(123,456)mulxmul(3,13) should turn into the string ab579mulx39.
In a file addmul.py, implement the function evaluate that takes a string as a parameter and returns the modified string with the expression evaluations.
Your function should be efficient with long strings too. 
A good test of efficiency is the last test case in the code template below, where the string contains 10^5 copies of the expression mul(6,7).
Your function should finish quickly in this test case too.
'''

import re

def evaluate(data):
    if not data:
        return data
    
    add_pattern = re.compile(r'add\(([1-9]\d*),([1-9]\d*)\)')
    mul_pattern = re.compile(r'mul\(([1-9]\d*),([1-9]\d*)\)')

    def replace_add(match):
        num1, num2 = map(int, match.groups())
        return str(num1 + num2)

    def replace_mul(match):
        num1, num2 = map(int, match.groups())
        return str(num1 * num2)

    data = add_pattern.sub(replace_add, data)
    data = mul_pattern.sub(replace_mul, data)

    return data
        

if __name__ == "__main__":
    print(evaluate("add(1,2)")) # 3
    print(evaluate("aybabtu")) # aybabtu
    print(evaluate("mul(6,7),mul(7,191)")) # 42,1337
    print(evaluate("abadd(123,456)mulxmul(3,13)")) # ab579mulx39
    print(evaluate("mul()mul(13)mul(0,1)")) # mul()mul(13)mul(0,1)
    print(evaluate("a"))
    print(evaluate("add()add(5)add(0,1)add(1,0)add(1,-1)add(-1,1)add(1, 2)add(1.5,2)add(01,2)"))
    print(evaluate("mul()mul(5)mul(0,1)mul(1,0)mul(1,-1)mul(-1,1)mul(1, 2)mul(1.5,2)mul(01,2)"))

    data = "mul(6,7)"*10**5
    result = evaluate(data)
    print(len(result)) # 200000
    print(result[:20]) # 42424242424242424242

    data = "add(1,1)"*10**5
    result = evaluate(data)
    print(len(result)) # 200000
    print(result[:20]) # 42424242424242424242