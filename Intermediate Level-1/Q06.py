"""
Write a program to segregate 0s and 1s.You are given an array of 0s and 1s in random order.
Segregate 0s on left side and 1s on right side of an array.
Example:
Input:
6
0 1 0 1 1 1
Output:
0 0 1 1 1 1
"""
n = int(input())
arr = list(map(int, input().split(' ')))[:n]

zeroes = []
ones = []
for n in arr:
    if n == 0:
        zeroes.append(n)
    else:
        ones.append(n)

zeroes.extend(ones)

final = ''
for i in zeroes:
    final += str(i)
print(' '.join(final))
