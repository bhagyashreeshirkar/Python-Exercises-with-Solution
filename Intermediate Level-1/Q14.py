"""
Have the function MathChallenge(num) take the num parameter being passed which will be an integer and return the string
True if it's a power of two. If it's not then return the string False.
For example, if the input is 16 then your program should return the string True
but if the input is 22 then the output should be False.

Examples:
Input: 4
Output: True

Input: 124
Output: False
"""

def MathChallenge(num):
    powers_of_2 = []
    temp = 1
    b = 0
    while b <= num:
        b = 2 ** temp
        powers_of_2.append(b)
        temp += 1
    # print(powers_of_2)

    if num in powers_of_2:
        return True
    else:
        return False


print(MathChallenge(4))
print(MathChallenge(123))
print(MathChallenge(16))
print(MathChallenge(22))
