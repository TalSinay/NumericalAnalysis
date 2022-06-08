import math
from sympy import *

def simpson(f,a,b,n):
	h = float((b-a)*1.0/n*1.0)
	print("h->=",h)
	m = int(n/2)
	s0 = f(a)+f(b)
	print("f(a)+f(b)=",s0)
	s1 = 0
	for i in range(1,2*m,2):
		s1=s1+f(a+h*i)
		print("Interim result ",s1)
	s2=0
	for i in range(2,2*m,2):
		s2=s2+f(a+h*i)
		print("Interim result ", s2)
	return h/3*(s0+4*s1+2*s2)

def Trapezoidal(f, a, b, n):
    h = float(b - a)/n
    s = 0.0
    s += f(a)+f(b)
    for i in range(1, n):
        s += sum([2* f(a + i*h)])
    s *= h/2.0
    return s
e=float(math.e)
pi=math.pi
x = symbols('x')
f=simplify(sin(2*e**(-2*x))/(x**2+5*x+6))
f=lambdify(x,f)
#print(Trapezoidal(f,-0.4,0.4,100))
print("the value is ",simpson(f,-0.4,0.4,10))