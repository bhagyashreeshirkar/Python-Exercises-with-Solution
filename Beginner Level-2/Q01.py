"""
Write a Python function that takes a sequence of numbers & determines whether all the numbers are different from each other.
"""


def values(numbers):
    a = ''  # assigning a variable to make it True or false depending upon the conditions
    temp = 0  # assigning a temp variable to make comparison between previous and current element of the list
    for number in numbers:
        if temp == number:
            a = 'There is a chance of repetition'
            break
        else:
            a = 'All the numbers are different from each other'
        temp = number
    print(a)


values([55, 102, 345, 345, 1100])
values([2, 4, 5, 5, 7, 9])
values([2, 4, 5, 7, 9])
