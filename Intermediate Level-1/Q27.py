"""
Write a program to sort each word in sentence in ascending order.

Example:
Input:
hello how are you

output:
are hello how you
"""

string = input()

words = string.split()  # splits sentence into words
h = sorted(words)  # sort function to sort words in a list
print(' '.join(h))  # after sorting it will join words to form a sentence
