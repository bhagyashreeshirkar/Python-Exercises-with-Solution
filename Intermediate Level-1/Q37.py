"""
Niven Numbers-
Niven numbers are positive integers greater than 0 that are divisible by the sum of their digits.
For Example, 42 is a Niven number, it is divisible by 4+2=6; 42/6=6 hence output will be 6.
(Note: If it isn't a Niven number, return 0.)

Example1:
Input: 36
Output: 4
(Explanation: 3+6=9; hence 36/9 =4)

Example1:
Input: 57
Output: 0
(Explanation: 5+7=12; hence 57/12, remainder is not equal to 0. therefore 57 is not a Niven number)
"""

def checkNivenNumber(num):
    sum = 0
    for n in str(num):
        sum += int(n)
    # return sum

    if num % sum == 0:
        return num// sum
    else:
        return 0

print(checkNivenNumber(36))
print(checkNivenNumber(57))
print(checkNivenNumber(30))
