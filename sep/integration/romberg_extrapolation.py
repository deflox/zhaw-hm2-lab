import numpy as np

def romberg_extrapolation(f, a, b, m):
    res = np.ones((m+1,m+1))
    
    for j in range(0,m+1):
        h = (b-a)/2**j
        res[j][0] = h*((f(a)+f(b))/2);
        for i in range(1,2**j):
            res[j][0] += h*f(a+i*h)
            
    for j in range(1,m+1):
        res[0:m+1-j,j] = (4**j*res[:,j-1][1:m+2-j]-res[:,j-1][0:m+1-j])/(4.**j-1)
    
    print(res)
    print()
    
    return res[0][m]

# funktion die integriert werden soll
def f(x):
    return np.cos(x**2)

# integration von bis
a = 0
b = np.pi

# stufen der extrapolation
m = 4

I = romberg_extrapolation(f,a,b,m)

print('Integralwert:', I)