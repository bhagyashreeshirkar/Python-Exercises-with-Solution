"""
Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on.
Continues this operation until the number is positive.
"""


def value(num):
    temp = num
    while temp > 0:
        sum = 0
        string = str(temp)
        for n in string:
            sum += int(n)
        sub = temp - sum
        temp = sub
        print(sub, end=' ')
    print()


value(21)
value(45)
value(201)
