import numpy as np
import sympy as sp

def newton_verfahren(f_func, Df_func, start, tol):
    x = start
    i = 0
    
    while np.linalg.norm(f_func(x),2) > tol: # abbruchkriterium
        
        # neues x ausrechnen
        delta = np.linalg.solve(Df_func(x), -f_func(x))
        x = x + delta
        i += 1
        
        print('i=', i)
        print('x= \n', x)
        print("||f(x)|| = ", np.linalg.norm(f_func(x),2))
        print()
    
    return x

# erstelle vektorielle funktion
x1, x2 = sp.symbols('x1 x2')
f1 = 5*x1**2-x2**2
f2 = x2-0.25*(sp.sin(x1)+sp.cos(x2))

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
start = np.array([[0.25,0.25]]).T

result = newton_verfahren(f_func, Df_func, start, tol)

print()
print('Resultat: \n', result)