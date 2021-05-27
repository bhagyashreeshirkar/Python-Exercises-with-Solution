"""
Write a python program to solve the quadratic equation or find out the roots of the quadratic equation.
"""
import math


def find_roots(a, b, c):
    function = (b ** 2) - (4 * a * c)
    root1 = (- b + math.sqrt(function)) / (2 * a)
    root2 = (- b - math.sqrt(function)) / (2 * a)
    return round(root1), round(root2)


print(find_roots(2, 10, 8))

'''
Note: For mathematical solutions make sure that parenthesis should be there for each term.
'''

# for complex roots cmath ie, complex math function is used

import cmath
def find_roots(a, b, c):
    function = (b ** 2) - (4 * a * c)
    root1 = (- b + cmath.sqrt(function)) / (2 * a)
    root2 = (- b - cmath.sqrt(function)) / (2 * a)
    return root1, root2


print(find_roots(2, 10, 8))
print(find_roots(1, 4, 2))
