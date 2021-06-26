import numpy as np
import sys

def allgemeines_runge_kutta_verfahren(f,x1,x2,n,y0,a,b,c):
    if len(b) != len(c):
        sys.exit("b and c arrays need to have the same length")
        
    if len(b)-1 != len(a):
        sys.exit("there are not enough a records")
    
    k = np.zeros(len(b))
    x,h = np.linspace(x1,x2,n+1,retstep=True,endpoint=True)
    y = np.zeros(np.shape(x)[0])
    y[0] = y0
    
    for w in range(0,len(x)-1):
        
        # calculate all k values
        for i in range(0,len(c)):
            # use a values with previously calculated k values
            a_value = 0
            if i != 0:
                for z in range(0,len(a[i-1])):
                    #print("c_",i+1,":","a_",i,z+1,"=",a[i-1][z],"*","k_",z+1,"=",k[z],"*h=",h,sep="")
                    a_value += a[i-1][z]*k[z]*h
            
            #print("k_",i," ",x[i]+c[i]*h,y[i]+a_value)
            # calculate new k
            k[i]=f(x[w]+c[i]*h,y[w]+a_value)
        
        # calculate new y value
        k = b*k
        y[w+1]=y[w]+h*np.sum(k)
        
    return x,y       

# parameter im beispiel hier entsprechen den parametern für das runge
# kutta verfahren
c = np.array([0,0.5,0.5,1],dtype=float)
b = np.array([1/6,1/3,1/3,1/6],dtype=float)

# a werte im schema von oben nach unten
# für mehr werte einfach mehr variablen definieren und im a-array hinzufügen
a2 = np.array([0.5],dtype=float)
a3 = np.array([0,0.5],dtype=float)
a4 = np.array([0,0,1],dtype=float)
a = np.array([a2,a3,a4],dtype=object)

# differentialgleichung
def f(x,y):
    return x**2+0.1*y

# interval dem gefolgt werden soll und anzahl subintervalle
x1 = -1.5
x2 = 1.5
n = 5

# anfangswert y(-1.5)=0
y0 = 0

x,y = allgemeines_runge_kutta_verfahren(f,x1,x2,n,y0,a,b,c)

print("x-werte:", x)
print("y-werte:", y)