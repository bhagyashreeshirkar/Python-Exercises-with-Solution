"""
(An anagram is a word, phrase or name formed by rearranging the letters of another word, phrase or name.)
Write a program to check of two given strings are anagrams or not. Return 'Yes' if they are anagrams, otherwise return 'No'.

Example1:
Input1: listen
Input2: silent
Output: Yes

Example2:
Input1: bad
Input2: dad
Output: No

"""
input1 = input('Input1: ')
input2 = input('Input2: ')

# Method1
if sorted(input1) == sorted(input2):
    print('Yes')
else:
    print('No')
