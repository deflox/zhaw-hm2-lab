import numpy as np
import sys

# aufgabe a

def lagrange(n,i,x_int,x):
    result = 1
    for j in range(0, n):
        if j != i:
            result *= (x_int-x[j])/(x[i]-x[j])
    return result

def lagrange_int(x,y,x_int):
    if len(x) != len(y):
        sys.exit("x and y vectors need to have the same length!")
    
    result = 0
    for i in range(0, len(x)):
        print(lagrange(len(x),i,x_int,x))
        result += y[i]*lagrange(len(x),i,x_int,x)
    
    return result

# vorgegebene datenpunkte
x = np.array([-1,0,2,3], dtype=float)
y = np.array([-2,0,4,0], dtype=float)

# gesuchter zu interpolierender wert
x_int = 1

print('Resultat:', lagrange_int(x,y,x_int))

# aufgabe b