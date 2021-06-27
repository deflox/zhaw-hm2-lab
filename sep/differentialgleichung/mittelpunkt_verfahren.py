import numpy as np

def euler_mid(f,a,b,n,y0):
    
    x = np.zeros(n+1)
    x[0] = a
    y = np.zeros(n+1)
    y[0] = y0
    h = (b-a)/n
    
    for i in range(n):
        x_half = x[i] + h/2.
        y_half = y[i] + h/2.*f(x[i], y[i])
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*f(x_half,y_half)
        
    return x,y

def f(x,y):
    return x**2/y

a = 0
b = 1.4
y0 = 2
n = 5

h = 0.7
n = int((b-a)/h)

x,y = euler_mid(f, a, b, n, y0)

print("x-werte mittelpunkt verfahren:", x)
print("y-werte mittelpunkt verfahren:", y)