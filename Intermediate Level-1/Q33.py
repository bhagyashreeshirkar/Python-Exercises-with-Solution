"""
Write a program to display sum of squares of even digits in a number.
Note:
* If the number is 0 or less than 0, then display it as 'Number cannot be 0 or negative'.
* If the number is grater than 32767, then display it as 'Number exceeds the limit'.
* If the input does not contain an even number then display it as 'Even Digits does not found'.

Example1:
Input:
2798
Output:
68
(Explanation: as 2798 contains  2 even numbers 2 and 8 hence, 2^2 + 8^2 = 4+64=68)
"""

def SumOfEvenNumbers(num):
    n = []
    final_value = 0
    even_num = []

    for i in str(num):
        n.append(int(i))
    if num <= 0:
        return 'Number cannot be 0 or negative'
    elif num > 32767:
        return 'Number exceeds the limit'
    else:
        for k in n:
            if k % 2 == 0:
                even_num.append(k)
                final_value += k**2
        if len(even_num) == 0:
            return 'Even Digits does not found'

    # print(even_num)
    return final_value


print(SumOfEvenNumbers(2798))
print(SumOfEvenNumbers(6588))
print(SumOfEvenNumbers(1353))
print(SumOfEvenNumbers(99023))
print(SumOfEvenNumbers(0))
