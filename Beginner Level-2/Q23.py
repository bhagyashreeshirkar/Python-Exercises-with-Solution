"""
Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
"""

value = int(input('Enter a value: '))
n = 1
for i in range(1, value + 1):
    n = n * i
print(f'factorial of {value} is {n}')
