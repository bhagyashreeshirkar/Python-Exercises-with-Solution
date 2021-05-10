"""
Write a Python program to create a function that takes one argument,
and that argument will be multiplied with an unknown given number.
Sample Output:
Double the number of 15 = 30
Triple the number of 25 = 75
"""


def compute(n):
    return lambda x: x * n


result = compute(2)  # ie, n = 2
print(result(15))  # ie, x = 15

result = compute(3)  # ie, n = 2
print(result(25))  # ie, x = 25
