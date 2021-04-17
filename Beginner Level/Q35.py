"""
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49
"""


def solve(x, y):
    value = (x + y) * (x + y)
    print(f'({x} + {y}) ^ 2) = {value}')


solve(4, 3)
