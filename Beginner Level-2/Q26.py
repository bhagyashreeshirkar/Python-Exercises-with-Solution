"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""


def values(numbers):
    new = []
    for n in numbers:
        if n not in new:
            new.append(n)
    print(f'Unique List:', new)


values([1, 2, 3, 3, 3, 3, 4, 5])
