"""
Have the function StringChallenge(string) take the string parameter being passed and return a compressed version
of the string using the run length coding algorithm. This algorithm works by taking the occurrence of each repeating
character and outputting that number along with a single character of the repeating sequence.
For example, 'wwwggopp' would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbol.

Example:
Input: 'aabbcde'
Output: 2a2b1c1d1e
"""

def StringChallenge(string):
    temp = {}
    for ch in string:
        if ch in temp:
            temp[ch] += 1
        else:
            temp[ch] = 1

    final_str = ''
    for i in temp:
        a = temp.get(i)  # To get value of each key and append it to final_string
        final_str += str(a)  # To get a key and append it to final_string
        final_str += i

    print(final_str)


StringChallenge('wwwggopp')
StringChallenge('aabbcde')
