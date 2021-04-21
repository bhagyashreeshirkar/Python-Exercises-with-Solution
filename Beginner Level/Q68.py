"""
Write a Python program to filter the positive numbers from a list.
"""

numbers = [5.3, 77, -66, 23, -1, -33, 89, 100]

# Method-1
positive_numbers = []
for number in numbers:
    if number == abs(number):
        positive_numbers.append(number)

print(positive_numbers)


# Method-2 (List comprehension)
positive_numbers = [number for number in numbers if number == abs(number)]
print(positive_numbers)
