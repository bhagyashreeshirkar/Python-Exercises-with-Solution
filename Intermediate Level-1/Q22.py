"""
Write a program to print an integer representing the sum of the energy of the two chemicals which produces maximum
energy on reaction.

Example:
Input:
7
9 -3 8 -6 -7 8 10
Output:
19
(Explanation: The maximum product of the energies is 90 ie, 9x10. so, the sum of the energies of the chemicals is 19.)
"""

n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)
pseudo_arr = arr

multiples = []

for i in arr:
    pseudo_arr.remove(i)
    for n in pseudo_arr:
        multiples.append(i*n)
        if max(multiples) == i*n:
            sum = i + n
    pseudo_arr.append(i)


print(sum)
# print(multiples)
