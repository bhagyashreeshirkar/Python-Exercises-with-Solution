"""
Write a Python program to get the least common multiple (LCM) of two positive integers.
LCM = It is a least common number with comes in the multiplication table of both the numbers

mathematical logic-
for eg; 12, 24
12 = 12, 24, 36, 48, 60,..
24 = 24, 48, 72, 76, 120,..
since 24 is smallest common number in the multiplication table of both the numbers;
hence, LCM of 12 and 24 is 24

Programming logic-
when if max(12, 24) = 24 gets divided by both 12 and 24 gives remainder 0 then LCM is max(12, 24) ie, 24
and if not then it'll increment max(12, 24) ie, 24 by 1(25, 26, 27,..) until it prints a number which divides both the numbers
"""
# Method-1
import math


def numbers(a1, a2):
    print(math.lcm(a1, a2))


numbers(4, 6)
numbers(15, 17)


# Method-2
def lcm(n1, n2):
    maxNum = max(n1, n2)
    while True:
        if maxNum % n1 == 0 and maxNum % n2 == 0:
            break  # as we want only first number(which will least number) which gets divisible by both, we break the loop
        else:
            maxNum = maxNum + 1
    print(maxNum)


lcm(4, 6)
lcm(15, 17)
