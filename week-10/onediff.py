'''
Your task is to count how many ways you can form a string of length n using the characters a–z so that any pair of adjacent characters in the string are also consecutive in the alphabetical order.
When n=2, the answer is 50. The first character of the string can be chosen freely from the range a–z (26 options).
If the first character is a or z, there is only one choice for the second character. Otherwise, there are two choices for the second character.
Thus the total number of such strings is 2 + 24 x 2 = 50.
When n=5, the strings ababa, cdcba and bcdef are examples of valid strings.
In a file onediff.py, implement the function count_strings that takes the length of the strings as a parameter, and returns the number of the strings.
The function should be efficient when the string length is in the range 1 ... 100.
'''

def count_strings(n):
    count = {}
    for char in range(26):
        count[(char, 1)] = 1

    for pos in range(2, n + 1):
        for char in range(26):
            ways = 0
            if char > 0:
                ways += count[(char - 1, pos - 1)]
            if char < 25:
                ways += count[(char + 1, pos - 1)]
            count[(char, pos)] = ways

    total = 0
    for char in range(26):
        total += count[(char, n)]
    return total
          


if __name__ == "__main__":
    print(count_strings(1)) # 26
    print(count_strings(2)) # 50
    print(count_strings(3)) # 98
    print(count_strings(4)) # 192

    print(count_strings(42)) # 36766943673096
    print(count_strings(100)) # 7073450400109633000218032957656