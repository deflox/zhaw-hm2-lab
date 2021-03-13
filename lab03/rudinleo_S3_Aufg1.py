import numpy as np
import sympy as sp

x1, x2 = sp.symbols('x1 x2')
f1 = 20-18*x1-2*x2**2
f2 = -4*x2*(x1-x2**2)

f = sp.Matrix([f1,f2])
x = sp.Matrix([x1,x2])
Df = f.jacobian(x)

print('Jacobi-Matrix: \n', Df)

# create numpy functions based on the sympy functions
# argument should be a 2d column vector
f_func = sp.lambdify([ [[x1],[x2]] ], f, 'numpy')
Df_func = sp.lambdify([ [[x1],[x2]] ], Df, 'numpy')

steps = 4
x_prev = 0
x_current = np.array([[1.1],[0.9]])

for i in range(1,steps+1):
    f_result = f_func(x_current)
    Df_result = Df_func(x_current)
    d_result = np.linalg.solve(Df_result,-f_result)
    x_prev = x_current
    x_current = x_current + d_result
    
    print()
    print(str(i) + '. Iterationsschritt:')
    print('Resultat Jacobi-Matrix: \n', Df_result)
    print('Resultat -f(x): \n', -f_result)
    print('Resultat delta: \n', d_result)
    print('Resultat x: \n', x_current)
    
    print('||f(x)||: \n', np.linalg.norm(f_result,2))
    print('||x_current-x_prev||: \n', np.linalg.norm(x_current-x_prev,2))        