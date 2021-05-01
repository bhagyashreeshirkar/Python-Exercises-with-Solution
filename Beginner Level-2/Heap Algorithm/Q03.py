"""
Write a python program to remove an element into a heap.
"""

import heapq

numbers = [2, 50, 67, 12, 3, 4]
heapq.heapify(numbers)
print(numbers)

heapq.heappop(numbers)  # This function returns the smallest data element from the heap.
print(numbers)
