"""
Write a Python program to test whether a passed letter is a vowel or not.
"""

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def guess(letter):
    if letter in vowels:
        return 'It is a vowel'
    else:
        return 'It is a consonant'


print(guess('k'))
print(guess('A'))
print(guess('i'))
