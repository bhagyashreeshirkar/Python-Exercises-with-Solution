"""
Write a program that takes two strings S1 and S2 as input(one per line).
The program checks if the string S1 can be created by rearranging the characters of string S2 and vice versa.
If yes the program should print YES; NO otherwise. The program should ignore the case sensitivity of characters.
Example1:
Input:
Bat
TAB
Output:
YES

Example2:
input:
abcdef
efdabd
Output:
NO
"""

S1 = input()
S2 = input()

S1_char = []
S2_char = []

for a in S1:
    S1_char.append(a.lower())
    S1_char.append(a.upper())
for b in S2:
    S2_char.append(b.lower())
    S2_char.append(b.upper())

if sorted(S1_char) == sorted(S2_char):  # comparing 2 lists
    print('YES')
else:
    print('NO')
