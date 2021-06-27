import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# aufgabe a

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
        # aufgabe b
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

x = np.array([25,35,45,55,65],dtype=float)
y = np.array([47,114,223,81,20],dtype=float)

# erstelle sympy symbole für lambda parameter
l = sp.symbols('l0 l1 l2')

def f(x, l):
    return l[0]/((x**2-l[1]**2)**2+l[2]**2)

g = sp.Matrix([y[k]-f(x[k],l) for k in range(len(x))])
Dg = g.jacobian(l)

g = sp.lambdify([l], g, 'numpy')
Dg = sp.lambdify([l], Dg, 'numpy')

lam0 = np.array([10**8,50,600],dtype=np.float64) # startvektor für lambda
tol = 1e-3 # genauigkeit
max_iter = 50 # maximale anzahl iterationen
pmax = 5 # maximaler dämpfungs potenz
damping = 0 # schaltet dämpfung an oder aus

lam,n = gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping)

print("Lösung für Startwert (10**8,50,600):", lam, "n=", n)

plt.plot(x,y,'ro',label='Punkte')
plt.plot(x,f(x,lam))
plt.grid()
plt.legend()
plt.show()

# aufgabe c
lam0 = np.array([10**7,35,350],dtype=np.float64) # startvektor für lambda
tol = 1e-3 # genauigkeit
max_iter = 50 # maximale anzahl iterationen
pmax = 5 # maximaler dämpfungs potenz

damping = 1 # schaltet dämpfung an oder aus
lam_with_dumping,n_with_dumping = gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping)

damping = 0 # schaltet dämpfung an oder aus
#lam_without_dumping,n_without_dumping = gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping)

print("Lösung für Startwert (10**7,35,350) mit Dämpfung:", lam_with_dumping, "n=", n_with_dumping)
#print("Lösung für Startwert (10**7,35,350) ohne Dämpfung:", lam_without_dumping, "n=", n_without_dumping)

'''
Keine Dämpfung führt bei diesem Startwert nicht zu einem Ergebnis.
'''