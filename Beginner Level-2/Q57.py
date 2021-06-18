"""
Write a Python program which solve the equation:
ax+by=c
dx+ey=f
Print the values of x, y where a, b, c, d, e and f are given. a,b,c,d,e,f separated by a single space.

Example:
Input:
Input the value of a, b, c, d, e, f:
5 8 6 7 9 4
Output:
Values of x and y: -2.000, 2.000
"""
a, b, c, d, e, f = map(int, input('Input the value of a, b, c, d, e, f: \n').split(' '))
y = (d*c - f*a)/(b*d - a*e)
x = (c/a) - ((b * y)/a)
print(f'Values of x and y: {x:.3f}, {y:.3f}')
