"""
check whether a number is armstrong or not.
Armstrong number:
153 = (1*1*1) + (5*5*5) + (3*3*3)
1634 = (1*1*1) + (6*6*6) + (3*3*3) + (4*4*4)
"""


def check(num):
    string = str(num)
    length = len(string)
    value = 0
    for n in string:
        ans = pow(int(n), int(length))
        value += ans
    if num == value:
        return f'{num} is an armstrong number'
    else:
        return f'{num} is not an armstrong number'


print(check(153))
print(check(1634))
print(check(97))
