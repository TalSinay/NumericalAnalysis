from sympy import *
import math

def bisectionMethod(f, start_point, end_point, iterationAllowed,eps=0.0001):
    for i in range(iterationAllowed):
        middle = start_point + (end_point - start_point) / 2
        if abs(f(middle)) < eps:
            return int(middle * 10 ** 5) / 10 ** 5, i + 1
        elif f(start_point) * f(middle) < 0:
            end_point = middle
        elif f(middle) * f(end_point) < 0:
            start_point = middle
    return None,None
def nigzeret(f, x):
    my_f1 = diff(f,x)
    return lambdify(x, my_f1)

def main(f,start_point,end_point, eps=0.0001):
    roots=[]
    fx = f
    x= symbols('x')
    f=lambdify(x,f)
    fd=nigzeret(fx,x)
    a = int((abs(start_point) + abs(end_point)) * 10)
    choice=int(input("which methon you want to use:\n1->Bisection Method\n2->Newton Raphson\n3->secant method\n"))
    if choice==1:
        while start_point < end_point:
            #x1 = start_point + i * 0.5
            #x2 = x1 + 0.5
            x1 = start_point
            x2 = x1 +0.1
            if (f(x1) * f(x2)) < 0:
                t,iters=bisectionMethod(f,x1,x2,30)
                if (t==None):
                    break
                roots.append(t)
                print("Bisection Method iter number ->", iters)
                print(t," is a root")
            elif (fd(x1) * fd(x2) < 0):
                g,iters =bisectionMethod(fd, x1, x2, 30)
                if abs(f(g))<eps:
                    roots.append(g)
                    print("A positive root for the func ->", 0)
                else:
                    print("the number ",g, " is a extreme point,not a root")
            start_point=start_point+0.1
    if choice==2:
        for i in range(a):
            x1 = start_point + i * 0.1
            x2 = x1 + 0.1
            if (f(x1) * f(x2)) < 0:
                t=Newton_Raphson(fx, x1, x2, eps)
                roots.append(t)
                print(t," is a root")
            elif (fd(x1) * fd(x2) < 0):
                g = Newton_Raphson(fx, x1, x2, eps)
                if abs(f(g))<0.00001 :
                    roots.append(0)
                    print("A positive root for the func ->", 0)
                else:
                    print("the number ",g, " is a extreme point,not a root")
    if choice==3:
        for i in range(a):
            x1 = start_point + i * 0.1
            x2 = x1 + 0.1
            if (f(x1) * f(x2)) < 0:
                t=secant_method(f, x1, x2, eps)
                if (t==None):
                    continue
                elif(abs(t-0)<=eps):
                    continue
                roots.append(t)
                print(t," is a root")
            elif (fd(x1) * fd(x2) < 0):
                g = secant_method(f, x1, x2, eps)
                print(g,"g")
                print("fg",f(g))
                if abs(f(g))==0:
                   print("A positive root for the func ->", 0)
                   roots.append(0)
                else:
                    print("the number ",g, " is a extreme point,not a root")
    w=set(roots)
    print("the roots of the function-> ",w)


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
    return x2
e=float(math.e)
x = var('x')  # the possible variable names must be known beforehand...
f=simplify(sin(2*e**(-2*x))/(x**2+5*x+6))

# f= sympify(user_input)
# start_point=int(input("Enter start point\n"))
start_point=-1
end_point=2
# end_point=int(input("Enter end point\n"))
main(f,start_point,end_point)
main(f,start_point,end_point)