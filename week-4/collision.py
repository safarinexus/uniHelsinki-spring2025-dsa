'''
Consider again the hash function of the earlier task:

(c_0 A^{n-1} + c_1 A^{n-2} ... + c_{n-1} A^0) mod M

The parameters are the same as before: A=23 and M=2^{32}.
In a file collision.py, implement the function find_other that takes a string as a parameter and returns a different string with the same hash value.
The input string consists of the characters a–z and has at most 100 characters. The output string should satisfy the same requirements.
The function should be efficient and return a different string immediately.
In the code below, the string zfgjynuk is an example of what the function might return.
Your function does not need to return this specific string.
It can return any string that satisfies the requirements and has the same hash value.
'''

import random

def hash_value(string):
    hash = 0
    curr = len(string) - 1
    A = 23
    M = 2**32

    for i in string: 
        val = ord(i) - 97
        hash += val * (A ** curr)
        curr -= 1

    hash = hash % M
    return hash

def find_other(string):
    hash = hash_value(string)
    res = ""

    return res

if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682
