"""
Write a python program to display following output.

Example:
Input: [5, 0, 7, 6]
Output: [5, 7, 6, 0]

Input: [0, 3, 0, 2, 0]
Output: [3, 2, 0, 0, 0]
(Explanation:- On shifting the zeroes to the end, the array will change from [0, 3, 0, 2, 0] to [3, 2, 0, 0, 0].
"""

arr = list(map(int, input().split(',')))

num = []
zeroes = []

for i in arr:
    if i !=0:
        num.append(i)
    else:
        zeroes.append(i)

for j in zeroes:
    num.append(j)

print(num)
