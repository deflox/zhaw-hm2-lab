import sympy as sp

x01 = 1
x02 = 2
x03 = 3

# aufgabe a
x1, x2 = sp.symbols('x1 x2')
f1 = 5*x1*x2
f2 = x1**2*x2**2+x1+x2

F = sp.Matrix([f1,f2])
X = sp.Matrix([x1,x2])
M = F.jacobian(X)
print('Jacobi Matrix a) \n', M)

F0 = F.subs([(x1,x01),(x2,x02)])
M0 = M.subs([(x1,x01),(x2,x02)])
x0minusx = sp.Matrix([x1-x01,x2-x02])
print('Linearisierung für a): \n', F0.evalf() + (M0.evalf() * x0minusx))
print()

# aufgabe b
x1, x2, x3 = sp.symbols('x1 x2 x3')
f1 = sp.log(x1**2+x2**2)+x3**2
f2 = sp.exp(x2**2+x3**2)+x1**2
f3 = (1)/(x3**2+x1**2)+x2**2

F = sp.Matrix([f1,f2,f3])
X = sp.Matrix([x1,x2,x3])
M = F.jacobian(X)
print('Jacobi Matrix b) \n', M)

F0 = F.subs([(x1,x01),(x2,x02),(x3,x03)])
M0 = M.subs([(x1,x01),(x2,x02),(x3,x03)])
x0minusx = sp.Matrix([x1-x01,x2-x02,x3-x03])
print('Linearisierung für b): \n', F0.evalf() + (M0.evalf() * x0minusx))