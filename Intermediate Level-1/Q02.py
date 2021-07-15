"""
Write a program to display following output. The function accepts an integer 'sum' and an integer 'array' of size n.
** Implement the function to find the least two elements pair and check whether (arr[j] + arr[k] <= sum)
    if True return the product of elements of the pair.
** Return 0 if no such pair found.
** Return -1 if array is empty.

Example1:
Input:
sum: 9
arr: 5 2 4 3 9 7 1
Output: 2
(Pair of least two elements is (1, 2), 1+2 = 3 < 9. Product of 1*2 = 2. Thus, output is 2.

Example2:
Input:
sum: 4
arr: 9 8 3 -7 3 9
Output: -21
"""

def product_smallest_pair(sum, arr):

    new_arr = sorted(arr)
    a1 = new_arr[0]
    a2 = new_arr[1]

    if a1 + a2 <= sum:
        return a1 * a2
    elif len(arr)== 0:
        return '-1'
    else:
        return '0'


s = int(input('sum: '))
a = list(map(int, input('arr: ').split(' ')))

print(product_smallest_pair(s, a))
