import numpy as np

def rudinleo_S9_Aufg3(f, a, b, m):
    res = np.ones((m+1,m+1))
    
    for j in range(0,m+1):
        h = (b-a)/2**j
        res[j][0] = h*((f(a)+f(b))/2);
        for i in range(1,2**j):
            res[j][0] += h*f(a+i*h)
            
    for j in range(1,m+1):
        res[0:m+1-j,j] = (4**j*res[:,j-1][1:m+2-j]-res[:,j-1][0:m+1-j])/(4.**j-1)
    
    return res[0][m]

def f(x):
    return np.cos(x**2)

a = 0
b = np.pi
m = 4

T = rudinleo_S9_Aufg3(f,a,b,m)

print('Integralwert: ', T)