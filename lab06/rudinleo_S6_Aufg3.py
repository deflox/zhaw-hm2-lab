import numpy as np
import matplotlib.pyplot as plt

# aufgabe 3a

'''
0_1 steht für b
0_2 steht für a
'''

data=np.array([
    [1971, 2250.],
    [1972, 2500.],
    [1974, 5000.],
    [1978, 29000.],
    [1982, 120000.],
    [1985, 275000.],
    [1989, 1180000.],
    [1989, 1180000.],
    [1993, 3100000.],
    [1997, 7500000.],
    [1999, 24000000.],
    [2000, 42000000.],
    [2002, 220000000.],
    [2003, 410000000.],
])

A = np.zeros((np.shape(data)[0],2))
A[:,0] = 1
A[:,1] = data[:,0] - 1970

Q,R = np.linalg.qr(A)

# beim ausrechnen müssen die y-Werte logarithmiert werden
lamda = np.linalg.solve(R,np.matmul(Q.T, np.log10(data[:,1])))

def F(t, lamda):
    return 10.**(lamda[0]+(t-1970.)*lamda[1])

plt.plot(data[:,0],data[:,1],'ro')
plt.plot(data[:,0],F(data[:,0],lamda),label='Ausgleichsfunktion')
plt.legend()
plt.grid()
plt.show()

plt.semilogy(data[:,0],data[:,1],'ro')
plt.semilogy(data[:,0],F(data[:,0],lamda),label='Ausgleichsfunktion')
plt.legend()
plt.grid()
plt.show()

# aufgabe 3b
print('Transitoren im Jahr 2015: ', F(2015,lamda))

# aufgabe 3c
print('Theta0 =', lamda[0])
print('Theta1 =', lamda[1])