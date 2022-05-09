from sympy import *
import math

def nigzeret(f, x):
    my_f1 = diff(f,x)
    return lambdify(x, my_f1)

def Bisection_Method(f,start_point,end_point, eps=0.0001):
    c=(end_point+start_point)/2
    x= symbols('x')
    f=lambdify(x,f)
    count=1
    k = int(-(math.log(e / (b - start_point))) / math.log(2))
    while (abs(start_point-c)>eps or count>k):
        print("iter number ",count," ",start_point,"is the start ",c,"is the middle ",end_point,"is the end ")
        if f(c)==0:
            print("this is the number")
            return c
        if f(start_point)*f(c)<0:
            c,end_point=(start_point+c)/2,c

        else:
            c, start_point = (end_point + c) / 2, c
        count += 1
    if count>k:
        print("cant use crossing method")
        return
    return c


def Newton_Raphson(f,start_point,end_point,e):
    x0 = (end_point + start_point) / 2
    fx = f
    x1 = start_point
    x = symbols('x')
    f = lambdify(x, f)
    fd = nigzeret(fx, x)
    count = 1
    while (abs(x1 - x0) > e):
        x0=x1
        print("f(d)",fd(x0)," f(x) ",f(x0),"  x= ",x0)
        if fd(x0) == 0:
            print("cant divided by zero")
            return
        x1 = x0 - (f(x0) / fd(x0))
        count += 1
        if (count >= 50):
            return None
    print("Newton-Raphson num of iter", count)
    return x1


x = var('x')  # the possible variable names must be known beforehand...
user_input ="x**3-x-1"
f= sympify(user_input)
start_point=float(input("Enter start point\n"))
b=float(input("Enter end point\n"))

e=0.0001

print(Newton_Raphson(f,start_point,b,e))
#print(Bisection_Method(f,a,b))