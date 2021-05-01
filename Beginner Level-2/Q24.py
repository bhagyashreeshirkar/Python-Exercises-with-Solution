"""
Write a Python function to check whether a number is in a given range from 1 to 25.
"""


def check(number):
    if number in range(1, 26):
        print(f'%d is in the range.' % number)
    else:
        print(f'%d is out of the range.' % number)


check(9)
check(57)
