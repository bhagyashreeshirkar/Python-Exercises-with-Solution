"""
Write a program to print the calculated molecular mass.
Constraints -
Element symbols can only be capital letters
Element symbols can only be one of the following - H, C, N, O, S

Example1:
Input: C6H6
Output: 78
(The molecular mass of Benzene(C6H6)
= 6*atomic mass of carbon + 6*atomic mass of hydrogen
= 6*12 + 6*1
= 72 + 6 = 78)

Example2:
Input: H2O
Output: 18

"""
from molmass import Formula


def calMolecularMass(element):
    # return f'{Formula(element).mass:.2f}'
    return int(Formula(element).mass)

print(calMolecularMass('H2O'))
print(calMolecularMass('C6H6'))
