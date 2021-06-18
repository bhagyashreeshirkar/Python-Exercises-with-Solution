"""
Write a program to merge two lists alternatively into single list.

Example:
Input:
List1: [1, 3, 5, 7, 9]
List2: ['a', 'b', 'c', 'd', 'e', 'f']
Output:
[1, 'a', 3, 'b', 5, 'c', 7, 'd', 9, 'e', 'f']
"""

def lists(list1, list2):

    final_list = []

    l1 = len(list1)
    l2 = len(list2)

    a = max(l1, l2)

    for i in range(a):
        if i < l1:
            final_list.append(list1[i])
        if i < l2:
            final_list.append(list2[i])

    return final_list


print(lists([1, 3, 5, 7, 9], ['a', 'b', 'c', 'd', 'e', 'f']))
print(lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
