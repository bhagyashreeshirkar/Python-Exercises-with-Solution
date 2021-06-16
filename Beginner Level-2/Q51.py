"""
Write a python program to find heights of the top three building in descending order from eight given buildings.
0 ≤ height of building (integer) ≤ 10,000
Sample Input:
Input the heights of eight buildings:
 25
 35
 15
 16
 30
 45
 37
 39

Sample Output:
Heights of the top three buildings:
45
39
37
"""

arr = []
# for _ in range(8):  # If we want a specific range of input
for _ in range(int(input('Enter no of buildings: '))):
    heights = input().split('\n')
    for height in heights:
        arr.append(int(height))
arr = sorted(arr)
print(f'Heights of the top three buildings:{arr[-1:-4]}')
