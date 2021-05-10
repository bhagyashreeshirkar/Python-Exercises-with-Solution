"""
Write a Python program to find the value of n where n degrees of number 2 are written sequentially in a line without spaces.
Sample Example:
248163264 = 6 (2,4,8,16,32,64) ie, 2^6
"""


def value(n):
    a = ''
    for i in range(1, 100):
        a = a + str(pow(2, i))  # string concatenation for eg; ('abc' + 'def') = abcdef
        if n == a:
            print(i)
            break


value('248163264')
value('24')
value('248163264128256')
