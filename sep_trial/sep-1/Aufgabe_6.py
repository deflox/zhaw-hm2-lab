import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# aufgabe a

# N(0) = G/(2*(G-N_0))/N_0
# lim_t->inf N(t) = 0

# aufgabe b

ti = np.array([0,14,28,42,56],dtype=float)
Ni = np.array([29,2072,15798,25854,28997],dtype=float)

plt.plot(ti,Ni,'ro',label="Datenpunkte")

'''
G muss sehr gross sein, da t im Exponent steht und daher den Bruch stark
verkleinert umso grösser t ist

N sollte auch relativ gross sein um als Faktor dem Exponent t entgegenzuwirken
aber auch nicht zu gross, sonst wird das Resultat das Bruches negativ also
auf jeden Fall kleiner als G

'''

# aufgabe c

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
        print('Iteration: ',k)
        print('lambda = ',lam)
        print('Inkrement = ',increment)
        print('Fehlerfunktional =', err_func)
    return(lam,k)

# erstelle sympy symbole für lambda parameter
l = sp.symbols('l0 l1 l2')

# erstelle ansatzfunktion für x parameter und alle lambda parameter
def f(x, l):
    return l[0]/(((l[0]-l[1])/l[1])*sp.exp(-l[2]*x)+1)

# erstelle g(lambda) funktion, was der fehlerfunktion entspricht
g = sp.Matrix([Ni[k]-f(ti[k],l) for k in range(len(ti))])

# erstelle jacobi-matrix von g(lambda) um dann die linearisierung im
# newton-verfahren durchzführen
# partielle ableitung von allen zeilen für alle lambda parameter
Dg = g.jacobian(l)

# umwandeln zu numpy funktionen um als funktionsparameter zu übergeben
g = sp.lambdify([l], g, 'numpy')
Dg = sp.lambdify([l], Dg, 'numpy')

# parameter für funktion
lam0 = np.array([30000,200,0.5],dtype=np.float64) # startvektor für lambda
tol = 1e-5 # genauigkeit
max_iter = 500 # maximale anzahl iterationen
pmax = 10 # maximaler dämpfungs potenz
damping = 1 # schaltet dämpfung an oder aus

# lambda parameter und anzahl iterationen
[lam_with,n] = gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping)

def f_final(x, l):
    return l[0]/(((l[0]-l[1])/l[1])*np.exp(-l[2]*x)+1)

ti_values = np.arange(-5,70,1)
plt.plot(ti_values, f_final(ti_values,lam_with),label="Approximierte Funktion")
plt.legend()
plt.grid()
plt.show()