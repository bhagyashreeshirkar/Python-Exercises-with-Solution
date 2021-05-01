"""
Write a Python program to append a new item to the end of the array.
Sample Output:
Original array: array('I', [1, 3, 5, 7, 9])
Append 11 at the end of the array:
New array: array('I', [1, 3, 5, 7, 9, 11])
"""

from array import *

numbers = array('I', [1, 3, 5, 7, 9])

print(f'Original array:', numbers)
numbers.append(11)
print(f'New array:', numbers)
