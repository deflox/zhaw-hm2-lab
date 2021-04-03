import numpy as np
import matplotlib.pyplot as plt

'''
Calculates the natural cubic spine function for the given set of x and y
values. It is then used to calculate the yy values for the given set of
xx values. The resulting yy values are then plotted onto the spine function.
'''
def rudinleo_S5_Aufg2(x,y,xx):
    if (len(x) != len(y)):
        'Amount of x values does not match with y values.'
        
    if (x[0] > xx[0] or x[len(x)-1] < xx[len(xx)-1]):
        'xx values need to be in the range of the x values'
    
    n = len(x) - 1
    
    # calculate a_i values
    a = np.copy(y[0:n])
    
    # calculate h_i values
    h = x[1:] - x[0:n]
    
    # calculate c_i values
    A = np.zeros((n-1,n-1))
    z = np.zeros(n-1)    
    for i in range(1, n): # n is taken since it is not included in the range       
        if i == 1:
            A[0][0] = 2*(h[0]+h[1])
            A[0][1] = h[1]
            z[0] = 3*((y[2]-y[1])/h[1]) - 3*((y[1]-y[0])/h[0])
        elif i == (n-1):
            A[i-1][i-2] = h[n-2]
            A[i-1][i-1] = 2*(h[n-2]+h[n-1])
            z[i-1] = 3*((y[n]-y[n-1])/h[n-1]) - 3*((y[n-1]-y[n-2])/h[n-2])
        else:
            A[i-1][i-2] = h[i-1]
            A[i-1][i-1] = 2*(h[i-1]+h[i])
            A[i-1][i] = h[i]
            z[i-1] = 3*((y[i+1]-y[i])/h[i]) - 3*((y[i]-y[i-1])/h[i-1])
    
    c = np.zeros(n+1)
    c[1:n] = np.linalg.solve(A,z)
    
    # calculate b_i
    b = ((y[1:] - y[0:n])/h) - (h/3*(c[1:] + 2*c[0:n]))
    
    # calculate d_i
    d = 1/(3*h)*(c[1:] - c[0:n])
    
    # plot function
    yy = np.zeros(len(xx))
    for i in range(0, n):
        # plot spline part
        x_values = np.arange(x[i], x[i+1], 0.01)
        y_values = a[i] + b[i]*(x_values-x[i]) + c[i]*(x_values-x[i])**2 + d[i]*(x_values-x[i])**3
        plt.plot(x_values, y_values, label='S'+str(i))
        
        # calculate and plot xx points that are within the current range
        for z in range(0, len(xx)):
            if (xx[z] >= x[i] and xx[z] < x[i+1]):
                yy[z] = a[i] + b[i]*(xx[z]-x[i]) + c[i]*(xx[z]-x[i])**2 + d[i]*(xx[z]-x[i])**3
                plt.plot(xx[z], yy[z], 'ro')
        
    plt.legend()
    plt.show()    
    
    return yy