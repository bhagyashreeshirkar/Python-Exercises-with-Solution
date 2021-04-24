"""
Write a Python program to test if a variable is a list or tuple or a set.
"""


def guess(a):
    if type(a) == list:
        return 'It is a list'
    elif type(a) == tuple:
        return 'It is a tuple'
    else:
        return 'It is a set'


print(guess((3.3, 56, 6)))
print(guess([3, 4, 1, 6, 7]))
print(guess({33, 12, 88, 90}))
