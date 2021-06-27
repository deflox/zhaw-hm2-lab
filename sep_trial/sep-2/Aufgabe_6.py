import numpy as np

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

def romberg_extrapolation(f, a, b, m):
    res = np.ones((m+1,m+1))
    
    for j in range(0,m+1):
        h = (b-a)/2**j
        
        print()
        print()
        print("T_",j,"0=",sep="")
        summierte_trapezregel_verbose(f, a, b, int((b-a)/h))
                
        res[j][0] = h*((f(a)+f(b))/2);
        for i in range(1,2**j):
            res[j][0] += h*f(a+i*h)
            
    for j in range(1,m+1):
        res[0:m+1-j,j] = (4**j*res[:,j-1][1:m+2-j]-res[:,j-1][0:m+1-j])/(4.**j-1)
    
    print(res)
    #print()
    
    return res[0][m]

# funktion die integriert werden soll
def f(t):
    return 2*np.exp(-(t/10-2)**4)

# integration von bis
a = 0
b = 40

# stufen der extrapolation
m = 3

I = romberg_extrapolation(f,a,b,m)

print('Integralwert:', I)