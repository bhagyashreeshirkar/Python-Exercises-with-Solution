"""
Write a program to find sum of square roots among user entered numbers.

Example:
Input:
arr: 5 4 10 9 8 4 49
Output:
14 (perfect squares among all are 4, 9, 4 and 49; hence, 2+3+2+7 = 14)

Input:
arr: 16 7 81 24 36 40
Output:
19 (4+9+6 = 19)
"""

values = list(map(int, input('arr: ').split(' ')))

numbers = []
for n in values:
    a = round(n ** 0.5)
    if a * a == n:
        numbers.append(a)
print(sum(numbers))
