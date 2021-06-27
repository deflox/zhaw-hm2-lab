import numpy as np

L=1
R=80
C=4*10**(-4)
U=100

def f(t,z):
    return np.array([z[1],( (U-R*z[1]-(z[0])/(C)) / L )]) # z fängt mit index 0 an

h=0.01
a=0
b=1
n=int((b-a)/h)
rows=2

t = np.zeros(n+1)
z = np.zeros([rows,n+1])

t[0]=a
z[:,0]=np.array([0,0])

for i in range(0,1):
    th2 = t[i]+h/2
    print(th2)
    zh2 = z[:,i] + h/2*f(t[i],z[:,i])
    print(zh2)
    t[i+1] = t[i]+h
    print(t[i+1])
    z[:,i+1] = z[:,i] + h* f(th2,zh2)
    print(z[:,i])
    print(f(th2,zh2))
    print(z[:,i+1])