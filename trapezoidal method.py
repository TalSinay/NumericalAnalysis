import math
from sympy import *

def simpson(f,a,b,n):
	h = float((b-a)*1.0/n*1.0)
	m = int(n/2)
	s0 = f(a)+f(b)
	s1 = 0
	for i in range(1,2*m,2):
			s1=s1+f(a+h*i)
	s2=0
	for i in range(2,2*m,2):
			s2=s2+f(a+h*i)
	return h/3*(s0+4*s1+2*s2)

def Trapezoidal(f, a, b, n):
    h = float(b - a)/n
    s = 0.0
    s += f(a)+f(b)
    for i in range(1, n):
        s += sum([2* f(a + i*h)])
    s *= h/2.0
    return s

pi=math.pi
x = symbols('x')
f=simplify(sin(x))
f=lambdify(x,f)
print(Trapezoidal(f,0,pi,100))
print(simpson(f,0,pi,4))