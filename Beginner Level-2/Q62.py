"""
Write a program in which you have to check if a string contains only digits or not. If yes then display true otherwise false.
Example1:
Input:
8468
Output:
true

Example2:
Input:
ab23
Output:
false
"""
value = input()

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
string = ''
for n in value:
    for i in digits:
        if n == i:
            string += i

if string == value:
    print('true')
else:
    print('false')
