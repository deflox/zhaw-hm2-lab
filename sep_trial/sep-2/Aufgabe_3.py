# aufgabe a

'''
Spline-Interpolationen haben folgende Vorteile:
- es gibt keine Knicke was in diesem Fall eher ein Nachteil wäre
- Polynom Interpolationen können an oszillieren, was für eine Fahrbahn eines Autos auch nachteilig wäre

'''

# aufgabe c
import numpy as np
import matplotlib.pyplot as plt

def spline_interpolation(x,y,xx):
    n = x.shape[0]-1
    
    # step 1
    a = np.copy(y[0:n])
    
    # step 2
    h = x[1:n+1] - x[0:n]
    
    # step 3
    c = np.zeros(n+1)
    
    # step 4
    if n >= 2:
        
        A = np.zeros((n-1,n-1))
        for i in range(n-1):
            A[i,i] = 2*(h[i]+h[i+1])
            
        for i in range(0,n-2):
            A[i,i+1] = h[i]
            A[i+1,i] = h[i]
            
        z = 3*((y[2:n+1]-y[1:n])/h[1:n] - (y[1:n]-y[0:n-1])/h[0:n-1])
        c[1:n] = np.linalg.solve(A,z).reshape((n-1))
        
    # step 5
    b = (y[1:n+1]-y[0:n])/h - h/3*(c[1:n+1]+2*c[0:n])
    
    # step 6
    d = (c[1:n+1]-c[0:n])/(3*h)
    
    # evaluate
    m = xx.shape[0]
    yy = np.zeros(m)
    for j in range(0,m):
        i = 0
        while xx[j] > x[i+1]:
            i = i+1
        t = xx[j] - x[i]
        yy[j] = a[i] + t*(b[i] + t*(c[i] + t*d[i]))
        
    # plot
    plt.plot(x,y,'o')
    plt.plot(xx,yy,'x')
    for i in range(0,n):
        x0 = x[i]
        x1 = x[i+1]
        t = np.linspace(0, x1-x0)
        plt.plot(x0+t, a[i] + t*(b[i] + t*(c[i] + t*d[i])), '--')
        
    plt.legend(['Stützpunkte', 'Interpolationspunkte'])
    plt.show()
    
    # print koefficients
    for i in range(n):
        print('S_', i, ':', ' a=', a[i], ' b=', b[i], ' c=', c[i], ' d=', d[i], sep='')
    
    return yy

x = np.array([0,2,6],dtype=float)
y = np.array([0.1,0.9,0.1],dtype=float)
xx = np.array([])

yy = spline_interpolation(x, y, xx)