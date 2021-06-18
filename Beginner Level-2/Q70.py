"""
Write a program to print the following output.

Example:
Input: [47, 49, 36, 98, 90]
Output: [36, 47, 90, 49, 98]
(In the given array, 36 is the smallest number hence we start with it and arrange the series as sorted odd-even alternatively.)
"""
x = list(map(int, input().split(',')))

final = [min(x)]
x.remove(min(x))

odd_num = []
even_num = []
for i in sorted(x):
    if i % 2 == 1:
        odd_num.append(i)
for j in sorted(x):
    if j % 2 == 0:
        even_num.append(j)

a1 = len(odd_num)
a2 = len(even_num)
for n in range(max(a1, a2)):  # It means it will start from 0 to max(a1, a2)
    if n < a1:
        final.append(odd_num[n])
    if n < a2:
        final.append(even_num[n])

print(final)
