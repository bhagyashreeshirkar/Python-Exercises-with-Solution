"""
Write a function 'findDuplicatingCharacterWithCount'. Find the characters which gets repeated 3 or more times in the word.
Function should return an empty arr if there is no such word and if occurs make it in uppercase with count in
format "<uppercase_character>-<count>".

Example:
Input:
Bookkeeper
Output:
[E-3]

Input:
aggressiveness
Output:
[E-3, S-4]

Input:
Testing
Output:
[]
"""

def findDuplicatingCharacterWithCount(string):
    count = {}

    for n in string:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1
    # print(count)

    k = []
    for n in count:
        if count[n] >= 3:
            s = f'{n.upper()}-{count[n]}'
            k.append(s)

    print(k)


findDuplicatingCharacterWithCount('Bookkeeper')
findDuplicatingCharacterWithCount('aggressiveness')
findDuplicatingCharacterWithCount('Testing')
