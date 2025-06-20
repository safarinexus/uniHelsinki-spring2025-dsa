'''
Your task is to form all words that consist of the letters of a given word and contain no letter twice in a row.
Here a word means any combination of letters and it does not have to be a real word in any language.
For example, if the input word is kala, the desired words are akal, akla, alak, alka, kala and laka.
In a file allwords.py, implement the function create_words with a word as a parameter.
The function should return a list of the desired words in lexicographical order.
You may assume that the length of the word is in the range 1...8.
The function should be efficient in all such cases.
'''
import itertools

def create_words(word):
    res = set()

    def check_word(word): 
        prev = word[0]
        for i in range(1, len(word)):
            if word[i] == prev:
                return False
            prev = word[i]
        return True

    for permutation in itertools.permutations(word):
        temp = "".join(permutation)
        if check_word(temp):
            res.add(temp)

    return sorted(list(res))


if __name__ == "__main__":
    print(create_words("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab")) # ['aba']
    print(create_words("aaab")) # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky', 
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    print(len(create_words("aybabtu"))) # 660
    print(len(create_words("abcdefgh"))) # 40320