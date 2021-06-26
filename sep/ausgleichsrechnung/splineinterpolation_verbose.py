import numpy as np
import sys

def splineinterpolation_verbose(x,y,xx):
    if (len(x) != len(y)):
        sys.exit('Amount of x values does not match with y values.')
        
    if (x[0] > xx[0] or x[len(x)-1] < xx[len(xx)-1]):
        sys.exit('xx values need to be in the range of the x values')
        
    n = len(x) - 1
    
    # calculate a_i values
    for i in range(0,n):
        print("a_" + str(i) + " = " + str(y[i]))
        
    print()
    
    # calculate h_i values
    for i in range(0,n):
        print("h_", i, " = x_", i+1, " - x_", i, " = ", x[i+1]-x[i], sep="")
    
    print()
    
    # calculate c_i values
    print("c_0 =", 0)
    
    for i in range(1,n):
        if i == 1:
            print("2*(h_0 + h_1)*c_1 + h_1*c_2 = 3*(y_2-y_1)/h_1 - 3*(y_1-y_0)/h_0")
        if i == n-1:
            print("h_(n-2)*c_(n-2) + 2*(h_(n-2)+h_(n-1))*c_(n-1) = 3*(y_n-y_(n-1))/h_(n-1) - 3*(y_(n-1)-y_(n-2))/h_(n-2)")
    
    print("c_", n, " = ", 0, sep="")
    

x = np.array([4,6,8,10],dtype=float)
y = np.array([6,3,9,0],dtype=float)
xx = np.array([5,7,9])

yy = splineinterpolation_verbose(x, y, xx)