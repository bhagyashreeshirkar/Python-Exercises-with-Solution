"""
Write a Python program which iterates the integers from 1 to 50.
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz ..
"""

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        continue
    elif i % 3 == 0:
        print('Fizz')
        continue
    elif i % 5 == 0:
        print('Buzz')
        continue
    else:
        print(i)

'''Note: if we don't use continue statement then for 15, 30, 45 numbers it will print Fizzbuzz Fizz Buzz all three
Thus we have used continue statement it will skip 15, 30, 45 for next 2 elif statements; and same for both of them'''
