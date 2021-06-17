import sympy as sp
import numpy as np

x0 = np.array([1.,2.])

''' Jacobi Matrix berechnen für Funktion R^2->R^2 '''

# sympy symbole für die funktionsparameter
x1, x2 = sp.symbols('x1 x2')

# funktionen definieren um y1... werte zu berechnen
f1 = 5*x1*x2
f2 = x1**2*x2**2+x1+x2

f = sp.Matrix([f1,f2]) # funktionen als sympy matrix zusammenführen
x_symbols = sp.Matrix([x1,x2]) # x-parameter als matrix zusammenführen

# jacobi matrix berechnen
Df = f.jacobian(x_symbols)

print('Jacobi Matrix: \n', Df)
print()

# jacobi matrix mit dem wert 1 für x_1 und den wert 2 für x_2 substituieren
Df_subs = Df.subs([(x1,x0[0]),(x2,x0[1])])

print('Jacobi Matrix an der Stelle (1,2): \n', Df_subs.evalf())
print()

''' 
Linearisierung von Funktionen mit mehreren Variablen and der Stelle x_0 (1,2):
g(x) = f(x_0)+Df(x_0)(x-x_0)
'''

# ursprungsfunktion mit dem wert 1 für x_1 und den wert 2 für x_2 substituieren
f_subs = f.subs([(x1,x0[0]),(x2,x0[1])])

# erstelle symbolisch die subtraktion von x - x_0
xminusx0 = sp.Matrix([x1-x0[0],x2-x0[1]])

# realisiere linearisierungsfunktion an der stelle (1,2)
lin = f_subs.evalf() + (Df_subs.evalf() * xminusx0)

print('Linearisierung der Funktion an der Stelle (1,2): \n', lin)