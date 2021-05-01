"""
Write a Python program to guess a number between 1 to 9.
Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct,
on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""
import random

number = random.randint(1, 10)

while True:
    user_guess = int(input('Enter a number: '))
    if user_guess == number:
        print('Well guessed!')
        break
    else:
        print('Try again!')
