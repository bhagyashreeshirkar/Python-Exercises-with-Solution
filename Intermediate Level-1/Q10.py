"""
Have the function StringChallenge(sen) take the sen parameter being passed and return the longest word in the string.
If there are two or more words that are the same length, return the first word from the string.

Example1:
Input: Python is an amazing language
Output: language

Example2:
Input: I love dogs
Output: love
"""

def StringChallenge(sen):
    words = sen.split()
    m = []
    for word in words:
        m.append(len(word))
    a = max(m)
    for word in words:
        if len(word) == a:
            return word

print(StringChallenge('Python is an amazing language'))
print(StringChallenge('I love dogs'))
