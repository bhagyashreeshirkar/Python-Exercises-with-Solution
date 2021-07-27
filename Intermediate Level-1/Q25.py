"""
A kid from UKG learnt to write numbers from 20 to 30. When requested, K repeating few of them.
Teacher noticed that kid has left out few numbers. Write a function 'validateNumberSequence' that helps finding the
left out numbers and the numbers repeat more than once.

Example1:
Input:
[20, 21, 22, 23, 25, 26, 28, 29, 30]
Output:
[24, 27]

Example2:
Input:
[20, 21, 22, 22, 25, 23, 26, 29, 28, 30]
Output:
[22, 24, 27]
"""

def validateNumberSequence(arr):
    temp = []
    final_list= []

    for i in arr:
        if i in temp:
            final_list.append(i)
        else:
            temp.append(i)

    for j in range(20, 31):
        if j not in arr:
            final_list.append(j)

    print(final_list)
a = list(map(int, input().split(',')))


validateNumberSequence(a)
