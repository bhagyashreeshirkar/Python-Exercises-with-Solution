"""
Write a Python function to check whether a number is divisible by another number.
Accept two integers values form the user.
"""

print('Enter two numbers:')
a, b = map(int, input().split(','))

if a % b == 0:
    print(f'{a} is divisible by {b}')
else:
    print(f'{a} is not divisible by {b}')


