import numpy as np

def rudinleo_S11_Aufg3(f,a,b,n,y0):
    x,h = np.linspace(a,b,n+1,retstep=True,endpoint=True)
    
    y_euler = np.zeros(np.shape(x)[0]-1)
    y_mittelpunkt = np.zeros(np.shape(x)[0]-1)
    y_modeuler = np.zeros(np.shape(x)[0]-1)
    
    i = 0
    for xi in x[:-1]:
        # Euler-Verfahren
        y_old = y0 if i == 0 else y_euler[i-1]
        y_euler[i] = y_old + h * f(xi,y_old)

        # Mittelpunkt-Verfahren
        y_old = y0 if i == 0 else y_mittelpunkt[i-1]
        x_half = xi + h/2
        y_half = y_old + h/2 * f(xi,y_old)
        y_mittelpunkt[i] = y_old + h * f(x_half,y_half)

        # Modifiziertes Euler-Verfahren
        y_old = y0 if i == 0 else y_modeuler[i-1]
        y_eul = y_old + h * f(xi,y_old)
        k1 = f(xi,y_old)
        k2 = f(x[i+1],y_eul)
        y_modeuler[i] = y_old + h * (k1+k2)/2
        
        i+=1
    
    return x[1:],y_euler,y_mittelpunkt,y_modeuler

def f(x,y):
    return x**2/y
    
a = 0
b = 1.4
n = 3
y0 = 2.

x,y_euler,y_mittelpunkt,y_modeuler = rudinleo_S11_Aufg3(f, a, b, n, y0)

print('x: \n', x)
print('y_euler: \n', y_euler)
print('y_mittelpunkt: \n', y_mittelpunkt)
print('y_modeuler: \n', y_modeuler)