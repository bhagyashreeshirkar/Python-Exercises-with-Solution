"""
Write a Python program that accepts a word from the user and reverse it.
"""


def enter(word):
    for n in reversed(word):
        print(n, end='')
    print()


enter('himalaya')
enter('madam')
