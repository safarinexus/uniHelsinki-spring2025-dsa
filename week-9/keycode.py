'''
A key code consists of four digits in the range 1...9. 
A code may not contain the same digit twice.
You are given a string describing a key code. 
Each character in the string is either a valid code digit or the character ?, which means an unknown digit.
Your task is to construct a list of all the possible key codes matching the string.
For example, when the string is 24?5, the possible codes are 2415, 2435, 2465, 2475, 2485 and 2495.
In a file keycode.py, implement the function find_codes with the key code string as a parameter.
The function should return a list that contains all the matching codes in order from the smallest to the largest.
The function should be efficient in all cases.
'''

def find_codes(pattern):
    pass

if __name__ == "__main__":
    codes = find_codes("24?5")
    print(codes) # ['2415', '2435', '2465', '2475', '2485', '2495']

    codes = find_codes("1?2?")
    print(codes[:5]) # ['1324', '1325', '1326', '1327', '1328']
    print(len(codes)) # 42

    codes = find_codes("????")
    print(codes[:5]) # ['1234', '1235', '1236', '1237', '1238']
    print(len(codes)) # 3024