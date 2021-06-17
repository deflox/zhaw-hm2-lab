import numpy as np

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

def f(x):
    return 1/x

a = 2
b = 4
n = 4
h = 0.5
# n = np.int((b-a)/h)

summierte_trapezregel_verbose(f, a, b, n)
print('Resultat:', summierte_trapezregel(f, a, b, n))