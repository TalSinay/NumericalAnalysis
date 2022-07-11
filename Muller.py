import cmath
import math


def muller(f, x2, x1, xn, eps):
	i = 0
	print("n\txn\t\tf(xn)")
	print("1\t" + str(x2) + "\t\t" + str(f(x2)))
	print("2\t" + str(x1) + "\t\t" + str(f(x1)))
	print("3\t" + str(xn) + "\t\t" + str(f(xn)))
	# stop iteration if Y is smaller the epsilon
	while (abs(f(xn)) > epsilon):
		q = (xn - x1) / (x1 - x2)
		a = q * f(xn) - q * (1 + q) * f(x1) + q ** 2 * f(x2)
		b = (2 * q + 1) * f(xn) - (1 + q) ** 2 * f(x1) + q ** 2 * f(x2)
		c = (1 + q) * f(xn)
		# see which x intercept is better by using a quadratic equation
		r = xn - (xn - x1) * ((2 * c) / (b + cmath.sqrt(b ** 2 - 4 * a * c)))
		s = xn - (xn - x1) * ((2 * c) / (b - cmath.sqrt(b ** 2 - 4 * a * c)))
		if (abs(f(r)) < abs(f(s))):
			xplus = r
		else:
			xplus = s
		if xplus.imag == 0j:  # result is real number
			xplus = xplus.real
			aa = f(xplus)
			print(str(i + 4) + "\t" + str(round(xplus, 5)) + "\t\t" + str(round(aa, 5)))
		else:
			print(str(i + 4) + "\t{:.4f}".format(xplus) + "\t{:.4f}".format(f(xplus)))
		# run the muller method with the next values
		x2 = x1
		x1 = xn
		xn = xplus
		i = i + 1
	print(str(i) + " iterations")
	# when root is complex double check complex conjugate
	if isinstance(xplus, complex):
		conjugate = complex(xplus.real, -xplus.imag)
		if abs(f(conjugate)) < epsilon:
			print("and \t{:.4f}".format(conjugate) + "\t{:.4f}".format(f(conjugate)))
			return conjugate
	if xplus<x2 and xplus>xn:
		return 0
	return xplus


def f(x):
	return x**2-2


def f2(x):
	return x**2+16


def f3(x):
	return x**5-4*x**3+x**2+3


def f4(x):
	coso=math.cos
	sqrtt=math.sqrt
	if isinstance(x, complex):
		coso = cmath.cos
		sqrtt = cmath.sqrt
	return coso(x)-sqrtt(x+2)+x**2.5


epsilon = 10**-5
a = 1  # the smallest value in the range
b = 2  # the greater value in the range
c = 1.5  # the middle value in the range

print("Using Muller method for function : x**2-2")
muller(f, a, b, c, epsilon)
print("Using Muller method for function : x**2+16")
muller(f2, a, b, c, epsilon)
print("Using Muller method for function : x**5-4*x**3+x**2+3")
muller(f3, a, b, c, epsilon)
print("Using Muller method for function : cos(x)-sqrt(x+2)+x**2.5")
muller(f4, a, b, c, epsilon)
print("Using Muller method for function : x**2-2")
muller(f, -3, -5, -1.5, epsilon)


a = -5
b = -1.5
c = 3

complexarr = set()
floatarr = set()

#Divide into smaller ranges of 0.5

while(abs(a-c)>epsilon):
	tt=muller(f, a, a+0.25, a+0.5, epsilon)
	if isinstance(tt, complex):
		complexarr.add(tt)
	elif isinstance(tt, float):
		floatarr.add("%.3f" % tt)
	a += 0.5
print("Complex roots : "+str(complexarr))
print("normal roots : "+str(floatarr))
