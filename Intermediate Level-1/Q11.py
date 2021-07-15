"""
Have the function StringChallenge(sen) take the sen parameter being passed and return the longest word in the string.
If there are two or more words that are the same length, return the first word from the string.
*** Words may also contain numbers, for example 'Hello world123 567' ***

Example1:
Input: fun&!! time
Output: time

Example2:
Input: I love dogs
Output: love
"""

def StringChallenge(sen):

    other_char = ['!', '@', '#', '%', '^', '&', '*', '(', ')', '-', '=', '+']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for n in sen:
        if n in other_char or n in num:
            sen = sen.replace(n, '')

    words = sen.split()
    m = []
    for word in words:
        m.append(len(word))
    a = max(m)
    for word in words:
        if len(word) == a:
            return word


print(StringChallenge('I love dogs'))
print(StringChallenge('fun&!! time'))
print(StringChallenge('Hello world123 567'))
