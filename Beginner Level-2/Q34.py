"""
Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on.
Continues this operation until the number is positive.
Sample Example:
num = 21
21 - (2+1) = 18
18 - (1+8) = 9
9 - (9) = 0
Output: [18, 9, 0]
"""

def number(num):
    list_of_numbers = []
    while num > 0:
        answer = num - sum([int(n) for n in str(num)])
        list_of_numbers.append(answer)
        num = answer
    print(list_of_numbers)


number(52)
number(21)
