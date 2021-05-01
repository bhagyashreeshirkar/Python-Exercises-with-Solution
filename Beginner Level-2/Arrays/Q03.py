"""
Write a Python program to reverse the order of the items in the array. Go to the editor
Sample Output
Original array: array('I', [1, 3, 5, 3, 7, 1, 9, 3])
Reverse the order of the items:
array('I', [3, 9, 1, 7, 3, 5, 3, 1])
"""

from array import *

numbers = array('I', [1, 3, 5, 3, 7, 1, 9, 3])

print(f'Original array:', numbers)
numbers.reverse()
print(f'Reversed array:', numbers)
