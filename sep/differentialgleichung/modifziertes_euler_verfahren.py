import numpy as np

def euler_mod(f,a,b,n,y0):
    
    x = np.zeros(n+1)
    x[0] = a
    y = np.zeros(n+1)
    y[0] = y0
    h = (b-a)/n
    
    for i in range(n):
        x[i+1] = x[i] + h
        k1 = f(x[i], y[i])
        k2 = f(x[i+1], y[i] + h*k1)
        y[i+1] = y[i] + h*((k1 + k2)/2)
        
    return x,y

def f(x,y):
    return x**2/y

a = 0
b = 1.4
y0 = 2
n = 5

h = 0.7
n = int((b-a)/h)

x,y = euler_mod(f, a, b, n, y0)

print("x-werte modifiziertes euler-verfahren:", x)
print("y-werte modifiziertes euler-verfahren:", y)