import numpy as np
import matplotlib.pyplot as plt

def df(x):
    return np.exp(-x**2)*(-2+4*x**2)

a = 0
b = 0.5
err = 10**-5

# plot
x_values = np.arange(a,b,0.001)
y_values = df(x_values)

plt.plot(x_values, y_values)
plt.xlim(a, b)
plt.grid()
plt.show()

# identify biggest slope
max_slope = np.max(np.abs(y_values))

print('Höchste Steigung auf Interval [a,b]:', max_slope)

# summierte rechteck regel
h = np.sqrt((err*24)/((b-a)*max_slope))
n = round((b-a)/h, 0)

print('h summierte Rechteck-Regel:', h)
print('n summierte Rechteck-Regel:', n)

# summierte trapez regel
h = np.sqrt((err*12)/((b-a)*max_slope))
n = round((b-a)/h, 0)

print('h summierte Trapez-Regel:', h)
print('n summierte Trapez-Regel:', n)

# simpsons-regel
# h = np.sqrt(np.sqrt((err*2880)/((b-a)*max_slope)))
# n = round((b-a)/h, 0)

print('h Simpsons-Regel:', h)
print('n Simpons-Regel:', n)