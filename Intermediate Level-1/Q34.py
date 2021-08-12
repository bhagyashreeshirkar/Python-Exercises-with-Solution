"""
A democratic prime number is the one where only left part of a number is a prime number. Given a number,
write a program to find whether the number is a democratic prime number or not. The given numbers in the input consist
of digits 1 to 9 only.

Example:
Input1: 31566
Output1: democratic prime
Explanation: The left part is 31 which is a prime number, the right part is 66 which is not a prime number.

Input2: 1124
Output2: democratic prime
Explanation: The left part is 11 which is a prime number, the right part is 24 which is not a prime number.

Input3: 512
Output3: non democratic prime
Explanation: The left part is 5 which is a prime number, the right part is 2 which is also a prime number.
"""

num = input()

new_num = list(num)
# print(new_num)

if len(new_num) % 2 != 0:  # even length
    x = ((len(new_num) + 1) - 2) // 2
elif len(new_num) % 2 == 0:  # odd length
    x = (len(new_num) - 2) // 2
# print(x)

n = new_num[:x]
m = new_num[-x:]
# print(n, m)

n1 = ''
n2 = ''

for a in n:
    n1 += a
for b in m:
    n2 += b
# print(n1, n2)


# for recognizing prime numbers
def is_prime(z):
    for k in range(2, z):
        if z % k == 0:
            return False
    else:
        return True


if is_prime(int(n1)) == True and is_prime(int(n2)) == True:
    print('non democratic prime')
else:
    print('democratic prime')
