import numpy as np

def lagrange(n,i,x_int,x):
    result = 1
    for j in range(0, n):
        if j != i:
            result *= (x_int-x[j])/(x[i]-x[j])
    return result

def lagrange_int(x,y,x_int):
    if len(x) != len(y):
        return 'x and y vectors need to have the same length!'
    
    result = 0
    for i in range(0, len(x)):
        result += y[i]*lagrange(len(x),i,x_int,x)
    
    return result

x_int = 3750
x = np.array([0,2500,5000,10000],dtype=np.float)
y = np.array([1013,747,540,226],dtype=np.float)

print('Resultat:', lagrange_int(x,y,x_int))