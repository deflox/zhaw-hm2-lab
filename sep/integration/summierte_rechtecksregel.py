import numpy as np

def summierte_rechtecksregel(f, a, b, n):
    h = (b-a)/n
    f_sum = 0
    for i in range(n):
        f_sum += f((a+i*h)+(h/2))
    
    return h*f_sum

def summierte_rechtecksregel_verbose(f, a, b, n):
    h = (b-a)/n
    f_sum = ""
    for i in range(n):
        print("f(" + str((a+i*h)+(h/2)) + ") =", f((a+i*h)+(h/2)))
        f_sum += str(f((a+i*h)+(h/2)))
        if (i != n-1):
            f_sum += " + "
    
    print(str(h) + " * " + " (" + f_sum + ")")

def f(x):
    return 1/x

a = 2
b = 4
n = 4
h = 0.5
# n = np.int((b-a)/h)

summierte_rechtecksregel_verbose(f, a, b, n)
print('Resultat:', summierte_rechtecksregel(f, a, b, n))