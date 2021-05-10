"""
Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
also create a lambda function that multiplies argument x with argument y and print the result.
"""

value = lambda n: n + 15
print(value(10))

value2 = lambda x, y: x * y
print(value2(5, 6))
