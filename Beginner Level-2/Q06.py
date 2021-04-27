"""
Write a Python program to count the number of each character of a given text of a text file.
"""
file = open('Q06.txt')
text = file.read()

temp = {}
for ch in text:
    if ch in temp:
        temp[ch] += 1
    else:
        temp[ch] = 1
print(temp)
