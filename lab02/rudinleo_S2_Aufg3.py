import sympy as sp

x1, x2, x3 = sp.symbols('x1 x2 x3')
f1 = x1+x2**2-x3**2-13
f2 = sp.log(x2/4)+sp.exp(0.5*x3-1)-1
f3 = (x2-3)**2-x3**3+7

F = sp.Matrix([f1,f2,f3])
X = sp.Matrix([x1,x2,x3])
M = F.jacobian(X)

x01 = 1.5
x02 = 3.0
x03 = 2.5

F0 = F.subs([(x1,x01),(x2,x02),(x3,x03)])
M0 = M.subs([(x1,x01),(x2,x02),(x3,x03)])
x0minusx = sp.Matrix([x1 - x01,x2 - x02,x3 - x03])

print(F0.evalf() + (M0.evalf() * x0minusx))