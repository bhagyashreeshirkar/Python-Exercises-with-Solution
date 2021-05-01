"""
Note:
    A heap is created by simply using a list of elements with the heapify function.

heapify – This function converts a regular list to a heap.
          In the resulting heap the smallest element gets pushed to the index position 0.
          But rest of the data elements are not necessarily sorted.

heappush – This function adds an element to the heap without altering the current heap.

heappop – This function returns the smallest data element from the heap.

heapreplace – This function replaces the smallest data element with a new value supplied in the function.

heapq.nlargest - This method is used to return n largest element from the heap.

heapq.nsmallest - This method is used to return n smallest element from the heap.

"""