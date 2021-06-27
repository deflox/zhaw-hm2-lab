import numpy as np
import sympy as sp

def gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping):
    k=0
    lam=np.copy(lam0)
    increment = tol+1
    err_func = np.linalg.norm(g(lam))**2
    
    while increment >= tol and max_iter >= k:
        # QR-Zerlegung von Dg(lam)
        [Q,R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R,-Q.T @ g(lam)).flatten() # Achtung: flatten() braucht es, um aus dem Spaltenvektor delta wieder
                                                           # eine "flachen" Vektor zu machen, da g hier nicht mit Spaltenvektoren als Input umgehen kann           
        # hier kommt die Däfmpfung, falls damping = 1
        p=0
        while damping == 1 and p <= pmax and np.linalg.norm(g(lam+(delta/2**p)))**2 >= err_func:
            p = p+1
            
        if p == pmax:
            p = 0
               
        # Update des Vektors Lambda
        lam = lam+(delta/2**p)
        err_func = np.linalg.norm(g(lam))**2
        increment = np.linalg.norm(delta)
        k = k+1
        
        #print('Iteration: ',k)
        #print('lambda = ',lam)
        #print('Inkrement = ',increment)
        #print('Fehlerfunktional =', err_func)
        
    return(lam,k)

def gauss_newton(g, Dg, lam0, tol, max_iter):
    k=0
    lam=np.copy(lam0)
    increment = tol+1
    err_func = np.linalg.norm(g(lam))**2
    
    while increment >= tol and max_iter >= k: # Hier kommt Ihre Abbruchbedingung, die tol und max_iter berücksichtigen muss# 

        # QR-Zerlegung von Dg(lam) und delta als Lösung des lin. Gleichungssystems
        [Q,R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R,-Q.T @ g(lam)).flatten() # Achtung: flatten() braucht es, um aus dem Spaltenvektor delta wieder
                                                           # eine "flachen" Vektor zu machen, da g hier nicht mit Spaltenvektoren als Input umgehen kann           
            
        # update des vektors lambda
        lam = lam+delta
        err_func = np.linalg.norm(g(lam))**2
        increment = np.linalg.norm(delta)
        k = k+1
        
        #print('Iteration: ',k)
        #print('lambda = ',lam)
        #print('Inkrement = ',increment)
        #print('Fehlerfunktional =', err_func)
        
    return(lam,k)

# stützstellen die approximiert werden soll durch eine nichtlineare ansatzfunktion
x=np.array([2.,2.5,3.,3.5,4.,4.5,5.,5.5,6.,6.5,7.,7.5,8.,8.5,9.,9.5])
y=np.array([159.57209984, 159.8851819 , 159.89378952, 160.30305273,
            160.84630757, 160.94703969, 161.56961845, 162.31468058,
            162.32140561, 162.88880047, 163.53234609, 163.85817086,
            163.55339958, 163.86393263, 163.90535931, 163.44385491])

# erstelle sympy symbole für lambda parameter
l = sp.symbols('l0 l1 l2 l3')

# erstelle ansatzfunktion für x parameter und alle lambda parameter
def f(x, l):
    return (l[0]+l[1]*10**(l[2]+l[3]*x))/(1+10**(l[2]+l[3]*x))

# erstelle g(lambda) funktion, was der fehlerfunktion entspricht
g = sp.Matrix([y[k]-f(x[k],l) for k in range(len(x))])

# erstelle jacobi-matrix von g(lambda) um dann die linearisierung im
# newton-verfahren durchzführen
# partielle ableitung von allen zeilen für alle lambda parameter
Dg = g.jacobian(l)

# umwandeln zu numpy funktionen um als funktionsparameter zu übergeben
g = sp.lambdify([l], g, 'numpy')
Dg = sp.lambdify([l], Dg, 'numpy')

# parameter für funktion
lam0 = np.array([100,120,3,-1],dtype=np.float64) # startvektor für lambda
tol = 1e-5 # genauigkeit
max_iter = 30 # maximale anzahl iterationen
pmax = 5 # maximaler dämpfungs potenz
damping = 1 # schaltet dämpfung an oder aus

# lambda parameter und anzahl iterationen
lam_with,n = gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping)

print("Lösung für Startwert", lam0, ":", lam_with, "n=", n)

import matplotlib.pyplot as plt
plt.plot(x,y,'ro',label='Punkte')
plt.plot(x,f(x,lam_with))
plt.grid()
plt.legend()
plt.show()