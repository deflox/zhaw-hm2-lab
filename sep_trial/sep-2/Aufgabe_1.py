import numpy as np
import sympy as sp

# aufgabe a

'''
ausgelesene Punkte: (1.3,100) (1.6,250) (1.9,600)

Gleichungssystem:
100 = a+b*e^(c*1.3)
250 = a+b*e^(c*1.6)
600 = a+b*e^(c*1.9)

Umstellen nach 0:
0 = a+b*e^(c*1.3) - 100
0 = a+b*e^(c*1.6) - 250
0 = a+b*e^(c*1.9) - 600

'''

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

m1=np.array([1.3,100],dtype=float)
m2=np.array([1.6,250],dtype=float)
m3=np.array([1.9,600],dtype=float)

a, b, c = sp.symbols('a b c')
f1=a+b*sp.exp(c*m1[0])-m1[1]
f2=a+b*sp.exp(c*m2[0])-m2[1]
f3=a+b*sp.exp(c*m3[0])-m3[1]

# erstelle jacobi matrix
f = sp.Matrix([f1,f2,f3])
symbols = sp.Matrix([a,b,c])
Df = f.jacobian(symbols)

# erstelle numpy funktionen die als parameter 2 dimensionalen numpy array
# entgegen nehmen
f_func = sp.lambdify([ [[a],[b],[c]] ], f, 'numpy')
Df_func = sp.lambdify([ [[a],[b],[c]] ], Df, 'numpy')

# parameter für das newton-verfahren
tol = 1e-5
start = np.array([[1,2,3]]).T

result = newton_verfahren(f_func, Df_func, start, tol)

print()
print('Resultat: \n', result)

# aufgabe b

'''
Gleichugssystem:
0 = a+b*e^(c*t)-y
differentiation:
b*c*e^(c*t)
'''

def newton_verfahren(f,dF,x0,tol):
    c = 0
    xn = x0
    xn_1 = xn - (f(xn))/(dF(xn))
    while np.abs(xn_1-xn) > tol:
        c += 1
        #print('xn_'+str(c)+':', xn_1)
        xn = xn_1
        xn_1 = xn - (f(xn))/(dF(xn))
    
    return xn_1

def f(t):
    return result[0]+result[1]*np.exp(result[2]*t)-1600

def df(t):
    return result[1]*result[2]*np.exp(result[2]*t)

x0 = 2.1
tol = 1e-4

ti = newton_verfahren(f,df,x0,tol)

print("Näherung von ti:", ti)