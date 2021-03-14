import sympy as sp
import numpy as np

# aufgabe a
x,y = sp.symbols('x y')
f1 = x**2/186**2 - y**2/(300**2-186**2) - 1
f2 = (y-500)**2/279**2 - (x-300)**2/(500**2-279**2) - 1

# plotting
p1 = sp.plot_implicit(sp.Eq(f1,0),(x,-2000,2000),(y,-2000,2000))
p2 = sp.plot_implicit(sp.Eq(f2,0),(x,-2000,2000),(y,-2000,2000))
p1.append(p2[0])
p1.show()

'''
Folgende 4 Punkte konnten qualitativ aus dem Plot herauslesen werden:
- oben links: x=-1300, y=1600
- unten links: x=-190, y=90
- unten rechts: x=250, y=250
- oben rehcts: x=750, y=900
'''

# aufgabe b

def newton_verfahren(f_func, Df_func, start, tol):
    x = start
    i = 0
    while np.linalg.norm(f_func(x),2) > tol:
        delta = np.linalg.solve(Df_func(x), -f_func(x))
        x = x + delta
        i += 1
        print('i=', i)
        print('x= \n', x)
        print("||f(x)|| = ", np.linalg.norm(f_func(x),2))
    
    return x
        
f = sp.Matrix([f1,f2])
Df = f.jacobian(sp.Matrix([x,y]))

# create numpy functions that expect a 2d column vector as argument
f_func = sp.lambdify([ [[x],[y]] ], f, 'numpy')
Df_func = sp.lambdify([ [[x],[y]] ], Df, 'numpy')        

start1 = np.array([[-1300],[1600]],dtype=np.float)
start2 = np.array([[-200],[100]],dtype=np.float)
start3 = np.array([[250],[250]],dtype=np.float)
start4 = np.array([[750],[900]],dtype=np.float)

tol = 1e-5
result1 = newton_verfahren(f_func, Df_func, start1, tol)
result2 = newton_verfahren(f_func, Df_func, start2, tol)
result3 = newton_verfahren(f_func, Df_func, start3, tol)
result4 = newton_verfahren(f_func, Df_func, start4, tol)

print()
print('Resultat oben links: \n', result1)
print('Resultat unten links: \n', result2)
print('Resultat unten rechts: \n', result3)
print('Resultat oben rechts: \n', result4)