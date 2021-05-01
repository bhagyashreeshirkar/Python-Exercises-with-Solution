"""
Write a Python program to count the number of even and odd numbers from a series of numbers.

Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

Expected Output :
Number of even numbers : 4
Number of odd numbers : 5
"""


def values(numbers):
    even_numbers = 0
    odd_numbers = 0
    for n in numbers:
        if n % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1

    print(f'Number of even numbers: {even_numbers}')
    print(f'Number of odd numbers: {odd_numbers}')


values((1, 2, 3, 4, 5, 6, 7, 8, 9))
values((33, 56, 21, 88, 10, 12, 44, 67, 31, 69, 100, 102))
