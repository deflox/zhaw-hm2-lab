import numpy as np
import matplotlib.pyplot as plt
from rudinleo_S11_Aufg1 import rudinleo_S11_Aufg1
from rudinleo_S11_Aufg3 import rudinleo_S11_Aufg3
from rudinleo_S12_Aufg1 import rudinleo_S12_Aufg1


def f(x):
    return np.sqrt((2*x**3)/3+4)

def f_diff(x,y):
    return x**2/y

h = 0.1
a = 0
b = 10
n = int((b-a)/h)
y0 = 2.

x,y_euler,y_mittelpunkt,y_modeuler = rudinleo_S11_Aufg3(f_diff, a, b, n, y0)
x,y_runge_kutta = rudinleo_S12_Aufg1(f_diff, a, b, n, y0)


# plot vector field
rudinleo_S11_Aufg1(f_diff, a, b, 1, 25, 0.25, 0.25)

# plot correct solution
x_values = np.arange(a,b,h)
y_values = f(x_values)
plt.plot(x_values,y_values,label='Exakte Lösung')

# plot numeric solutions
plt.plot(x,y_euler,label='Euler Verfahren')
plt.plot(x,y_mittelpunkt,label='Mittelpunkt Verfahren')
plt.plot(x,y_modeuler,label='Modifiziertes Euler-Verfahren')
plt.plot(x,y_runge_kutta,label='Runge Kutta')

#plt.xlim(3.1,3.2)
#plt.ylim(4.95,5.05)
plt.grid()
plt.legend()
plt.show()