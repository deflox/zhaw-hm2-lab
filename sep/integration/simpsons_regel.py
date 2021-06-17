def simpson_regel(f, a, b, n):
    h = (b-a)/n
    res = (f(a)+f(b))/2
    for i in range(1,n+1):
        xi = a+i*h
        xim = xi-h
        res = res + f(xi) + 2.*f((xim+xi)/2.)
    
    res = res - f(xi)
    return (h/3.*res)

def f(x):
    return 1/x

a = 2
b = 4
n = 4
h = 0.5
# n = np.int((b-a)/h)

print('Resultat:', simpson_regel(f, a, b, n))