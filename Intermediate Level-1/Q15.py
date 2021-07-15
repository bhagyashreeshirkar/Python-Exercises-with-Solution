"""
Write a python program to display the following output. n should be even number and m should be the half of n.

Example1:
Input:
8
7 43 12 4 1 3 78 6
4
Output:
1 3 4 6 78 43 12 7
(Explanation:- n = 8 so next line would 8 numbers; if user enters m = 4 then among those 8 numbers first 4 numbers
would in ascending order and remaining 4 numbers would be in descending order.)

Example2:
Input:
10
1 2 3 4 5 6 7 8 9 10
5
Output:
1 2 3 4 5 10 9 8 7 6
"""
n = int(input())
arr = list(map(int, input().split()))[:n]
m = int(input())

sorted_arr = sorted(arr)
reversed_arr = sorted(arr, reverse=True)

final_list = []

for i in sorted_arr[:m]:
    final_list.append(i)
for j in reversed_arr[:m]:
    final_list.append(j)

# print(final_list)

s = ' '.join(str(e) for e in final_list)
print(s)  # To convert list into string to get proper output
