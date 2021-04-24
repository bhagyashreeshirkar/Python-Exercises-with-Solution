"""
Write a Python program to check whether lowercase letters exist in a string.
"""


# Method-1
def enter_string(sentence):
    for ch in sentence:
        if ch.lower() in sentence:
            return True
        else:
            return False


print(enter_string('A8238i823acdeOUEI'))


# Method-2
string = 'A8238i823acdeOUEI'
print(any(ch.lower() for ch in string))
