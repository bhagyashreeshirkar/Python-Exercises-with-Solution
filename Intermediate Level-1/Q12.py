"""
Have the function SecondGreatLow(arr) take the array of numbers stored in arr and
return the second lowest and second highest numbers, respectively separated by a space.

Example1:
Input: [1, 42, 42, 180]
Output: 42 42

Example2:
Input: [4, 90]
Output: 4 90

Example3:
Input: [34, 22, 21, 67, 80, 9, 15]
Output: 15 67
"""

def SecondGreatLow(arr):
    sorted_arr = []
    a = len(arr)

    while a > 0:
        b = min(arr)
        sorted_arr.append(b)
        arr.remove(b)
        a = a - 1
    # print(sorted_arr)

    if len(sorted_arr) > 2:
        print(sorted_arr[1], sorted_arr[-2])
    else:
        print(sorted_arr[0], sorted_arr[1])


SecondGreatLow([1, 42, 42, 180])
SecondGreatLow([4, 90])
SecondGreatLow([34, 22, 21, 67, 80, 9, 15])
