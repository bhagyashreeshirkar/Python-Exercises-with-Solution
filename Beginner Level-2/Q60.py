"""
Write a python program that accepts a string and display total number of upper and lower case characters.
Example:
The quick Brown Fox
Upper case characters: 3
Lower case characters: 13
"""

string = input()

# my_str is used to remove spaces in the string
my_str = ''
for a in string:
    if a != ' ':
        my_str += a

upper_letters = []
lower_letters = []

for n in my_str:
    if n == n.upper():
        upper_letters.append(n)
    if n == n.lower():
        lower_letters.append(n)

print(f'Upper case characters: ', len(upper_letters))
print(f'Lower case characters: ', len(lower_letters))
