from math import *
from sympy import *

def trapez(n, a, b, func):
    h = (b - a)/n
    sum = (func(a) + func(b))/2
    for i in range(1, n):
        sum += func(a + i*h)
    return sum*h

def Romberg(a, b, n, func, eps=0.0001):
    matrix = []
    iter=n
    while(True):
        for i in range(len(matrix) , n):
            tmp=[]
            tmp.append(trapez(iter, a, b, func))
            matrix.append(tmp)
            for j in range(1, i+1):
                matrix[i].append((matrix[i][j-1]*(4**j) - matrix[i-1][j-1])/(4**j - 1))
            iter *= 2
        if abs(matrix[n - 1][n - 1] - matrix[n - 2][n - 2]) < eps :
            break
        iter=iter*2
    return matrix


eps=10**(-5)
a=0
b=1
x = symbols('x')
f = simplify(1/(2+(x**4)))
func = lambdify(x, f)
n=5
matrix=Romberg(a, b, n, func, eps)
print(matrix[len(matrix) - 1][n - 1])
for i in range(len(matrix)):
    print(matrix[i][i])


