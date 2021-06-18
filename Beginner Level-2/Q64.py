"""
Write a program to print a list in a sorted manner.

Example:
input:
9
14
46
43
27
57
41
45
21
70
Output:
[14, 21, 27, 41, 43, 45, 46, 57, 70]
"""

nums = []
for _ in range(int(input())):
    value = int(input())
    nums.append(value)

print(sorted(nums))
