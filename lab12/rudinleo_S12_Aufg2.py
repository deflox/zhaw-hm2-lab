import numpy as np
import matplotlib.pyplot as plt
from rudinleo_S11_Aufg1 import rudinleo_S11_Aufg1
from rudinleo_S12_Aufg1 import rudinleo_S12_Aufg1

# aufgabe a

def y(t):
    return (t/2.)+(9./(2.*t))

def y_diff(t,y):
    return 1-(y/t)

y0 = 5
h = 0.01
a = 1
b = 6
n = int((b-a)/h)

# plot vector field
rudinleo_S11_Aufg1(y_diff, a, b, 3, 5, 0.25, 0.1)

# plot exact solution
t_values = np.arange(a,b,h)
plt.plot(t_values,y(t_values),label='Exakte Lösung')

# plot runge kutta solution
x_runge_kutta,y_runge_kutta = rudinleo_S12_Aufg1(y_diff, a, b, n, y0)
plt.plot(x_runge_kutta,y_runge_kutta,label='Numerische Lösung')

plt.grid()
plt.legend()
plt.show()

# aufgabe b

# aufgabe c

# aufgabe d