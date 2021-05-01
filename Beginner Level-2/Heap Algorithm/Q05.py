"""
Write a program to print first 3 smallest numbers from a heap and first 4 largest numbers from a heap.
"""

import heapq

numbers = [33, 21, 45, 6, 78, 11, 34, 117, 89, 90, 100]
heapq.heapify(numbers)
print(f'heap:', numbers)

new_SH = heapq.nsmallest(3, numbers)  # to find first 3 smallest numbers
print(f'first 3 smallest numbers:', new_SH)

new_LH = heapq.nlargest(4, numbers)  # to fins first 4 largest numbers
print(f'first 4 largest numbers:', new_LH)
