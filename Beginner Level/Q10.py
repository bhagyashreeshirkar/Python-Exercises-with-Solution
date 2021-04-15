"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
[ 5
  5 5
  5 5 5 ]
  ie, 5 + 55 + 555 = 615
"""

n = int(input('Enter the value of n: '))
a = int(('%s' % n))
b = int(('%s%s' % (n, n)))
c = int(('%s%s%s' % (n, n, n)))  # since a, b, c are in string format hence, we've to convert it into an integer
print(a + b + c)
