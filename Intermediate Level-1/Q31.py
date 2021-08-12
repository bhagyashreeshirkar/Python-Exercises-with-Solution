"""
You are given an arr of size N. Your task is to find and print the maximum element of the array along with the index.
Note:
* Array index starts with 0.
* The minimum element and its index should be separated by a line in the output.

Input Format: The input consists of two lines-
The first line contains N.
The second line contains arr.

Output Format: The output consists of two lines-
Print the minimum element in the first line.
Print the index of the minimum element in the second line.

Example:
Input:
10
23 45 82 27 66 12 78 13 71 86
Output:
12
5

Example2:
Input2:
8
1 9 11 144 6 7 112 95
Output2:
1
0
"""

n = int(input())
arr = list(map(int, input().split(' ')))[:n]

sorted_arr = sorted(arr)
min_element = sorted_arr[0]

print(min_element)
print(arr.index(min_element))
