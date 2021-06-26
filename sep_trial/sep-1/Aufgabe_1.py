import numpy as np

# aufgabe b

def summierte_trapezregel(f, a, b, n):
    h = (b-a)/n
    f_sum = 0
    for i in range(1,n):
        f_sum += f(a+i*h)
    
    return h * ( ( (f(a) + f(b)) / 2 ) + f_sum )

def summierte_trapezregel_verbose(f, a, b, n):
    h = (b-a)/n
    fa = f(a)
    fb = f(b)
    
    f_sum = ""
    for i in range(1,n):
        print("f(" + str(a+i*h) + ") =", f(a+i*h))
        f_sum += str(f(a+i*h))
        if i != n-1:
            f_sum += " + "
            
    print()        
    print(str(h) + " * ( (" + str(fa) + " + " + str(fb) + " / 2) + " + f_sum + " )")

u=2000
m0=10000
q=100
g=9.8

def v(t):
    return u*np.log(m0/(m0-q*t))-g*t

a=0
b=30
h = 10
n = int((b-a)/h)

summierte_trapezregel_verbose(v, a, b, n)
print(summierte_trapezregel(v, a, b, n))

# aufgabe c

import matplotlib.pyplot as plt

def df(t):
    return (u*q**2)/((m0-q*t)**2)

a = 0
b = 30
err = 0.1

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

# summierte trapez regel
h = np.sqrt((err*12)/((b-a)*max_slope))
n = round((b-a)/h, 0)

print('h summierte Trapez-Regel:', h)
print('n summierte Trapez-Regel:', n)