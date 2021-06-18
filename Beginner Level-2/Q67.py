"""
Write a program to reverse a string word-wise.

Example:
Input:
Welcome to world
Output:
world to welcome
"""

def string(s):
    words = s.split()  # this will split a string into words wherever there are spaces
    words = words[::-1]
    print(' '.join(words))


statement = input()
string(statement)
