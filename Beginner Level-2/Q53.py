"""
Write a Python program to compute the digit number of sum of two given integers.
Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 ≤ x, y ≤ 1,000,000
Sample Input1:
Input two integers(a b): 5 7
Sample Output1:
sum = 12
Number of digit of a and b: 2

Sample Input2:
Input two integers(a b): 25 100
Sample Output2:
sum = 125
Number of digit of a and b: 3
"""

a, b = map(int, input('Input two integers(a b): ').split(' '))
sum = a + b
print(f'Sum:', sum)
print(f'Number of digit of sum of a and b:', len(str(sum)))
