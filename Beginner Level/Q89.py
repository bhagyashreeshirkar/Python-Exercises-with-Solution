"""
write a program to get most repetitive element in an array.
"""

numbers = [1, 3, 1, 5, 6, 2, 9, 9, 1, 1, 13, 6, 11, 45, 67, 33, 76, 21, 9, 9, 9]
value = max(set(numbers), key=numbers.count)
print(value)

