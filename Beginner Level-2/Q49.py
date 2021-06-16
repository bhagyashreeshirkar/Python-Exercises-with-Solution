"""
Write a Python program to find the number of divisors of a given integer is even or odd.
Sample Input1:
15
Sample Output1:
No of divisors = 1, 3, 5 = 3 = Odd

Sample Input2:
9
Sample Output2:
No of divisors = 1, 3 = 2 = Even
"""

value = int(input('Enter Number: '))
divisors = []
for i in range(1, value):
    if value % i == 0:
        divisors.append(i)
no_of_divisors = len(divisors)
print(f'Divisors:', divisors)
print(f'No of divisors:', no_of_divisors)
if no_of_divisors % 2 == 0:
    print('Even')
else:
    print('Odd')
