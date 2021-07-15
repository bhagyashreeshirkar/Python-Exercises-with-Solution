"""
Write a program to find two numbers and print their index else print -1.

Example:
Input: 3, 6, 7, 8, 9
7
9
Output:
Element 1 index = 2
Element 2 index = 4
"""

arr = list(map(int, input().split(',')))
a = int(input())
b = int(input())

for n in arr:
    if a == n:
        print(f'Element 1 index = {arr.index(n)}')
    if b == n:
        print(f'Element 2 index = {arr.index(n)}')
