"""
Write a Python program to calculate the sum of three given numbers,
if the values are equal then return three times of their sum.
"""


def numbers(a, b, c):
    sum = a + b + c
    if a == b == c:
        return sum * 3
    else:
        return sum


print(numbers(1, 2, 3))
print(numbers(3, 3, 3))
