from sympy import *
import math

def nigzeret(f, x):
    my_f1 = diff(f,x)
    return lambdify(x, my_f1)

def main(f,start_point,end_point, eps=0.0001):
    fx = f
    x= symbols('x')
    f=lambdify(x,f)
    fd=nigzeret(fx,x)
    a = int((abs(start_point) + abs(end_point)) * 10)
    choice=int(input("which methon you want to use:\n1->Bisection Method\n2->Newton Raphson\n3->secant method\n"))
    if choice==1:
        for i in range(a):
            x1 = start_point + i * 0.1
            x2 = x1 + 0.1
            if (f(x1) * f(x2)) < 0:
                print(Bisection_Method(f, x1, x2, eps)," is the negative root")
            if (fd(x1) * fd(x2) < 0):
                g = Bisection_Method(f, x1, x2, eps)
                if f(g) ==0:
                    print("A positive root for the func ->", g)
                else:
                    print("the number ",g, " is a extreme point,not a root")
    if choice==2:
        for i in range(a):
            x1 = start_point + i * 0.1
            x2 = x1 + 0.1
            if (f(x1) * f(x2)) < 0:
                print(Newton_Raphson(fx, x1, x2, eps)," is the negative root")
            if (fd(x1) * fd(x2) < 0):
                g = Newton_Raphson(fx, x1, x2, eps)
                if f(g) ==0 :
                    print("A positive root for the func ->", g)
                else:
                    print("the number ",g, " is a extreme point,not a root")
    if choice==3:
        for i in range(a):
            x1 = start_point + i * 0.1
            x2 = x1 + 0.1
            if (f(x1) * f(x2)) < 0:
                print(secant_method(f, x1, x2, eps)," is the negative root")
            if (fd(x1) * fd(x2) < 0):
                g = secant_method(f, x1, x2, eps)
                if f(g) ==0:
                    print("A positive root for the func ->", g)
                else:
                    print("the number ",g, " is a extreme point,not a root")

def Bisection_Method(f,start_point,end_point, eps=0.0001):
    c=(end_point+start_point)/2
    count=1
    k = int(-(math.log(eps / (end_point - start_point)) / math.log(2)))
    while (abs(start_point - c) > eps):
        if f(c) == 0:
            return c
        if f(start_point) * f(c) < 0:
            c, end_point = (start_point + c) / 2, c
        else:
            c, start_point = (end_point + c) / 2, c
        count += 1
        if count > k + 1:
            print("cant use crossing method")
            return
    print("Bisection Method iter number ->", count)
    if abs(f(c))<eps:
        return 0
    return c

def Newton_Raphson(f,start_point,end_point,e):
    x0 = (end_point + start_point) / 2
    x = symbols('x')
    fx = f
    f = lambdify(x, f)
    x1 = start_point
    fd=nigzeret(fx,x)
    count = 1
    while (abs(x1 - x0) > e):
        x0=x1
        if fd(x0) == 0:
            print("cant divided by zero")
            return
        x1 = x0 - (f(x0) / fd(x0))
        count += 1
        if (count >= 50):
            print("The method is not suitable")
            return None
    print("Newton-Raphson num of iter", count)
    if abs(f(x1))<e:
        return 0
    return x1

def secant_method(f,start_point,end_point,e):
    x2 = (start_point + end_point) / 2
    x1 = end_point
    x0 = start_point
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
    if abs(f(x2))<e:
        return 0
    return x2

x = var('x')  # the possible variable names must be known beforehand...
user_input = input("Enter function\n")
f= sympify(user_input)
start_point=int(input("Enter start point\n"))
end_point=int(input("Enter end point\n"))
main(f,start_point,end_point)