"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
Sample String : 'The quick Brow Fox'
Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""

string = input('String: ')
upper = 0
lower = 0
for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print(f'No. of Upper case characters: ', upper)
print(f'No. of Lower case characters: ', lower)
