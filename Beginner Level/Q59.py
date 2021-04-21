"""
Write a Python program to test whether all numbers of a list is greater than a certain number.
"""

container = [29, 71, 45, 32, 67]

# Method-1
for n in container:
    if n <= 45:
        print(f'{n} is less than 500')
    else:
        print(f'{n} is greater than 500')
