from rudinleo_S11_Aufg1 import rudinleo_S11_Aufg1

def f(x,y):
    return x**2 + 0.1*y

xmin = -2
xmax = 2
ymin = -0.5
ymax = 3.5
hx = 0.25
hy = 0.25

rudinleo_S11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy)