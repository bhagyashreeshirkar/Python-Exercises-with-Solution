"""
Write a Python program to find whether a given number (accept from the user) is even or odd,
print out an appropriate message to the user.
"""

value = int(input('Enter a number: '))
if value > 0:    # value must be positive integer
    if value % 2 == 0:
        print('Even number')
    else:
        print('Odd number')
else:
    print('Invalid number')
