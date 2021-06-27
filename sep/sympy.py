import sympy as sp
import math

x = sp.Symbol('x')
f = x**2+ math.e **(-x)
print("function=", f)
print("integral=", sp.integrate(f, x))
print("derivate=", sp.diff(f, x, 1))

print()
x = sp.Symbol('x')
f = x**2* math.e **(-x)
print("function=", f)
print("integral=", sp.integrate(f, x))
print("derivate=", sp.diff(f, x, 1))

print()
x = sp.Symbol('x')
f = 1/2*2**x
print("function=", f)
print("integral=", sp.integrate(f, x))
print("derivate=", sp.diff(f, x, 1))

print()
x = sp.Symbol('x')
f = 1/(sp.cos(x+(sp.pi/4))-1) + 2
print("function=", f)
print("derivate=", sp.diff(f, x, 1))