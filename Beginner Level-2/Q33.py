"""
Write a Python program to create a sequence where the first four members of the sequence are equal to one,
and each successive term of the sequence is equal to the sum of the four previous ones.
Find the Nth member of the sequence.
Sample Sequence -
seq     = 1 1 1 1 4 7 13 25 49,..
Nth num = 1 2 3 4 5 6  7  8  9
"""
def value(num):
    a, b, c, d = 1, 1, 1, 1
    for n in range(4, num):
        e = a + b + c + d
        d, c, b, a = e, d, c, b
    print(e)


value(5)
value(6)
value(9)
