"""
Write a python program to replace an element from a heap.

Note:
The heapreplace function always removes the smallest element of the heap and
inserts the new incoming element at some place not fixed by any order.
"""
import heapq

numbers = [33, 21, 2, 5, 67, 1, 10]
heapq.heapify(numbers)
print(numbers)

heapq.heapreplace(numbers, 11)  # It will replace a smallest number(ie, 1) by 11.
print(numbers)
