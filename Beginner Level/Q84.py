"""
Write a Python program to extract values from a dictionary and print addition of them.
Sample Example:
dictionary = {'Apple': 3, 'Orange': 5}
addition: 8
"""

# Method-1
fruits = {'Apple': 3, 'Orange': 5}
a = fruits.values()
print(f'Addition of fruits are:', sum(a))


# Method-2
fruits = {'Apple': 3, 'Orange': 5}
a, b = fruits.values()
print(f'Addition of fruits are:', a + b)
