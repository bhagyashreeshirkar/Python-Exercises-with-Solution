"""
Write a Python program to input two integers in a single line and print addition of them.
"""
# accepting inputs without semicolon
print('Enter values of x and y')
x, y = map(int, input().split())
print(f'values entered:', x, y)
print(f'addition:', x + y)


# accepting inputs including semicolon
print('\nEnter values of x and y')
x, y = map(int, input().split(','))
print(f'values entered:', x, y)
print(f'addition:', x + y)
