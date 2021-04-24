"""
Write a Python function that takes a positive integer
and returns the sum of the cube of all the positive integers smaller than the specified number.
Sample Test:
number = 4
1^3 + 2^3 + 3^3 = 36
"""


def value(number):
    cubes = 0
    for n in range(1, number):
        cubes = cubes + n ** 3
    return cubes


print(value(4))
print(value(8))
