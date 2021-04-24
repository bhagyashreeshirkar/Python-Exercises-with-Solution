"""
Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
Note: Do not use built-in functions.
"""

# To find maximum Number
numbers = [33, 56, 12, 10, 10, 8, 100, 100, 21]

temp = numbers[0]  # assign first element of a list to temp variable

for number in numbers:
    if number >= temp:
        temp = number
print(temp)

# To find minimum number
numbers = [33, 56, 12, 10, 10, 8, 100, 100, 21]

temp = numbers[0]  # assign first element of a list to temp variable

for number in numbers:
    if number <= temp:
        temp = number
print(temp)
