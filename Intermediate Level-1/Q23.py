"""
Write a program to find the maximum difference between two adjacent numbers in an array of positive integers.

Example:
Input:
5
10 11 7 12 14
Output:
4
Explanation:
10-11 = -1
11-7 = 4
7-12 = -5
12-14 = -2, so maximum difference is 4
"""

n = int(input())
arr = list(map(int, input().split()))[:n]

distances = []
s = arr[0]
for i in arr[1:]:
    distances.append(s-i)
    s = i

print(max(distances))  # Method-1

# Method-2
m = 0
for n in distances:
    if n > m:
        m = n
print(m)

