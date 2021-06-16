"""
Write a Python program to find the digits which are absent in a given mobile number.

Sample Input:
9, 8, 3, 2, 2, 0, 9, 7, 6, 3
Sample Output:
Absent digits are = 1, 4, 5
"""

mobile_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
absent_digits = []
values = list(map(int, input('Enter mobile numbers: ').split(',')))
for n in mobile_numbers:
    if n not in values:
        absent_digits.append(n)
print('Absent digits are: ', absent_digits)
