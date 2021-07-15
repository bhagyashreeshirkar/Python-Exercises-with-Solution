"""
Given a singly linked list of size N. The task is to rotate the linked list counter clockwise by k nodes.
where k is a given positive integer smaller than or equal to length of the linked list.

Example:
Input:
5
2 4 7 8 9
2
Output:
8 9 2 4 7
"""

n = int(input())
arr = list(map(int, input().split(' ')))[:n]
k = int(input())

list = []
for i in arr:
    a = arr.index(i) + k
    if a < n:
        list.insert(a, i)
    else:
        list.insert((arr.index(i) - k)-1, i)
# print(list)

s = ' '.join(str(e) for e in list)  # To convert list into string to get proper output
print(s)
