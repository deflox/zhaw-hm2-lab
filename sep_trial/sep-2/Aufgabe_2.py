import sympy as sp
import numpy as np

# aufgabe b

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
a = 2
b = 4
x, y = sp.symbols('x y')
f1 = 1-x**2-y**2
f2 = ((x-2)**2)/a+((y-1)**2)/b-1

# erstelle jacobi matrix
f = sp.Matrix([f1,f2])
symbols = sp.Matrix([x,y])
Df = f.jacobian(symbols)

# erstelle numpy funktionen die als parameter 2 dimensionalen numpy array
# entgegen nehmen
f_func = sp.lambdify([ [[x],[y]] ], f, 'numpy')
Df_func = sp.lambdify([ [[x],[y]] ], Df, 'numpy')

# parameter für das newton-verfahren
tol = 1e-8
start = np.array([[2,-1]]).T

result = newton_verfahren(f_func, Df_func, start, tol)

print('Resultat: \n', result)

# aufgabe c
p1 = sp.plot_implicit(sp.Eq(f1,0),(x,-2,2),(y,-2,2))
p2 = sp.plot_implicit(sp.Eq(f2,0),(x,-2,2),(y,-2,2))
p1.append(p2[0])
p1.show()