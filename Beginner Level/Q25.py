"""
Write a Python program to concatenate all elements in a list into a string and return it.
Sample Input:
[2, 3, 1, 4, 22]
Sample Output:
231422
"""


def concatenate(list):
    temp = ''
    for element in list:
        temp = temp + str(element)
    print(temp)    # It will directly print final range of for loop


concatenate(['hello', 'my', 'name', 'is', 'John'])
concatenate([2, 3, 1, 4, 22])
