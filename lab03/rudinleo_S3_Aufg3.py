import numpy as np
import sympy as sp

def gedaempftes_newton_verfahren(f_func, Df_func, start, tol, kmax):
    x = start
    i = 0
    while np.linalg.norm(f_func(x),2) > tol:
        delta = np.linalg.solve(Df_func(x), -f_func(x))
        
        # daempfung von delta
        k = 0
        while (k <= kmax and np.linalg.norm(f_func((x+delta/2.**k)),2) >= np.linalg.norm(f_func(x),2)):
            k += 1
        if k == kmax+1:
            k = 0
        
        x = x + delta/2.**k
        i += 1
        print('i=', i)
        print('x= \n', x)
        print("||f(x)|| = ", np.linalg.norm(f_func(x),2))
    
    return x

x1,x2,x3 = sp.symbols('x1 x2 x3')
f1 = x1+x2**2-x3**2-13
f2 = sp.log(x2/4.) + sp.exp(0.5*x3-1) - 1
f3 = (x2-3)**2 - x3**3 + 7

f = sp.Matrix([f1,f2,f3])
Df = f.jacobian(sp.Matrix([x1,x2,x3]))

f_func = sp.lambdify([ [[x1],[x2],[x3]] ], f, 'numpy')
Df_func = sp.lambdify([ [[x1],[x2],[x3]] ], Df, 'numpy')

kmax = 4
tol = 1e-5
start = np.array([[1.5,3.0,2.5]]).T

result = gedaempftes_newton_verfahren(f_func, Df_func, start, tol, kmax)

print('Resultat: \n', result)