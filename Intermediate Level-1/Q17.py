"""
The input consist of an integer billAmount, representing the total bill amount of a customer.
Write a program to print an integer representing the discount amount for the given total bill.

Example:
Input:
2514795
Output:
162
(Explanation: Odd digits in the given number 2514795 are 5,1,7,9,5. The sum of these odd digits is 27.
Similarly, Even digits are 2, 4 with sum of 6. so output is 27 x 6 = 162)
"""

def billAmount(amount):
    amount = str(amount)

    list_of_amount = [int(i) for i in amount]

    even = 0
    odd = 0
    for n in list_of_amount:
        if n % 2 == 0:
            even += n
        else:
            odd += n

    print(even*odd)


billAmount(2514795)
