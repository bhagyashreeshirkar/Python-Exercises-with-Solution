"""
Write a python program to find multiplication of multiple inputs
1. by defining function
2. by taking inputs from user
"""

import numpy

# by defining a method
def numbers(*args):
    return numpy.prod(args)


print(numbers(20, 10, 5))


# by taking inputs from user
values = list(map(int, input('Enter numbers: ').split(',')))
multiplication = 1
for num in values:
    multiplication *= num
print('Multiplication:', multiplication)
