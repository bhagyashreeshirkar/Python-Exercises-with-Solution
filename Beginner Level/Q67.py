"""
Write a Python program to input a number, if it is not a number generate an error message.
Sample Test:
Enter a number: jhs
Invalid Input. Try Again...
Enter a number: 44

"""
while True:
    try:
        value = int(input('Enter a number: '))
        break
    except ValueError:
        print('Invalid Input. Try Again...')
