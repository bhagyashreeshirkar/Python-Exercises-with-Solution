"""
Write a Python program to create an array of 5 integers and display the array items.
Access first first three elements individually indexes.
"""

from array import *

numbers = array('I', [10, 20, 30, 40, 50])

for a in numbers:
    print(a)

print(f'Elements through indexes-', numbers[0], numbers[1], numbers[2])
