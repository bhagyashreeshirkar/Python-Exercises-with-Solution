"""
Write a Python program to swap two variables.
"""


# Method-1
def swap(a, b):
    temp = a  # temp = 2
    a = b     # a = 6
    b = temp  # b = 2
    print(f'{a, b}')


swap(2, 6)


# Method-2
x = int(input('Enter a: '))
y = int(input('Enter b: '))
x, y = y, x

print(f'after swapping x = {x}, y ={y}')
