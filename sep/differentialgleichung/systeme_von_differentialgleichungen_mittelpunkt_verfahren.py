import numpy as np
import matplotlib.pyplot as plt

t0=0   # startzeitpunkt (parameter)

x0=0   # ort (y der ursprungsfunktion)
v0=100 # geschwindigkeit (y der ersten ableitung)

m=97000

def f(t,z):
    return np.array([z[1],(-5*z[1]**2)/m-570000/m]) # z fängt mit index 0 an

h=0.1
a=0
b=20
n=int((b-a)/h)
rows=2

t = np.zeros(n+1)
z = np.zeros([rows,n+1])

t[0]=a
z[:,0]=np.array([x0,v0])

for i in range(0,n):
    th2 = t[i]+h/2
    zh2 = z[:,i] + h/2*f(t[i],z[:,i])
    t[i+1] = t[i]+h
    z[:,i+1] = z[:,i] + h* f(th2,zh2)

plt.plot(t,z[0,:],t,z[1,:]), plt.legend(["x(t)", "x'(t)"])  