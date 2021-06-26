import numpy as np

def gauss_formeln(f,a,b,n):
    if n == 1:
        return (b-a)*f((b-a)/2)
    elif n == 2:
        return ((b-a)/2) * ( f( (-1/np.sqrt(3)) * ((b-a)/2) + ((b+a)/2) ) + f( (1/np.sqrt(3)) * ((b-a)/2) + ((b+a)/2) ) )
    elif n == 3:
        return ((b-a)/2) * ( (5/9) * f( -np.sqrt(0.6) * ((b-a)/2) + ((b+a)/2) ) + (8/9)*f((b+a)/2) ) + ((b-a)/2) * ( (5/9) * f( np.sqrt(0.6) * ((b-a)/2) + ((b+a)/2) ) )
    else:
        return "Unknown n value"
    
    
def f(x):
    return np.exp(-x**2)

a = 0
b = 0.5
n = 3

print("Lösung mittels Gauss-Formeln:", gauss_formeln(f,a,b,n))