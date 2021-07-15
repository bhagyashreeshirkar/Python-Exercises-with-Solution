"""
Write a program to find pairs of elements whose sum is equal to the given value.

Example:
Input:
5
1 3 4 7 5
7
Output:
[3, 4]
"""

n = int(input())
arr = list(map(int, input().split(' ')))[:n]
sum = int(input())

pair = []
for i in arr:
    for j in arr:
        if i + j == sum:
            pair.append(i) and pair.append(j)

print(pair)
