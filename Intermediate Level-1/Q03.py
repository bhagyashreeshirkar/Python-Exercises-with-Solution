"""
Write a program to swap two numbers without using third variable.
"""
a = int(input('a: '))
b = int(input('b: '))
a = a + b
b = a - b
a = a - b
print(f'swapping of two numbers is a: {a} and b: {b}')
