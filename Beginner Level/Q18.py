"""
Write a Python program to get a string which is n copies of a given string.
sample Input:
(abc, 2) , (.py, 4)
sample Output:
abcabc
.py.py.py.py
"""


def value(string, n):
    for i in range(1, n + 1):
        print(string, end='')
    print()  # to make cursor print on the  next line (Otherwise it'll be printed abcabc .py.py.py.py on same line)


value('abc', 2)
value('.py', 4)
