"""
Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
"""


def sum_of_numbers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c


print(sum_of_numbers(2, 3, 4))
print(sum_of_numbers(3, 3, 15))
print(sum_of_numbers(10, 22, 70))
