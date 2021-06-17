import numpy as np

def klassisches_runge_kutta_verfahren(f,a,b,n,y0):
    x,h = np.linspace(a,b,n+1,retstep=True,endpoint=True)
    y = np.zeros(np.shape(x)[0])
    y[0] = y0
    
    for i in range(0,len(x)-1):
        k1=f(x[i],y[i])
        k2=f(x[i]+h/2,y[i]+(h/2)*k1)
        k3=f(x[i]+h/2,y[i]+(h/2)*k2)
        k4=f(x[i]+h,y[i]+h*k3)
        y[i+1]=y[i]+(h*(1./6.)*(k1+2*k2+2*k3+k4))
    
    return x,y