"""
Write a python program to count each letter(character) repeated in a string.
"""
string = 'This is my vlog. This is my New Youtube channel'


# Method-1
temp = {}  # assigning an empty dictionary

for ch in string:
    if ch in temp:  # This is the way you can add characters into a dictionary;
        temp[ch] += 1  # if there's already a character present in it add 1 to its value whenever character repeats
    else:
        temp[ch] = 1  # else by adding character to a dictionary assign its value as 1
print(temp)


# Method-2
for ch in set(string):
    print(f'{ch} = {string.count(ch)}', end=',')
