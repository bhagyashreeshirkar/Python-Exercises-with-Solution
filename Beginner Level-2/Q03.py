"""
Write a Python program to display all possible strings. Use the characters exactly once.
Sample Example-
'A', 'B', 'C'
ABC,ACB,BAC,BCA,CAB,CBA
"""
from itertools import permutations


# Method-1
def enter(characters):
    all_strings = permutations(characters)
    for string in all_strings:
        print(''.join(string), end=' ')
    print()  # This is to print output of next input on next line


enter(['A', 'B', 'C'])
enter(['a', 'e', 'i', 'o', 'u'])


# Method-2 (by using list comprehension method
def enter(chars):
    print([''.join(ch) for ch in permutations(chars)])


enter(['A', 'B', 'C'])
enter(['a', 'e', 'i', 'o', 'u'])

