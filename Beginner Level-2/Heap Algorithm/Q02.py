"""
Write a python program to add an element into a heap.

Note:
    Inserting a data element to a heap always adds the element at the last index.
    But you can apply heapify function again to bring the newly added element to the first index only if it smallest in value.
    In the below example we insert the number 8.
"""
import heapq

numbers = [22, 45, 17, 67, 34, 12, 9]
heapq.heapify(numbers)
print(numbers)  # to perform heap methods first we always need to convert a list into heap bu using heapify method

heapq.heappush(numbers, 8)  # Inserting a new element
print(numbers)
