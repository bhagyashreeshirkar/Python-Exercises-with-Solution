"""
Write a program to find squares of odd and even numbers from range 1 to 10.
"""
even_numbers = [i * i for i in range(1, 11) if i % 2 == 0]
print(f'squares of even numbers', even_numbers)

odd_numbers = [i * i for i in range(1, 11) if i % 2 == 1]
print(f'squares of odd numbers', odd_numbers)
