import numpy as np
import matplotlib.pyplot as plt

# aufgabe 3a
x = np.array([1981,1984,1989,1993,1997,2000,2001,2003,2004,2010])
y = np.array([0.5,8.2,15.,22.9,36.6,51.,56.3,61.8,65.,76.7])
z = np.polyfit(x,y,9)

def f(x):
    return np.polyval(z,x)

x_values = np.arange(1975,2020,0.1)

plt.plot(x_values,f(x_values),label='polyfit')
plt.grid()
plt.ylim(-100,250)

print(f(2020))

# aufgabe 3b
print('Schätzwert für 2020:', f(2020))

'''
Der Schätzwert liegt bei 122, dieser liegt über 100%, was nicht sein kann, da
nicht mehr als 100% der Bevölkerung einen Computer besitzen können.
'''

# aufgabe 3c
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
def lagrange_int_vec(x,y,x_int_vec):
    result = np.zeros(len(x_int_vec))
    for i in range(0,len(x_int_vec)):
        result[i] = lagrange_int(x,y,x_int_vec[i])
    return result

y_values_lagrange = lagrange_int_vec(x, y, x_values)
plt.plot(x_values,y_values_lagrange,label='lagrange')
plt.legend()
plt.show()

'''
Diese bricht an den Grenzen sehr stark aus.
'''