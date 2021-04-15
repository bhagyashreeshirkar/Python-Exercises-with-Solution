"""
Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""

values = [1, 5, 8, 3]


def check(number):
    if number in values:
        return True
    else:
        return False


print(check(3))
print(check(-1))
