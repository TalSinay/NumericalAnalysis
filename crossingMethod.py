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
            print("The method is not suitable")
            return None
    print("Newton-Raphson num of iter", count)
    return x1

def secant_method(f,start_point,end_point,e):
    x2 = (start_point + end_point) / 2
    x1 = end_point
    x0 = start_point
    x = symbols('x')
    f = lambdify(x, f, "math")
    count = 0
    while (abs(x2 - x1) > e):
        tmp = x2
        x2 = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = tmp
        count += 1
        if (count >= 50):
            print("The method is not suitable")
            return None
    print("secant num of iter", count)
    return x2


def main():
    x = var('x')  # the possible variable names must be known beforehand...
    user_input = input("Enter function\n")
    f= sympify(user_input)
    start_point=float(input("Enter start point\n"))
    b=float(input("Enter end point\n"))
    e=0.0001
    x = symbols('x')
    fd = nigzeret(f, x)
    a=(abs(start_point)+abs(b))*10
    choice=int(input("which methon you want to use:\n1->Bisection Method\n2->Newton Raphson\n3->secant method"))
    match choice:
        case 1:
            for i in range(a):
                x1 = start_point + i * 0.1
                x2 = x1 + 0.1
                if(f(x1)*f(x2)<0):
                    print("for f(X)->",Bisection_Method(f,x1,x2,e))
                if fd(x1)*fd(x2)<0:
                    print("for f'(X)->",Bisection_Method(fd, x1, x2, e))
        case 2:
            for i in range(a):
                x1 = start_point + i * 0.1
                x2 = x1 + 0.1
                if (f(x1) * f(x2) < 0):
                        print("for f(X)->", Newton_Raphson(f, x1, x2, e))
                if fd(x1) * fd(x2) < 0:
                    print("for f'(X)->", Newton_Raphson(fd, x1, x2, e))


        case 3:
            for i in range(a):
                x1 = start_point + i * 0.1
                x2 = x1 + 0.1
                if (f(x1) * f(x2) < 0):
                    print("for f(X)->", secant_method(f, x1, x2, e))
                if fd(x1) * fd(x2) < 0:
                    print("for f'(X)->", secant_method(fd, x1, x2, e))






#print(secant_method(f,start_point,b,e))
#print(Newton_Raphson(f,start_point,b,e))
#print(Bisection_Method(f,a,b))