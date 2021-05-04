from rudinleo_S11_Aufg3 import rudinleo_S11_Aufg3

def f(x,y):
    return x**2/y
    
a = 0
b = 1.4
n = 3
y0 = 2.

x,y_euler,y_mittelpunkt,y_modeuler = rudinleo_S11_Aufg3(f, a, b, n, y0)

print('x: \n', x)
print('y_euler: \n', y_euler)
print('y_mittelpunkt: \n', y_mittelpunkt)
print('y_modeuler: \n', y_modeuler)