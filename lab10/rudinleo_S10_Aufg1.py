import numpy as np
from rudinleo_S9_Aufg3 import rudinleo_S9_Aufg3

def f(x):
    return np.cos(x**2)

a = 0
b = np.pi
m = 4

T = rudinleo_S9_Aufg3(f,a,b,m)

print('Integralwert: ', T)