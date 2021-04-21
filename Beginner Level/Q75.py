"""
Write a Python program to check whether lowercase letters exist in a string.
"""
string1 = 'HI'
string2 = 'I am John'


print(any(ch.islower() for ch in string1))
print(any(ch.islower() for ch in string2))
