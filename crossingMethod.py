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



def NewtonRaphson(f,fd,start_point,end_point,e):
    x1=start_point
    for i in range(100):
        d=f(x1)
        x2=x1-f(x1)/fd(x1)
        if abs(x2 - x1) < e:
          print("Newton-Raphson num of iter", i)
          return float(x2)
        x1=x2
    return None


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


def main(f, start_point, end_point, eps=0.0001):
    roots = []
    fx = f
    x = symbols('x')
    f = lambdify(x, f)
    fd = nigzeret(fx, x)
    fd2 = nigzeret(fx.diff(x), x)
    a = int((abs(start_point) + abs(end_point)) * 10)
    choice = int(input("which methon you want to use:\n1->Bisection Method\n2->Newton Raphson\n3->secant method\n"))
    if choice == 1:
        while start_point < end_point:
            # x1 = start_point + i * 0.5
            # x2 = x1 + 0.5
            x1 = start_point
            x2 = x1 + 0.1
            if (f(x1) * f(x2)) < 0:
                t, iters = bisectionMethod(f, x1, x2, 30)
                if (t == None):
                    break
                roots.append(t)
                print("Bisection Method iter number ->", iters)
                print(t, " is a root")
            elif (fd(x1) * fd(x2) < 0):
                g, iters = bisectionMethod(fd, x1, x2, 30)
                if abs(f(g)) < eps:
                    roots.append(g)
                    print("A positive root for the func ->", 0)
                else:
                    print("the number ", g, " is a extreme point,not a root")
            start_point = start_point + 0.1
    if choice == 2:
        x1 = start_point
        if (f(end_point) == 0):
            print("Newton-Raphson num of iter 1")
            print(end_point, " is a root")
        while x1 < end_point:
            if (f(x1) == 0):
                print("Newton-Raphson num of iter 1")
                print(x1, " is a root")
                roots.append(x1)
                x1 = x1 + 0.1
                continue
            if (f(x1) * f(x1 + 0.1) < 0):
                t = NewtonRaphson(f, fd, x1 + 0.05, x + 0.1, eps)
                if (t == None):
                    break
                print("the roots of the function-> ", t)
                roots.append(t)
                x1 = x1 + 0.1
                continue
            if fd(x1) * fd(x1 + 0.1) < 0:
                posrott = NewtonRaphson(fd, fd2, x1 + 0.05, x + 0.1, eps)
                if abs(f(posrott)) < eps:
                    print("the roots of the function-> ", posrott)
                    roots.append(posrott)
                print("the number ", posrott, " is a extreme point,not a root")
            x1 = x1 + 0.1

    if choice == 3:
        for i in range(a):
            x1 = start_point + i * 0.1
            x2 = x1 + 0.1
            if (f(x1) * f(x2)) < 0:
                t = secant_method(f, x1, x2, eps)
                if (t == None):
                    continue
                elif (abs(t - 0) <= eps):
                    continue
                roots.append(t)
                print(t, " is a root")
            elif (fd(x1) * fd(x2) < 0):
                g = secant_method(f, x1, x2, eps)
                print(g, "g")
                print("fg", f(g))
                if abs(f(g)) == 0:
                    print("A positive root for the func ->", 0)
                    roots.append(0)
                else:
                    print("the number ", g, " is a extreme point,not a root")
    w = set(roots)
    print("the roots of the function-> ", w)


e=float(math.e)
x = var('x')  # the possible variable names must be known beforehand...
#f=simplify(sin(2*e**(-2*x))/(x**2+5*x+6))
f=simplify(sin(e**(-2*x)+e**(-2*x))/(2*(x**3)+5*(x**2)-6))
# f= sympify(user_input)
# start_point=int(input("Enter start point\n"))
start_point=-1.1
end_point=2
# end_point=int(input("Enter end point\n"))
main(f,start_point,end_point)
main(f,start_point,end_point)