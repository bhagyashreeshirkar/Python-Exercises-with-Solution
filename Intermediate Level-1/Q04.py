"""
Given a list of non negative integers, arrange them in such a manner that they form the largest number possible
in a string format.

Example:
Input:
5
3 30 34 5 9
Output:
9534330
(Given numbers are [3, 30, 34, 5, 9], the arrangement 9534440 gives the largest value.)
"""
from itertools import permutations


n = int(input())
arr = list(map(int, input().split()))[:n]

p = permutations(arr)
possibilities = [''.join(map(str, m)) for m in p]

# print(possibilities) # map don't change the sequence among a number if we enter 34 then it won't permute it like 43.
print(max(possibilities))
