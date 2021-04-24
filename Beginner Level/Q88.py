"""
Write a program to remove duplicates from an array.
"""

numbers = [1, 3, 1, 5, 6, 2, 9, 9, 1, 1, 13, 6, 11, 45, 67, 33, 76, 21]

# Method-1
temp = []
for number in numbers:
    if number not in temp:
        temp.append(number)
print(temp)

# Method-2
print(set(numbers))
