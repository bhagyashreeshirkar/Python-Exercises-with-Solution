"""
Write a program to return the difference between the largest and smallest numbers from an array of positive integers.

Example:
Input:
5
10 11 7 12 14
Output:
7
(Explanation: The first parameter is the size of the array. Next is an array of integers.
The difference between largest(14) and the smallest(7) is 7.)
"""

n = int(input())
arr = list(map(int, input().split()))[:n]

# Method-1
largest = arr[0]
smallest = arr[0]

for i in arr:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print(largest - smallest)


# Method-2
print(max(arr) - min(arr))
