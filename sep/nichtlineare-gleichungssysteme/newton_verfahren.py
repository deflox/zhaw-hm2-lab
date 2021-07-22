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
x, y = sp.symbols('x y')
f1 = (x**2+1)*(x+y)**2-25*x**2
f2 = (y**2+1)*(x+y)**2-16*y**2

# erstelle jacobi matrix
f = sp.Matrix([f1,f2])
symbols = sp.Matrix([x,y])
Df = f.jacobian(symbols)

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