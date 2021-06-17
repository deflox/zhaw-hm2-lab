import numpy as np
import sympy as sp

def vereinfachtes_newton_verfahren(f_func, Df_x0, start, tol):
    x = start
    i = 0
    
    while np.linalg.norm(f_func(x),2) > tol: # abbruchkriterium
        
        # neues x ausrechnen
        delta = np.linalg.solve(Df_x0, -f_func(x))
        x = x + delta
        i += 1
        
        print('i=', i)
        print('x= \n', x)
        print("||f(x)|| = ", np.linalg.norm(f_func(x),2))
        print()
    
    return x

# erstelle vektorielle funktion
x1, x2 = sp.symbols('x1 x2')
f1 = 2*x1+4*x2
f2 = 4*x1+8*x2**3

# erstelle jacobi matrix
f = sp.Matrix([f1,f2])
x_symbols = sp.Matrix([x1,x2])
Df = f.jacobian(x_symbols)

# erstelle numpy funktionen die als parameter 2 dimensionalen numpy array
# entgegen nehmen
f_func = sp.lambdify([ [[x1],[x2]] ], f, 'numpy')
Df_func = sp.lambdify([ [[x1],[x2]] ], Df, 'numpy')

# parameter für das newton-verfahren
tol = 1e-5
start = np.array([[4.,2.]]).T
Df_x0 = Df_func(start)

result = vereinfachtes_newton_verfahren(f_func, Df_x0, start, tol)

print()
print('Resultat: \n', result)