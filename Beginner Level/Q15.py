"""
Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
"""


def value(number):
    if number <= 17:
        print(17 - number)
    else:
        print((abs(17 - number)) * 2)  # Absolute value of a number is the value without considering its sign.


value(22)
value(14)
